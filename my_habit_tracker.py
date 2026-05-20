import json
import os
from datetime import date

print("Welcome to my Habit Tracker")
my_habits = ["Read Scipture", "Exercise", "Drink Water", "Journal", "Tidy Room"]
print("Here are my habits")
for habit in my_habits:
    print("-" + habit)
print("")
print("Which habits did I complete today?")
done_today = []
for habit in my_habits:
    answer = input(habit + "- did I do this today? (yes/no)")
    if answer == "yes":
        done_today.append(habit)

print("")
print("Today I completed:")
for habit in done_today:
    print("-" + habit)

today = str(date.today())

log = {}
if os.path.exists("habit_log.json"):
    with open("habit_log.json", "r") as f:
        log = json.load(f)
log[today] = done_today
with open("habit_log.json", "w") as f:
    json.dump(log, f, indent=2)

print("")
print("My log for today has been saved!")
print("")
print("my habit history:")
for day, habits in log.items():
    print(day + ":")
    for habit in habits:
        print("-" + habit)
print("")
print("My current streaks:")

for habit in my_habits:
    streak = 0
    check = date.today()
    while True:
        day_string = str(check)
        if day_string in log and habit in log[day_string]:
            streak += 1
            check = check - __import__("datetime").timedelta(days=1)
        else:
            break
    print(habit + " — " + str(streak) + " day(s) in a row")
