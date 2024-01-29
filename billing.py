# ----------------------------------------------------------------
# Author: Jacob Widdowson
# Date: 11/16/2023
#
# This module calculates and displays billing information
# for students in the class registration system.  Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------
import datetime


def display_bill(id, s_in_state, c_rosters, c_hours):
    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Determine if the student is in-state or out-of-state
    if id in s_in_state:
        student_type = "In-State Student"
        cost_per_hour = 225
    else:
        student_type = "Out-of-State Student"
        cost_per_hour = 850

    # Calculate the total cost and initialize the bill string
    total_cost = 0
    bill_string = "Tuition Summary\n"
    bill_string += f"Student: {id}, {student_type}\n"
    bill_string += f"{current_datetime.strftime('%b %d, %Y at %I:%M %p')}\n"
    bill_string += "Course    Hours    Cost   \n"
    bill_string += "------    -----  ---------\n"

    # Iterate over the class rosters and calculate the cost for each class
    for course, students in c_rosters.items():
        if id in students:
            hours = c_hours[course]
            cost = hours * cost_per_hour
            total_cost += cost
            bill_string += f"{course:<9} {hours:>5}  $ {cost:>7.2f}\n"

    bill_string += "        -------  ---------\n"
    bill_string += f"Total        {sum(c_hours.values()):>5}  $ {total_cost:>7.2f}\n"

    print(bill_string)
pass

