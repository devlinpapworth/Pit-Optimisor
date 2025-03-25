# Mineral identification system
''' Here I am defining global variables, lists and dictionaries although they
 are passed into functions.'''

wik_dict = {'Molybdenite': 'https://en.wikipedia.org/wiki/Molybdenite',
            'Graphite': 'https://en.wikipedia.org/wiki/Graphite',
            'Covellite': 'https://en.wikipedia.org/wiki/Covellite',
            'Galena': 'https://en.wikipedia.org/wiki/Galena',
            'Chalcocite': 'https://en.wikipedia.org/wiki/Chalcocite',
            'Bornite': 'https://en.wikipedia.org/wiki/Bornite',
            'Chalcopyrite': 'https://en.wikipedia.org/wiki/Chalcopyrite',
            'Limonite (Goethite)': 'https://en.wikipedia.org/wiki/Limonite',
            'Hematite': 'https://en.wikipedia.org/wiki/Limonite',
            'Magnetite': 'https://en.wikipedia.org/wiki/Magnetite',
            'Pyrite': 'https://en.wikipedia.org/wiki/Pyrite',
            'Talc': 'https://en.wikipedia.org/wiki/Talc',
            'Sulfur': 'https://en.wikipedia.org/wiki/Sulfur',
            'Realgar': 'https://en.wikipedia.org/wiki/Realgar',
            'Gypsum': 'https://en.wikipedia.org/wiki/Gypsum',
            'Sylvite': 'https://en.wikipedia.org/wiki/Sylvite',
            'Halite': 'https://en.wikipedia.org/wiki/Halite',
            'Biotite Mica': 'https://en.wikipedia.org/wiki/Biotite',
            'Muscovite Mica': 'https://en.wikipedia.org/wiki/Muscovite',
            'Bauxite': 'https://en.wikipedia.org/wiki/Bauxite',
            'Calcite': 'https://en.wikipedia.org/wiki/Calcite',
            'Barite': 'https://en.wikipedia.org/wiki/Baryte',
            'Dolomite': 'https://en.wikipedia.org/wiki/Dolomite_(mineral)',
            'Malachite': 'https://en.wikipedia.org/wiki/Malachite',
            'Sphalerite': 'https://en.wikipedia.org/wiki/Sphalerite',
            'Fluorite': 'https://en.wikipedia.org/wiki/Fluorite',
            'Apatite': 'https://en.wikipedia.org/wiki/Apatite',
            'Augite (pyroxene)': 'https://en.wikipedia.org/wiki/Augite',
            'Hornblende (amphibole)':
                'https://en.wikipedia.org/wiki/Hornblende',
            'Olivine': 'https://en.wikipedia.org/wiki/Olivine',
            'Plagioclase feldspar (including Albite, Labradorite, etc.)':
                'https://en.wikipedia.org/wiki/Plagioclase',
            'Potassium feldspar (Orthoclase, Microcline)':
                'https://en.wikipedia.org/wiki/Plagioclase',
            'Quartz (crystalline varieties)':
                'https://en.wikipedia.org/wiki/Quartz',
            'Silica (Chalcedony varieties)':
                'https://en.wikipedia.org/wiki/Silicate_mineral',
            'Garnet group (Almandine, etc.)':
                'https://en.wikipedia.org/wiki/Garnet',
            'Tourmaline': 'https://en.wikipedia.org/wiki/Tourmaline',
            'Corundum': 'https://en.wikipedia.org/wiki/Corundum'}

met_or_not_met = 0
which_table = 0
met_hardness_list = []
answer_list = []
mineral_potential_list = []
colour_dict = {}
streak_dict = {}
luster_dict = {}
cleavage_dict = {}
composition_dict = {}
other_dict = {}
name_list = []

'''This first funciton is the intial question asked when code started. The user
decides where the next path goes, either what there mineral luster is or if
they would like to enter a new mineral.'''


