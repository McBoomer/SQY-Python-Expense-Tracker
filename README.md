# Expense Tracker App

## Demo video
demo of the program running:

https://github.com/user-attachments/assets/dea47a01-b637-48d3-a67a-0afe5fb09476

## Overview

this is a simple python user interface that takes in user data with input fields and confirms it with buttons, it has a github dark theme look

user info is saved into  a `.db` file using sql as the system. the info is then shown in a table

the same data is sorted into its category and shown as a bar graph on the right side of the ui. this way users can track spending easy with a basic tool

this project  shows knowlege in:
- python
- sql / sqllite
- ax
- matplotplib
- css
- pyqt6

## Features
- dark github style theme
- add, delete and view expenses with input fields
- saves data  in a sqlite `.db` file
- table shows all expenses
- bar graph shows spending by category
- "today" button to quick set date
- table on  the left and chart on the right

## Tech Stack
- python
- pyqt6
- sqlite (sql)
- matplotplib
- css  (qt stylesheets0

## License
This project  is open source under the [MIT License](https://opensource.org/license/mit)

## Installation

copy this  repo and install deps:

```bash
git clone https://github.com/your-username/expense-tracker-app.git
cd expense-tracker-app
pip install pyqt6 matplotlib

run it
python main.py

Usage

type  date, category, amount and description

click add expense to save it

delete  expense button to remove it

see all data in the table

bar graph  shows spending in each category

Database Schema

the app makes a  file expenses.db with this table:

CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    category TEXT,
    amount REAL,
    description TEXT
);

Project Structure
expense-tracker-app/
|
|-- app.py        # main pyqt6 ui logic
|-- database.py   # handles sql database (sqlite)
|-- main.py       # start point for the app
|-- expenses.db   # database file made when running
|-- README.md     # this file


