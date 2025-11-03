# Habit Tracker Prototype
# Tracks daily habits and progress percentage

import datetime

habits = {
    "Workout": [],
    "Read": [],
    "Sleep 8 hours": []
}

def log_habit(habit):
    today = datetime.date.today()
    if habit in habits:
        habits[habit].append(today)
        print(f"{habit} logged for {today}.")
    else:
        print("Habit not found.")

def show_progress(habit):
    today = datetime.date.today()
    past_week = [today - datetime.timedelta(days=i) for i in range(7)]
    completed = len([d for d in habits[habit] if d in past_week])
    print(f"{habit}: {completed}/7 days this week.")

# Example usage
log_habit("Workout")
show_progress("Workout")
