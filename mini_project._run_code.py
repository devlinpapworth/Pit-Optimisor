import mini_project_functions as f_file
import mini_project as c_file

''' An intial question will be asked to the user where their answer will decide
what funcitons are used/opened. This intial question is inside the while loop,
as a result the testing of potential minerals it will repeat until the user
inputs stop to this inital quetion. At each stage the user is given a menu that
assigns numbers to the possible descriptions of the minerals left. The user
then inputs the number that best describes their mineral or they enter ? to
skip that question.
This process is repeated for all the questions until one mineral is left or
until the user has been asked all questions. The while loop will then ask the
initial question again until the user decides to stop. This intial question
will also give the option to add a new mineral.
The logic of the program works by loading all data to a dictionary called
name_to_data. After each question non matching entries are removed and a menu
of answers for the next question is producerd by processing remaining entries.
When only one entry is left in the dict or it is empty, processing stops'''
#
#

'''Extras inlcuded:
    - Ability to add new minerals to both the large data set and to a new file.
    - Error checking for all user inputs and giving a reasonable and useful
    response to their entry.
    - Code formatting with functions and structured software layout throughout,
   using other files facilitating neat and clear code, using import function.
    - Menu drop down feature of possible classifications of current minerals
    left.
    - Reusable and generic functions to reduce code complexity and ease of
    testing.
    - At each level all the possible minerals that the stage has limited are
    shown.
    - Questions are asked that take away as many minerals as possible after
    each stage.
    - Options to skip a question if the user is unsure and when the user makes
    a mistake they are able to try again.
    - Extra information via links to Wikipedia.
    - Multidemensional dictionary functions. '''
#
#
#
''' To make the code more readable and easier to debug I have split up the
initial functions onto seperate files and imported then in this file join
 them together in a short amount of code. I have imported two seperate files
 f_file is the intital code functions, c_file is where these functions are
 joined together '''

met_or_not_met = 0
count = 1

''' This clears the user outputs from any previous runs of the code and prints
instructions for the user to follow '''

outputs = open("outputs.txt", "a")
outputs.truncate(0)
outputs.close()


print()
print("************** Mineral Identification System ***************")
print()
print("Instructions:\n"
      "1. Please follow each question's instructions as they appear.\n\n"
      "2. At any point if you are unsure of the question or you are unsure "
      "what the correct answer is, please enter '?' to skip that question.\n\n"
      "3. The mineral data base used to check for your mineral is limited to a"
      " certain amount of minerals. Therefore, if at any point you are not"
      " seeing an option that describes your mineral, you will be given the"
      " option to enter your mineral into the data set or into a separate file"
      " so the mineral can be checked.")
print(" ")
print(" ")

''' Here is the main body of the code where a while loop is used incasing all
the question from the other two functions files. The loop will end once the
user inputs stop to the first path deciding question of luster type or to
enter a new mineral. Once the loop is broken it will print a summary message of
all the minerals the user has found.'''

while met_or_not_met != "Stop":
    print()
    print("==================================================================")
    print()
    print("************** Start  a new mineral classification ***************")
    print()
    print()
    user_hardness = 0
    user_streak = 0
    name_to_data, which_table, met_or_not_met = f_file.start_and_luster_type()
    # which table returned which dictates what table function is opened
    if which_table == 1:
        c_file.t_1(name_to_data)
    elif which_table == 2:
        c_file.t_2(name_to_data)
    elif which_table == "Yes":
        count = f_file.new_mineral(count)
f_file.summary_message()
