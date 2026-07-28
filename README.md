# ANITA — Habit Tracker CLI

ANITA is a command-line habit-tracking application built in Python. 
It allows users to create custom habits (both binary/check-based and 
measurable), log daily progress, and view performance statistics — 
all persisted through CSV-based storage.

## Features
- Create and manage custom habits with configurable frequency and units
- Track two habit types: checkable (yes/no) and measurable (numeric goals)
- Log daily progress and calculate completion percentages automatically
- View a daily summary of habit performance

## Tech Stack
- Python
- Pandas (data handling and CSV persistence)

## Roadmap
- [ ] Refactor to an object-oriented architecture (Habit, HabitTracker classes)
- [ ] Input validation and error handling
- [ ] Migrate storage from CSV to SQLite
- [ ] Graphical interface using Tkinter
- [ ] Email notifications for daily/weekly summaries
- [ ] Integration with external APIs for enriched habit data

## About this project
ANITA started as a practice project while learning Python fundamentals, 
and is being actively developed as a long-term portfolio piece — evolving 
in versioned iterations as new concepts (OOP, databases, GUI development, 
API integration) are learned and applied.
