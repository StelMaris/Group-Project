# TODO: Fill this in.
from datetime import datetime

def display_bill(id, s_in_state, c_roster, c_hours):
    hours_total = 0
    cost_total = 0
    currDate = datetime.now()

    print('Tuition Summary')
    if s_in_state[id] == True:
        print(f'Student: {id}, In-State Student')
    else:
        print(f'Student: {id}, Out-of-State Student')
    print(currDate.strftime("%b %d, %Y at %I:%M %p"))
    print(f'Course    Hours    Cost')
    print(f'------    -----  ---------')

    for item in c_roster:
        if id in c_roster[item]:
            hours_total += c_hours[item]
            if s_in_state[id] == True:
                cost = 225.00 * c_hours[item]
            else:
                cost = 850.00 * c_hours[item]
            cost_total += cost

            print(f'{item:6}    '
                  f'{c_hours[item]:>5d}  '
                  f'${cost:>8.2f}'
                  )

    print('        -------  ---------')
    print(f'Total     '
          f'{hours_total:>5d}  '
          f'${cost_total:>8.2f}'
          )
    print()