def start_and_luster_type():
    name_to_data = {}
    met_or_not_met = 0
    print("How would you describe the luster? ")
    print("     Enter 1 for metallic to submetallic")
    print("     Enter 2 for non metallic ")
    print("     If you are unsure make a guess and if not found try again.")
    print("If you would like to enter a new mineral then enter 'Yes'")
    met_or_not_met = input("Please enter stop if you"
                           " would like to end the system:   ")
    met_or_not_met = met_or_not_met.strip(" ").capitalize()

    if met_or_not_met == "1":
        which_table = 1

    elif met_or_not_met == "2":
        which_table = 2

    elif met_or_not_met == "Stop":
        print("==============================================================="
              "==============================================================="
              "==============================================================="
              "====================================")
        print("code terminated")
        # print summary message as ends while loop from main code file
        which_table = 0
    elif met_or_not_met == "Yes":
        which_table = "Yes"
    else:
        print(f"{met_or_not_met} is not a valid input please enter 1, 2"
              " or Stop to end code: ")
        which_table = 0
# acounting for user invalid input
    return (name_to_data, which_table, met_or_not_met)


'''The split data function splits data on commas unless it sees a opening
bracket then will stop splitting on commas untill the code sees the
corrosponding closing bracket then will resume splitting on commas. This
function is key for transfering the data from the two data files into code
that is readable and transferable by my code. An issue I incountered was that
when minerals could have multiple colours, for example, when splitting on
commas and using the index of this list all the mineral classifications would
be incorect. Therefore surrounding clasifications in brackets when needed
allowed me to correctly handle the data. Sources used:
(https://stackoverflow.com/questions/26633452/
how-to-split-by-commas-that-are-not-within-parentheses)  '''


def split_data(data_line):
    data = []
    letters = []
    gap = 0
    for i in data_line:
        if i == "(":
            gap += 1
        elif i == ")":
            gap -= 1
        if not gap and i == ",":
            data.append("".join(letters))
            letters = []
        else:
            if len(letters):
                letters.append(i)
            elif i not in ")":
                letters.append(i)
    data.append("".join(letters))

    return (data)


'''hard_array, data_array and composition_and_other_array transfer the data
from either table one or table two and take each classification of minerals
and transfer them into a list that is then put into a dictionary where the key
is the mineral name and the values are the list of streak, colour, etc. '''


def hard_array(line, text_to_remove):
    for p in text_to_remove:
        line = line.replace(p, "")

    split = split_data(line)  # splits on commas
    hard = split[1]
    hard = hard.split("-")
    if len(hard) == 1:
        hard.append(hard[0])

    return (hard)


def data_array(c_s, number, line, text_to_remove):
    for p in text_to_remove:
        line = line.replace(p, "")

    split = split_data(line)  # splits on commas
    c_s = split[number]
    c_s = c_s.replace("(", "")
    c_s = c_s.replace(")", "")
    c_s = c_s.split(",")
    c_s = [i.strip(" ").capitalize() for i in c_s]
    return (c_s)


def composition_and_other_array(c_s, number, line, text_to_remove):
    for p in text_to_remove:
        line = line.replace(p, "")

    split = split_data(line)  # splits on commas
    c_s = split[number]
    c_s = split_data(c_s)
    c_s = [i.strip(" ") for i in c_s]
    return (c_s)


'''these two table functions are used once the user has chosen the luster type
of their mineral  '''


def table_1():
    name_to_data = {}
    streak = 1
    colour = 1
    cleavage = 1
    cleavage = 1
    composition = 1
    other = 1
    # opening metalic to submetalic lustre file and asigning data
    # to a variable
    data_met_1 = open("Met_submet_lustre.csv", "r")
    data_met_1.readline()
    data_met = data_met_1.readlines()
    data_met_1.close()
    text_to_remove = ['\t', '\n']
    for line in data_met:
        hard = hard_array(line, text_to_remove)

        colour_ = data_array(colour, 2, line, text_to_remove)

        streak_ = data_array(streak, 3,  line, text_to_remove)

        cleavage_ = data_array(cleavage, 4, line, text_to_remove)

        composition_ = composition_and_other_array(composition, 5, line,
                                                   text_to_remove)

        other_ = composition_and_other_array(other, 6, line, text_to_remove)

        split = split_data(line)
        name = split[0]
        name_to_data[name] = (hard, colour_, streak_, cleavage_, composition_,
                              other_)
    return (name_to_data)


