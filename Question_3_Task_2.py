# Task 1

attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
]

def list_attendees():
    user_event = input("Which event would you like to check? ")
    for name, event in attendees:
        if user_event == event:
            print(f"{name} attended {event}.")

list_attendees()

# Task 2

def count_attendees():
    attendees_per_event = {}
    for name, event in attendees:
        if event not in attendees_per_event:
            attendees_per_event[event] = 1
        else:
            attendees_per_event[event] += 1
    for event, count_attendees in attendees_per_event.items():
        print(f"{count_attendees} attended {event}.")

count_attendees()