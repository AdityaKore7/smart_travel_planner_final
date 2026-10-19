"""
Smart Travel Planner - Semester V Python Project

    Tab 1 - Plan Trip   : enter trip costs and calculate the total budget
    Tab 2 - Saved Trips : see, search and delete saved trips
    Tab 3 - Statistics  : average, cheapest and costliest trip
"""

import tkinter as tk
from tkinter import ttk, messagebox

from travel_package import Trip, load_trips, save_trip, delete_trip, summarize

current_trip = None     # the trip made by the last click on "Calculate"


# ---------------------------------------------------------------
#  Plan Trip tab
# ---------------------------------------------------------------
def calculate():
    """Calculate button: read the boxes and show the budget."""
    global current_trip

    try:
        destination = destination_entry.get().strip()
        if destination == "":
            raise ValueError

        days = int(days_entry.get())
        travellers = int(travellers_entry.get())
        travel = float(travel_entry.get())
        hotel = float(hotel_entry.get())
        food = float(food_entry.get())

        misc_text = misc_entry.get().strip()
        if misc_text == "":         # miscellaneous is optional
            misc_text = "0"
        misc = float(misc_text)

        limit_text = limit_entry.get().strip()
        if limit_text == "":        # budget limit is optional
            limit = None
        else:
            limit = float(limit_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid values")
        return

    current_trip = Trip(destination, days, travellers, travel, hotel, food,
                        misc, limit)

    status = current_trip.status()
    colour = "black"
    if "Over budget" in status:
        colour = "red"

    result_label.config(fg=colour, text=(
        f"Destination : {current_trip.destination}\n"
        f"Days        : {current_trip.days}\n"
        f"Travellers  : {current_trip.travellers}\n"
        f"Total       : Rs. {current_trip.total():,.2f}\n"
        f"Per day     : Rs. {current_trip.per_day():,.2f}\n"
        f"Per person  : Rs. {current_trip.per_person():,.2f}\n"
        f"Status      : {status}"))


def save():
    """Save Trip button: store the trip in trips.json."""
    if current_trip is None:
        messagebox.showwarning("No Data", "Calculate the budget first.")
        return

    save_trip(current_trip)
    messagebox.showinfo("Success", "Trip saved!")


def clear():
    """Clear button: empty all boxes."""
    global current_trip

    for box in all_entries:
        box.delete(0, tk.END)

    current_trip = None
    result_label.config(text="Enter trip details and click Calculate", fg="black")


# ---------------------------------------------------------------
#  Saved Trips tab
# ---------------------------------------------------------------
def show_saved(*args):
    """Fill the table with the saved trips that match the search text."""
    for row in table.get_children():
        table.delete(row)

    keyword = search_var.get().strip().lower()
    trips = load_trips()

    for position in range(len(trips)):
        trip = trips[position]
        if keyword in trip.destination.lower():
            # row id = position of the trip in the file (used for delete)
            table.insert("", "end", iid=str(position), values=(
                trip.destination, trip.days, trip.travellers,
                f"{trip.total():,.2f}", trip.created))


def delete_selected():
    """Delete Selected button: remove the chosen trip."""
    selected = table.selection()

    if not selected:
        messagebox.showwarning("No Selection", "Select a trip to delete.")
        return

    delete_trip(int(selected[0]))
    show_saved()


# ---------------------------------------------------------------
#  Statistics tab
# ---------------------------------------------------------------
def show_stats():
    """Show count, average, cheapest and costliest trip."""
    trips = load_trips()

    if len(trips) == 0:
        stats_label.config(text="No saved trips yet.")
        return

    totals = []
    for trip in trips:
        totals.append(trip.total())

    stats = summarize(totals)       # NumPy

    cheapest = trips[0]
    costliest = trips[0]
    for trip in trips:
        if trip.total() < cheapest.total():
            cheapest = trip
        if trip.total() > costliest.total():
            costliest = trip

    stats_label.config(text=(
        f"Trips saved       : {stats['count']}\n"
        f"Average trip cost : Rs. {stats['average']:,.2f}\n"
        f"Cheapest trip     : {cheapest.destination} (Rs. {stats['minimum']:,.2f})\n"
        f"Costliest trip    : {costliest.destination} (Rs. {stats['maximum']:,.2f})"))


def tab_changed(event):
    """Refresh the data when the user opens a tab."""
    tab_name = tabs.tab(tabs.select(), "text")

    if tab_name == "Saved Trips":
        show_saved()
    elif tab_name == "Statistics":
        show_stats()


# ---------------------------------------------------------------
#  Window
# ---------------------------------------------------------------
root = tk.Tk()
root.title("Smart Travel Planner")
root.geometry("700x650")

tk.Label(root, text="SMART TRAVEL PLANNER",
         font=("Arial", 18, "bold")).pack(pady=10)

tabs = ttk.Notebook(root)
tabs.pack(fill="both", expand=True, padx=10, pady=5)

plan_tab = tk.Frame(tabs)
saved_tab = tk.Frame(tabs)
stats_tab = tk.Frame(tabs)

tabs.add(plan_tab, text="Plan Trip")
tabs.add(saved_tab, text="Saved Trips")
tabs.add(stats_tab, text="Statistics")
tabs.bind("<<NotebookTabChanged>>", tab_changed)


# ---- Plan Trip tab screen ----
form = tk.Frame(plan_tab)
form.pack(pady=10)

labels = ["Destination", "Days", "Travellers", "Travel Cost (Rs.)",
          "Hotel Cost (Rs.)", "Food Cost (Rs.)", "Miscellaneous (Rs.)",
          "Budget Limit (optional)"]
all_entries = []

for row in range(len(labels)):
    tk.Label(form, text=labels[row], width=20, anchor="w").grid(row=row, column=0, pady=4)
    box = tk.Entry(form, width=25)
    box.grid(row=row, column=1, pady=4)
    all_entries.append(box)

destination_entry = all_entries[0]
days_entry = all_entries[1]
travellers_entry = all_entries[2]
travel_entry = all_entries[3]
hotel_entry = all_entries[4]
food_entry = all_entries[5]
misc_entry = all_entries[6]
limit_entry = all_entries[7]

buttons = tk.Frame(plan_tab)
buttons.pack(pady=8)

tk.Button(buttons, text="Calculate", width=12, command=calculate).grid(row=0, column=0, padx=4)
tk.Button(buttons, text="Save Trip", width=12, command=save).grid(row=0, column=1, padx=4)
tk.Button(buttons, text="Clear", width=12, command=clear).grid(row=0, column=2, padx=4)

result_label = tk.Label(plan_tab, text="Enter trip details and click Calculate",
                        justify="left", font=("Consolas", 11), anchor="nw")
result_label.pack(fill="both", expand=True, padx=20, pady=8)


# ---- Saved Trips tab screen ----
search_frame = tk.Frame(saved_tab)
search_frame.pack(fill="x", padx=8, pady=8)

tk.Label(search_frame, text="Search destination:").pack(side="left")

search_var = tk.StringVar()
search_var.trace_add("write", show_saved)       # runs when the text changes
tk.Entry(search_frame, textvariable=search_var, width=25).pack(side="left", padx=6)

table = ttk.Treeview(
    saved_tab, columns=("destination", "days", "people", "total", "date"),
    show="headings", height=14)

table.heading("destination", text="Destination")
table.heading("days", text="Days")
table.heading("people", text="People")
table.heading("total", text="Total (Rs.)")
table.heading("date", text="Saved On")

table.column("days", width=60, anchor="center")
table.column("people", width=60, anchor="center")
table.pack(fill="both", expand=True, padx=8, pady=8)

tk.Button(saved_tab, text="Delete Selected", command=delete_selected).pack(pady=5)


# ---- Statistics tab screen ----
stats_label = tk.Label(stats_tab, justify="left", font=("Consolas", 11), anchor="nw")
stats_label.pack(padx=20, pady=20, anchor="w")


root.mainloop()
