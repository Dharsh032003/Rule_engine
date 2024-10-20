
# Rule Engine with AST

This project implements a simple 3-tier rule engine application using Abstract Syntax Trees (AST) to represent conditional rules. It allows for dynamic creation, combination, and modification of rules to determine user eligibility based on the rules.

## Features

- Create and store rules using a simple string syntax
- Combine multiple rules into a single AST
- Evaluate user data against stored rules
- Simple web interface for rule creation and evaluation

## Software requirements

- Backend: Python 3.7+, Flask
- Frontend: HTML, JavaScript
- Database: SQLite

## Installation

1. Clone the repository:
   ```
   cd rule-engine-ast
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   venv\Scripts\activate #on Mac use: source venv/bin/activate 
   ```

3. Install the required dependencies:
   ```
   pip install flask
   ```

## Running the Application

1. Start the Flask server:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000` or `http://127.0.0.1:5000`

## Usage

1. Create a rule using the web interface. Example rule:
   ```
   (age > 30 AND department = 'Sales') AND (salary > 50000 OR experience > 5)
   ```

2. Use the evaluation form to test the rule against sample data.

3. Create multiple rules and test combinations.