def table_2():
    name_to_data = {}
    streak = 1
    colour = 1
    luster = 1
    cleavage = 1
    cleavage = 1
    composition = 1
    other = 1
    # opening non metalic lustre file and asigning data a variable
    data_met_1 = open("non_met_lustre.csv", "r")
    data_met_1.readline()
    data_met = data_met_1.readlines()
    data_met_1.close()
    text_to_remove = ['\t', '\n']
    for line in data_met:
        hard = hard_array(line, text_to_remove)

        colour_ = data_array(colour, 2, line, text_to_remove)

        streak_ = data_array(streak, 3, line, text_to_remove)

        luster_ = data_array(luster, 4,  line, text_to_remove)

        cleavage_ = data_array(cleavage, 5, line, text_to_remove)

        composition_ = composition_and_other_array(composition, 6, line,
                                                   text_to_remove)

        other_ = composition_and_other_array(other, 7, line, text_to_remove)

        split = split_data(line)
        name = split[0]

        name_to_data[name] = (hard, colour_, streak_, luster_, cleavage_,
                              composition_, other_)
    return (name_to_data)


'''Here the user inputs a value for hardness and if it is not inbetween 1-10
the user is asked too try again and if a value is entered in between 1-10 but
does not match any mineral they have the option to add a new mineral. '''


def ques_1():
    user_hardness = input("What is the hardness value (1-10) or"
                          " enter (?)?: ")
    user_hardness = user_hardness.strip(" ")
    return (user_hardness)


def hardness_final(name_to_data, user_hardness):
    if not (float(user_hardness) >= 1 and float(user_hardness) <= 10):
        print("Please enter a value inbetween 1-10")
        range_or_single = input("What is the hardness value (1-10) or"
                                " enter (?): ")
        range_or_single = range_or_single.capitalize()
        user_hardness = range_or_single.strip(" ")
    if user_hardness != "?":
        for i in list(name_to_data):
            low_end = name_to_data[i][0][0]
            high_end = name_to_data[i][0][1]
            if not (float(user_hardness) >=
                    float(low_end) and float(user_hardness) <=
                    float(high_end)):
                # remove this mineral from the potential answers
                del name_to_data[i]
    return (name_to_data)


'''Here for each classification of minerals an inital question is asked. Where
for the classification that is being tested a menu is printed giving number
options of the possible classifications of the minerals left in name_to_data.
The user then inputs the number for the relevant classification for their
mineral. All user inputs are checked and acounted for.'''


def ques_2(name_to_data):
    x = 1
    for line in name_to_data:
        for i in name_to_data[line][1]:
            i = i.strip(" ").capitalize()
            if i not in colour_dict.values():
                colour_dict[x] = i
                x += 1
    print(" ")
    print("Please enter the correct corresponding number for the colour"
          " of your mineral")
    print("")
    for i, j in colour_dict.items():
        print(str(i) + "." + str(j))
        print(" ")
    user_colour = input("Enter here or '?' if your not sure:   ")
    return (user_colour)


def colour_final(name_to_data, user_colour):
    user_colour = int(user_colour)
    while user_colour not in colour_dict and user_colour != "?":
        user_colour = input("Invalid answer."
                            "Enter answer here or '?' if your not sure:   ")
        if user_colour != "?":
            user_colour = int(user_colour)
    if user_colour != "?":
        for line in list(name_to_data):
            if colour_dict[user_colour] not in name_to_data[line][1]:
                del name_to_data[line]
    colour_dict.clear()
    return (name_to_data)


