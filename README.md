# Employee Management Django Project
-Created by : gk-mokaya | 0797252133 | kevinmokaya001@gmail.com 
## Description
This is a Django-based Employee Management application that allows users to perform CRUD (Create, Read, Update, Delete) operations on employee records. The application provides a simple interface to manage employee details such as employee ID, name, email, and contact information.

## Features
- Create new employee records
- View a list of all employees
- Update existing employee details
- Delete employee records

## Technologies Used
- Python 3.x
- Django 5.2.4
- SQLite (default Django database)
- Crispy Forms with Bootstrap 5 for enhanced form rendering

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd emp\ mngt
   ```

3. (Optional but recommended) Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   *Note: If `requirements.txt` is not present, install Django and crispy forms manually:*
   ```
   pip install django crispy-forms crispy-bootstrap5
   ```

5. Apply migrations:
   ```
   python manage.py migrate
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the application in your browser at `http://127.0.0.1:8000/`.
- Use the interface to add new employees, view the list of employees, update employee details, or delete employees.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
