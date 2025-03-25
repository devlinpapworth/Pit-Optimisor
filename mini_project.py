import mini_project_functions as file

# Mineral identification system
met_or_not_met = 0
which_table = 0
mineral_list = []

''' In this file I have taken the questions and the quesitons_final functions
from the mini_project_functions file and put them together into each quesion.
In each function here all possible user inputs are aconted for using
try and expect.
In t_1 and t_2 all of the question functions are put into one function. This
allows for in mini_project_run_code the user is asked luster type and depending
on their selection either t_1 or t_2 is opened and that code run.
If at any point the count of the dictionary name_to_data is one all questions
are skipped.'''


def question_one(name_to_data, count):
    if count > 1:
        user_hardness = file.ques_1()
        while True:
            # will loop untill user inputs a valid response
            try:
                if user_hardness == "?":
                    break  #
                else:
                    user_hardness = float(user_hardness)
                    name_to_data = file.hardness_final(name_to_data,
                                                       user_hardness)
                    break  # will only break if user inputs a number that
                    # satisfies hardness_final

            except ValueError:
                # when user inputs an incorrect value in
                print("You input was an invalid entry."
                      " Please try again")
                user_hardness = input("What is the hardness value (1-10)"
                                      " or enter (?): ")
                continue  #
        name_to_data, count = file.count_of_mins(name_to_data)

    return (name_to_data, count)


def question_two(name_to_data, count):
    if count > 1:
        user_colour = file.ques_2(name_to_data)
        while True:
            # will loop untill user inputs a valid response
            try:
                if user_colour == "?":
                    break   #
                else:
                    user_colour = float(user_colour)
                    name_to_data = file.colour_final(name_to_data, user_colour)
                    break  # will only break if user inputs a number that
                    # satisfies colour_final

            except ValueError:
                # when user inputs an incorrect value in
                print("You input was an invalid entry."
                      " Please try again")
                user_colour = input("Please enter the correct corresponding"
                                    " number for the colour of your mineral"
                                    " or enter (?):")
                continue  #
        name_to_data, count = file.count_of_mins(name_to_data)
    return (name_to_data, count)


def question_three(name_to_data, count):
    if count > 1:
        user_streak = file.ques_3(name_to_data)
        while True:
            # will loop untill user inputs a valid response
            try:
                if user_streak == "?":
                    break  #
                else:
                    user_streak = float(user_streak)
                    name_to_data = file.streak_final(name_to_data, user_streak)
                    break  # will only break if user inputs a number that
                    # satisfies streak_final

            except ValueError:
                # when user inputs an incorrect value in
                print("You input was an invalid entery."
                      " Please try again")
                user_streak = input("Please enter the correct corresponding"
                                    " number for the streak of your mineral "
                                    " or enter (?):")
                continue  #
        name_to_data, count = file.count_of_mins(name_to_data)
    return (name_to_data,  count)


'''Number controls the index level as depending on which file is openened as
the index will change becasue of the luster classification. This allows for the
functions to be used in both table functions whlst controlling for this change.
'''


def question_four(name_to_data, count, number):
    if count > 1:
        user_cleavage = file.ques_4(name_to_data, number)
        while True:
            # will loop untill user inputs a valid response
            try:
                if user_cleavage == "?":
                    break  #
                else:
                    user_cleavage = float(user_cleavage)
                    name_to_data = file.cleavage_final(name_to_data,
                                                       user_cleavage, number)
                    break   # will only break if user inputs a number that
                    # satisfies cleavage_final

            except ValueError:
                # when user inputs an incorrect value
                print("You input was an invalid entry."
                      " Please try again")
                user_cleavage = input("Please enter the correct corresponding"
                                      " number for the cleavage of your "
                                      "mineral? or enter (?):")
                continue  #
        name_to_data, count = file.count_of_mins(name_to_data)
    return (name_to_data, count)


def question_luster(name_to_data, count):
    if count > 1:
        user_luster = file.ques_luster(name_to_data)
        while True:
            # will loop untill user inputs a valid response
            try:
                if user_luster == "?":
                    break   #
                else:
                    user_luster = float(user_luster)
                    name_to_data = file.luster_final(name_to_data, user_luster)
                    break   # will only break if user inputs a number that
                    # satisfies luster_final

            except ValueError:
                # when user inputs an incorrect value
                print("You input was an invalid entry."
                      " Please try again")
                user_luster = input("Please enter the correct corresponding"
                                    " number for the luster of your "
                                    "mineral or enter (?):")
                continue  #
        name_to_data, count = file.count_of_mins(name_to_data)
    return (name_to_data, count)


def question_five(name_to_data, count, number):
    if count > 1:
        user_composition = file.ques_5(name_to_data, number)
        while True:
            # will loop untill user inputs a valid response
            try:
                if user_composition == "?":
                    break   #
                else:
                    user_composition = float(user_composition)
                    name_to_data = file.composition_final(name_to_data,
                                                          user_composition,
                                                          number)
                    break   # will only break if user inputs a number that
                    # satisfies composition_final

            except ValueError:
                # when user inputs an incorrect value
                print("You input was an invalid entry."
                      " Please try again")
                user_composition = input("Please enter the correct "
                                         "corrospinding number for the "
                                         "composition of your mineral"
                                         " or enter (?):   ")
                continue  #
        name_to_data, count = file.count_of_mins(name_to_data)
    return (name_to_data, count)


def question_six(name_to_data, count, number):
    if count > 1:
        user_other = file.ques_6(name_to_data, number)
        while True:
            # will loop until user inputs a valid response
            try:
                if user_other == "?":
                    break  #
                else:
                    user_other = float(user_other)
                    name_to_data = file.other_final(name_to_data,
                                                    user_other, number)
                    break   # will only break if user inputs a number that
                    # satisfies other_final

            except ValueError:
                # when user inputs an incorrect value
                print("You input was an invalid entry."
                      " Please try again")
                user_other = input("Please enter the correct "
                                   "corresponding number for the "
                                   "other properties of your mineral"
                                   " or enter (?):")
                continue  #
        name_to_data, count = file.count_of_mins(name_to_data)
    return (name_to_data, count)


'''Bellow the question functions have been compiled into the table one and
table two functions. '''


def t_1(name_to_data):
    name_to_data = file.table_1()
    name_to_data, count = file.count_of_mins(name_to_data)

    name_to_data, count = question_one(name_to_data, count)
    name_to_data, count = question_two(name_to_data, count)
    name_to_data, count = question_three(name_to_data, count)
    name_to_data, count = question_four(name_to_data, count, 3)
    name_to_data, count = question_five(name_to_data, count, 4)
    if count > 1:
        check_others = input("Would you like to classify your mineral"
                             " on other properties, if so type Yes if not "
                             "press any key ")
        check_others = check_others.strip(" ").capitalize()
        if check_others == "Yes":
            name_to_data = question_six(name_to_data, count, 5)


def t_2(name_to_data):
    name_to_data = file.table_2()

    name_to_data, count = file.count_of_mins(name_to_data)

    name_to_data, count = question_one(name_to_data, count)
    name_to_data, count = question_two(name_to_data, count)
    name_to_data, count = question_three(name_to_data, count)
    name_to_data, count = question_luster(name_to_data, count)
    name_to_data, count = question_four(name_to_data, count, 4)
    name_to_data, count = question_five(name_to_data, count, 5)
    if count > 1:
        check_others = input("Would you like to classify your mineral"
                             " on other properties, if so type Yes if not "
                             "press any key ")
        check_others = check_others.strip(" ").capitalize()
        if check_others == "Yes":
            name_to_data = question_six(name_to_data, count, 6)