def ques_3(name_to_data):
    x = 1
    for line in name_to_data:
        for i in name_to_data[line][2]:
            i = i.strip(" ")
            if i not in streak_dict.values():
                streak_dict[x] = i
                x += 1
    print(" ")
    print("Please enter the correct corresponding number for the streak"
          " of your mineral:  ")
    print("")
    for i, j in streak_dict.items():
        print(str(i) + "." + str(j))
        print(" ")
    user_streak = input("Enter here or '?' if your not sure:   ")
    return (user_streak)


def streak_final(name_to_data, user_streak):
    user_streak = int(user_streak)
    while user_streak not in streak_dict and user_streak != "?":
        user_streak = input("Invalid answer."
                            " Enter answer here or '?' if your not sure:   ")
        if user_streak != "?":
            user_streak = int(user_streak)
    if user_streak != "?":
        for line in list(name_to_data):
            if streak_dict[user_streak] not in name_to_data[line][2]:
                del name_to_data[line]
    streak_dict.clear()
    return (name_to_data)


def ques_luster(name_to_data):
    x = 1
    for line in name_to_data:
        for i in name_to_data[line][3]:
            i = i.strip(" ")
            if i not in luster_dict.values():
                luster_dict[x] = i
                x += 1
    print(" ")
    print("Please enter the correct corresponding number for the luster type"
          " of your mineral:  ")
    print("")
    for i, j in luster_dict.items():
        print(str(i) + "." + str(j))
        print(" ")

    user_luster = input("Enter here or '?' if your not sure:   ")

    return (user_luster)


def luster_final(name_to_data, user_luster):
    user_luster = int(user_luster)
    while user_luster not in luster_dict and user_luster != "?":
        user_luster = input("Invalid answer."
                            " Enter answer here or '?' if your not sure:   ")
        if user_luster != "?":
            user_luster = int(user_luster)
    if user_luster != "?":
        for line in list(name_to_data):
            if luster_dict[user_luster] not in name_to_data[line][3]:
                del name_to_data[line]
    luster_dict.clear
    return (name_to_data)


def ques_4(name_to_data, number):
    x = 1
    for line in name_to_data:
        for i in name_to_data[line][number]:
            i = i.strip(" ")
            if i not in cleavage_dict.values():
                cleavage_dict[x] = i
                x += 1
    print(" ")
    print("Please enter the correct corresponding number for the cleavage"
          " of your mineral:  ")
    print("")
    for i, j in cleavage_dict.items():
        print(str(i) + "." + str(j))
        print(" ")

    user_cleavage = input("Enter here or '?' if your not sure:   ")

    return (user_cleavage)


def cleavage_final(name_to_data, user_cleavage, number):
    user_cleavage = int(user_cleavage)
    while user_cleavage not in cleavage_dict and user_cleavage != "?":
        user_cleavage = input("Invalid answer."
                              " Enter answer here or '?' if your not sure:   ")
        if user_cleavage != "?":
            user_cleavage = int(user_cleavage)
    if user_cleavage != "?":
        for line in list(name_to_data):
            if cleavage_dict[user_cleavage] not in name_to_data[line][number]:
                del name_to_data[line]
    cleavage_dict.clear()
    return (name_to_data)


def ques_5(name_to_data, number):
    x = 1
    for line in name_to_data:
        for i in name_to_data[line][number]:
            i = i.strip(" ")
            if i not in composition_dict.values():
                composition_dict[x] = i
                x += 1
    print(" ")
    print("Please enter the correct corresponding number for the composition"
          " of your mineral:  ")
    print("")
    for i, j in composition_dict.items():
        print(str(i) + "." + str(j))
        print(" ")

    user_composition = input("Enter here or '?' if your not sure:   ")

    return (user_composition)


