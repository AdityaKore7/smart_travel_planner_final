"""File handling: all trips are saved in trips.json (next to main.py)."""

import json
import os

from .models import Trip

project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(project_folder, "trips.json")


def load_trips():
    # returns a list of Trip objects ([] if the file is missing or damaged)
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        return [Trip.from_dict(item) for item in data]
    except (json.JSONDecodeError, TypeError):
        return []


def write_all(trips):
    data = [trip.to_dict() for trip in trips]
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def save_trip(trip):
    trips = load_trips()
    trips.append(trip)
    write_all(trips)


def delete_trip(index):
    trips = load_trips()
    if 0 <= index < len(trips):
        trips.pop(index)
        write_all(trips)
