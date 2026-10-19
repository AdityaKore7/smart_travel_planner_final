# Smart Travel Planner & Budget Estimator

## Project Overview

The **Smart Travel Planner & Budget Estimator** is a Python-based desktop application that helps users plan their trips and estimate the total travel budget. It provides a simple graphical user interface (GUI) where users can enter their destination, number of days, travel expenses, hotel expenses, and food expenses.

The application calculates the total estimated budget, saves trip details in a JSON file, and displays a bar graph to compare different expenses.

## Objectives

- To develop a simple and user-friendly travel planning application using Python.
- To calculate the estimated total cost of a trip.
- To save and manage trip details using file handling.
- To visualize travel, hotel, and food expenses using a bar graph.
- To apply Python concepts such as functions, classes, exception handling, and user-defined packages.
- To demonstrate the use of Tkinter, NumPy, and Matplotlib in a practical project.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Tkinter | Creates the graphical user interface |
| NumPy | Stores expense values in an array |
| Matplotlib | Displays expense comparison graphs |
| JSON | Stores trip information |
| OS module | Handles file paths and checks file existence |
| Object-Oriented Programming | Represents trips using a `Trip` class |

## Features

- **Trip Details:** Enter the destination and number of days.
- **Budget Calculation:** Calculate the total cost of travel, hotel, and food.
- **Save Trips:** Store trip details in a JSON file for future use.
- **Load Saved Trips:** Read previously saved trip details.
- **Delete Trips:** Remove a selected trip from the saved records.
- **Expense Visualization:** Display a bar graph comparing travel, hotel, and food costs.
- **Input Error Handling:** Handle invalid numeric inputs and selected file or JSON errors.
- **Simple GUI:** Interact with the application through Tkinter widgets.

*Note: Features such as loading and deleting saved trips depend on how the storage functions are connected to the application's GUI.*

## Project Structure

```text
Smart_Travel_Planner/
│
├── main.py
├── trips.json
├── README.md
│
└── travel_package/
    ├── __init__.py
    ├── calculation.py
    ├── models.py
    └── storage.py
```

- `main.py` — Runs the application and creates the GUI.
- `trips.json` — Stores saved trip records; it may be created when trips are saved.
- `calculation.py` — Contains the budget calculation function.
- `models.py` — Defines the `Trip` class and its data conversion methods.
- `storage.py` — Loads, saves, and deletes trip records.
- `__init__.py` — Marks the folder as a traditional Python package.

## Requirements

- Python 3.10 or later recommended.
- Matplotlib
- NumPy

Tkinter is included with most standard Windows Python installations. JSON and OS are part of Python's standard library.

## How to Run the Project

### 1. Download or clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Alternatively, download the repository as a ZIP file and extract it.

### 2. Open the project folder

Open the `Smart_Travel_Planner` folder in Visual Studio Code.

### 3. Install the required libraries

Open the terminal in VS Code and run:

```bash
python -m pip install numpy matplotlib
```

### 4. Run the application

Make sure the terminal is in the project folder containing `main.py`, then execute:

```bash
python main.py
```

### 5. Use the application

1. Enter the destination.
2. Enter the number of days.
3. Enter the travel cost.
4. Enter the hotel cost.
5. Enter the food cost.
6. Click **Calculate Budget** to view the total estimated cost.
7. Click **Save Trip** to save the trip details.
8. Click **Show Graph** to view the expense comparison.

## Example

**Input:**

| Expense | Amount |
|---|---:|
| Destination | Goa |
| Number of days | 3 |
| Travel cost | ₹4,000 |
| Hotel cost | ₹6,000 |
| Food cost | ₹3,000 |

**Output:**

```text
Destination: Goa
Days: 3
Total Budget: ₹13000
```

The application can also display a bar graph comparing the three expense categories.

## Python Concepts Demonstrated

- Data types and operators
- User-defined functions
- Object-Oriented Programming
- Lists and list comprehensions
- File handling
- Exception handling
- User-defined packages
- NumPy arrays
- Matplotlib graphs
- Tkinter GUI and layout managers
- JSON data storage

## Future Enhancements

- Add a dropdown list of popular destinations.
- Display all saved trips in the GUI.
- Add editing and filtering of saved trips.
- Calculate per-person and per-day budgets.
- Export trip summaries to CSV or PDF.

## Author

**Aditya Kore**

Computer Science and Engineering

## License

This project is intended for educational purposes. You may add an appropriate open-source license if you want others to reuse or modify the code.
