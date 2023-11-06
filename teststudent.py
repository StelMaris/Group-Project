# TODO: Fill this in

def add_course (id, c_roster, c_max_size):
    currCourse = input('Enter course you want to add: ')
    if currCourse not in c_roster:
        print('Course not found')
    elif id in c_roster[currCourse]:
        print('You are already enrolled in that course.')
    elif len(c_roster[currCourse]) == c_max_size[currCourse]:
        print('Course already full.')
    else:
        c_roster[currCourse].append(id)
        print('Course added')

    print()

def drop_course (id, c_roster):
    currCourse = input('Enter course you want to drop: ')
    if currCourse not in c_roster:
        print('Course not found')
    elif id not in c_roster[currCourse]:
        print('You are not enrolled in that course.')
    else:
        c_roster[currCourse].remove(id)
        print('Course dropped')

    print()

def list_courses (id, c_roster):
    print('Courses:')
    classes_count = 0
    for item in c_roster:
        if id in c_roster[item]:
            print(f'{item} (Enrolled)')
            classes_count += 1
        else:
            print(item)
    print(f'Total courses enrolled: {classes_count}')
    print()

def display_course_info (id, c_roster, c_hours, c_info, c_max_size):
    currCourse = input('Enter course you want to view: ')
    if currCourse not in c_roster:
        print('Course not found')
        print()
    else:
        print()
        header_length = len(currCourse) + len(c_info[currCourse][0]) + 3
        print(f'{currCourse} - {c_info[currCourse][0]}')
        print('-' * header_length)
        if id in c_roster[currCourse]:
            print(f'Status: Enrolled')
        else:
            print(f'Status: Not enrolled')
        print(f'Credit Hours: {c_hours[currCourse]}')
        if len(c_roster[currCourse]) == c_max_size[currCourse]:
            print(f'Seats: {len(c_roster[currCourse])}/{c_max_size[currCourse]} '
                  f'(Course is full)')
        else:
            if c_max_size[currCourse] - len(c_roster[currCourse]) == 1:
                print(f'Seats: {len(c_roster[currCourse])}/{c_max_size[currCourse]} '
                      f'(Course has {c_max_size[currCourse] - len(c_roster[currCourse])} seat available)')
            else:
                print(f'Seats: {len(c_roster[currCourse])}/{c_max_size[currCourse]} '
                      f'(Course has {c_max_size[currCourse] - len(c_roster[currCourse])} seats available)')
        print()
        print(f'Professor: {c_info[currCourse][1]}')
        print(f'Professor email: {c_info[currCourse][2]}')
        print()

