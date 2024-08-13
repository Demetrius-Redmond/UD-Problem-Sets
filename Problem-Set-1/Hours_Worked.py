
week_count = 0
hours_per_week = 0
number_of_weeks = int(input("Number of weeks to track: "))


for week in range(number_of_weeks):
    hours_per_week += int(input(f"Week {week_count} HW Hours: "))
    week_count +=1

total_or_average = input("Enter T for total hour, A for average hours per week: ")
if total_or_average == "T":
    print(hours_per_week)
if total_or_average == "A":
    print(round(hours_per_week / number_of_weeks, 2))

# wrote the code pretty quick and was stuck for about 30m or more because code kept crashing because I forgot to put wrap the total average strip in the input method...