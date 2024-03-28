itineraries = [
    ("Jimmy", "Tampa", "Huntsville"),
    ("Rachel", "Las Vegas", "Houston")
]

def format(itineraries):
    index = 1
    for name, origin, destination in itineraries:
        print("Itinerary " + str(index) + ": " + name + " - From " + origin + " to " + destination)
        index += 1

format(itineraries)