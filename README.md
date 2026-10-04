# Expense Analyzer

A simple Python project that analyzes personal expense data using Pandas.

I built this project to practice working with real-world style data and to get more comfortable with Python, Pandas, CSV files, and basic data analysis.

## What it does

The project reads expense data from a CSV file and calculates:

* Total expenditure
* Highest expense
* Lowest expense
* Average expense
* Category-wise spending
* More analysis will be added as I build the project

## Technologies

* Python
* Pandas
* CSV

## Project Structure

```text
expense_analyzer/
├── expense.py
├── main.py
└── README.md
```

## Example Data

The expense data contains information such as:

```text
date,category,description,amount
2026-10-01,Food,Lunch,120
2026-10-01,Transport,Bus,30
2026-10-02,Food,Dinner,180
```

## Current Progress

### Day 1

* Loaded CSV data using Pandas
* Created a DataFrame
* Calculated total expenditure
* Found highest and lowest expenses
* Calculated average expense

### Next

* Analyze spending by category
* Add more useful expense analysis
* Improve the project step by step

## Why I Built This

I wanted to move from solving individual Python/Pandas problems to actually using what I've learned in a small project.

This is a beginner project, so I'm building it step by step and adding features as I learn.

## How to Run

Clone the repository, install Pandas, and run:

```bash
python main.py
```