def composition_final(name_to_data, user_composition, number):
    user_composition = int(user_composition)
    while user_composition not in composition_dict and user_composition != "?":
        user_composition = input("Invalid answer."
                                 " Enter asnser here or '?' if "
                                 "your not sure:  ")
        if user_composition != "?":
            user_composition = int(user_composition)
    if user_composition != "?":
        for line in list(name_to_data):
            if composition_dict[user_composition] not in (name_to_data
                                                          [line][number]):
                del name_to_data[line]
    composition_dict.clear()
    return (name_to_data)


def ques_6(name_to_data, number):
    x = 1
    for line in name_to_data:
        for i in name_to_data[line][number]:
            i = i.strip(" ")
            if i not in other_dict.values():
                other_dict[x] = i
                x += 1
    print(" ")
    print("Please enter the correct corresponding number for the other facts"
          " of your mineral:  ")
    print("")
    for i, j in other_dict.items():
        print(str(i) + "." + str(j))
        print(" ")

    user_composition = input("Enter here or '?' if your not sure:   ")

    return (user_composition)


def other_final(name_to_data, user_other, number):
    user_other = int(user_other)
    while user_other not in other_dict and user_other != "?":
        user_other = int(input("Invalid answer."
                               " Enter answer here or '?' if your not sure: "))
    if user_other != "?":
        for line in list(name_to_data):
            if other_dict[user_other] not in name_to_data[line][number]:
                del name_to_data[line]
    other_dict.clear()
    return (name_to_data)


'''Here is a function that allows the user to input a new mineral that is not
already in the data. They have the option to add their new mineral to the large
data set or to add it to a new file. '''


def new_mineral(count):
    file_or_new_file = 1
    while True:
        if file_or_new_file == "Stop":
            break  #
        else:
            try:
                print("Do you want to add your mineral to the larger"
                      " data set or to a new file to be"
                      " officalised enter 'L' for large "
                      "data set or enter 'N' for"
                      " new file. To stop adding new minerals enter (Stop)")
                met_or_not_met = 0
                file_or_new_file = input("Please input answer here:   ")
                file_or_new_file = file_or_new_file.strip(" ").capitalize()
                if file_or_new_file == "L":
                    met_or_not_met = input("How would you describe the lustre "
                                           "(Enter 1 for metalic to "
                                           "submetalic or "
                                           "enter 2 for non metalic)?   ")
                    met_or_not_met = met_or_not_met.strip(" ").capitalize()

                    if met_or_not_met == "1":
                        data_met = open("Met_submet_lustre.csv", "a")
                        name1 = input("What is the name?: ")
                        hardness1 = input("What is the hardness?: ")
                        colour1 = input("What is the colour?:  ")
                        streak1 = input("What is the streak?: ")
                        cleavage1 = input("What is the cleavage?: ")
                        composition1 = input("What is the composition?: ")
                        other1 = input("What are other facts?: ")
                        data_met.writelines(name1 + ", " + hardness1 + ", "
                                            + colour1 + ", " + streak1 +
                                            ", " + cleavage1 + ", " +
                                            composition1 + ", " + other1)
                        data_met.writelines('\n')
                        print(f"Mineral {name1} has been added")

                    elif met_or_not_met == "2":
                        data_met = open("non_met_lustre.csv", "a")
                        name1 = input("What is the name?: ")
                        hardness1 = input("what is the hardness?: ")
                        colour1 = input("What is the colour?:  ")
                        streak1 = input("What is the streak?: ")
                        luster1 = input("What is the luster?: ")
                        cleavage1 = input("What is the cleavage?: ")
                        composition1 = input("What is the composition?: ")
                        other1 = input("What are other facts?: ")

                        data_met.writelines(name1 + ", " + hardness1 + ", "
                                            + colour1 + ", " + streak1 +
                                            ", " + luster1 + ", " +
                                            cleavage1 + ", " +
                                            composition1 + ", " + other1)
                        data_met.writelines('\n')
                        print(f"Mineral {name1} has been added")

                    elif met_or_not_met == "Stop":
                        print("=============================================="
                              "=============================================="
                              "==============================================="
                              "======================================"
                              "============================")

                elif file_or_new_file == "N":
                    met_or_not_met = input("How would you describe the lustre."
                                           " (Enter 1 for metalic to "
                                           "submetalic or "
                                           "enter 2 for non metalic)?  ")
                    met_or_not_met = met_or_not_met.strip(" ").capitalize()

                    if met_or_not_met == "1":
                        data_met = open("user_mineral.csv", "a")
                        name1 = input("What is the name?: ")
                        hardness1 = input("What is the hardness?: ")
                        colour1 = input("What is the colour?:  ")
                        streak1 = input("What is the streak?: ")
                        cleavage1 = input("What is the cleavage?: ")
                        composition1 = input("What is the composition?: ")
                        other1 = input("What are other facts?: ")

                        data_met.writelines("Metalic to submetalic luster:   ")
                        data_met.writelines(name1 + ", " + hardness1 + ", "
                                            + colour1 + ", " + streak1 + ", " +
                                            cleavage1 + ", " + composition1 +
                                            ", " + other1)
                        data_met.writelines('\n')
                        print(f"Mineral {name1} has been added")

                    elif met_or_not_met == "2":
                        data_met = open("user_mineral.csv", "a")
                        name1 = input("What is the name?: ")
                        hardness1 = input("what is the hardness?: ")
                        colour1 = input("What is the colour?:  ")
                        streak1 = input("What is the streak?: ")
                        luster1 = input("What is the luster?: ")
                        cleavage1 = input("What is the cleavage?: ")
                        composition1 = input("What is the composition?: ")
                        other1 = input("What are other facts?: ")

                        data_met.writelines(name1 + ", " + hardness1 + ", " +
                                            colour1 + ", " + streak1 + ", " +
                                            luster1, + ", " + cleavage1 + ", "
                                            + composition1 + ", " + other1)
                        data_met.writelines('\n')
                        print(f"Mineral {name1} has been added")

                    elif met_or_not_met == "Stop":
                        print("==============================================="
                              "==============================================="
                              "==============================================="
                              "=================================="
                              "============================")
            except TypeError:
                print("There was an error with one of you inputs"
                      " please try again")
    return (count)


