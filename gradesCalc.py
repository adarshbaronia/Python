print("Welcome to the Average Calculator App")
print()
name = input("Enter your name: ").strip().title()
grade = int(input("How many grades would you like to enter: "))
print()
grades = []
for i in range(grade):
    num = int(input("Enter your grade: "))
    grades.append(num)

print()
print("Grades Highest to lowest: ")
grades.sort(reverse=True)
for g in grades:
    print("\t" + str(g))

print()
print(f"{name}'s Grades Summary: ")
print(f"\t\tTotal Number of grades: {grade}")
print(f"\t\tHighest Grade: {max(grades)}")
print(f"\t\tLowest grade: {min(grades)}")
old_average = sum(grades) / len(grades)
print(f"\t\tAverage: {str(old_average)}")
print()
desired_avg = float(input("What is your desired average: "))
grade_req = desired_avg*(len(grades)+1) - sum(grades)
grade_req = round(grade_req, 2)
print()


if grade_req > 100:
    print(f"Sorry {name}! This can not be possible!")
else:
    print(f"Good luck {name}!")
    print(
        f"You will need to get a {grade_req} on your next assignment to earn the average of {desired_avg}!")

print()
print("Lets see what your average could have been if you did better/worse on an asssignment.")
new_grades = grades[:]
grade_change = int(input("What grade would you like to change: "))
new_grades.remove(grade_change)
new_grade = int(input("What grade would you like to change " + str(grade_change)+" to: " ))
new_grades.append(new_grade)
print()
new_grades.sort(reverse=True)
print("\nNew Grades Highest to Lowest: ")
for grade in new_grades:
    print("\t"+ str(grade))

print()
new_average = sum(new_grades) / len(new_grades)
new_average = round(new_average, 2)

print()
print(f"{name}'s Grades Summary: ")
print(f"\t\tTotal Number of grades: {str(len(new_grades))}")
print(f"\t\tHighest Grade: {str(max(new_grades))}")
print(f"\t\tLowest grade: {str(min(new_grades))}")
print(f"\t\tNew Average: {str(new_average)}")
print()
#print a summery of change in the aveage
print(f"Your new average would be a {str(new_average)} compared to your real average of {str(old_average)}")
average_change = new_average -  old_average
average_change = round(average_change, 2)
print()
print(f"That is a change of {average_change} points!")

print()
print("\n Too bad your original grades are stilll the same!")
for g in grades:
    print("\t" + str(g))
print()
print(f"Good luck {name}! Hope you acheieve it!") 


