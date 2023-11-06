# TODO: Fill this in

from teststudent import add_course, drop_course, list_courses, display_course_info
from testbilling import display_bill

def show_menu():
        print('Action Menu')
        print('-----------')
        print('1: Add course')
        print('2: Drop course')
        print('3: List courses')
        print('4: Show bill')
        print('5: View course info')
        print('0: Logout')


def main():
    student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444'),
                    ('1005', '555'), ('1006', '666')]

    student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False,
                        '1005': False,
                        '1006': True}

    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5,
                    'CSC104': 3, 'CSC105': 2}

    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': [],
                     'CSC105': ['1005', '1002']}

    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1,
                       'CSC104': 3, 'CSC105': 4}

    course_info = {'CSC101': ['Computing Concepts', 'Louis Reed', 'lreed@my.waketech.test.edu'],
                   'CSC102': ['Introduction to Computing', 'Donna Summer', 'dsummer@my.waketech.test.edu'],
                   'CSC103': ['Mathematical Foundations of Computing', 'Jonathan Lennon', 'jlennon@my.wakech.edu'],
                   'CSC104': ['Computer Applications I', 'James Hendricks', 'jhendricks@my.waketech.edu'],
                   'CSC105': ['Computer Applications II', 'Neil Young', 'nyoung@my.waketech.edu']}

    login_determine = 1

    while login_determine != 0:
        userID = input('Enter ID to log in, or 0 to quit: ')
        if int(userID) == 0:
            login_determine = 0
            user_option = 0
            break
        else:
            user_option = 1

        identity_confirmation = login(userID, student_list)
        if identity_confirmation == True:
            user_option = 1
        else:
            print(f'ID or PIN incorrect')
            print()
            user_option = 0

        while user_option != 0:
            show_menu()

            user_input = int(input('What do you want to do? '))
            if user_input not in range(0, 6):
                print('Not a valid option.')
            else:
                user_option = 0
            print()

            if user_input == 1:
                add_course(userID, course_roster, course_max_size)
                user_option = 1
            elif user_input == 2:
                drop_course(userID, course_roster)
                user_option = 1
            elif user_input == 3:
                list_courses(userID, course_roster)
                user_option = 1
            elif user_input == 4:
                display_bill(userID, student_in_state, course_roster, course_hours)
                user_option = 1
            elif user_input == 5:
                display_course_info(userID, course_roster, course_hours, course_info, course_max_size)
                user_option = 1
            elif user_input == 0:
                print('Session ended.')
                print()
                user_option = 0
                login_determine = 1
            else:
                pass
def login(id, s_list):
    userPin = input('Enter PIN: ')
    for user in s_list:
        if user[0] == id:
            if user[1] == userPin:
                print('ID and PIN verified')
                print()
                return True

main()