'''Here once the user has stopped the code a summary message of all the
minerals they have found is printed from outputs.txt file. '''


def summary_message():
    print("=================================================================="
          "=================================================================="
          "=================================================================="
          "===========================")
    outputs = open("outputs.txt", "r")
    summary = outputs.readlines()
    print("")
    print("The minerals you have found are:")
    for line in summary:
        print(line)
    outputs.close()


'''This function throughout the code will count how many minerals are left in
name_to_data and if only one left it will print what the mineral that is left.
If the count is greater than one a list of the minerals left is printed.
Lastly, if the mineral count is less than one the user is given the option to
add a new mineral.  '''


def count_of_mins(name_to_data):
    count = len(name_to_data)
    if count == 1:
        outputs = open("outputs.txt", "a")
        print("==============================================================")
        print("Your mineral is most likely: ")
        for key, values in name_to_data.items():
            key = str(key)
            print(key)
            print(f"Please use this link for more information on {key}:"
                  f" {wik_dict[key]}")
            outputs.writelines(f"{key} : {wik_dict[key]}")
            outputs.writelines('\n')
        outputs.close()
    elif count == 0:
        print("Error, no minerals match your description")
        new = input("Would you like to add a new mineral? "
                    "Enter Yes to add mineral or any key to carry on:  ")
        new = new.strip(" ").capitalize()

        if new == "Yes":
            new_mineral(count)
        else:
            print("Mineral Test Ended")

    else:
        print("=============================================================="
              "=====")
        print("Your possible minerals have been limited to: ")
        for key in name_to_data:
            print(key)

    print("==================================================================")
    return (name_to_data, count)
