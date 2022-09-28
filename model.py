import sqlite3
from sqlite3 import Error
import json

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection("employees.sqlite")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

create_employees_table = """
CREATE TABLE IF NOT EXISTS employees (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  surname TEXT NOT NULL,
  name TEXT NOT NULL,
  position TEXT NOT NULL,
  salary INTEGER
);
"""

# execute_query(connection, create_employees_table)

create_employees = """
INSERT INTO
  employees (surname, name, position, salary)
VALUES
  ('Иванов', 'Иван', 'директор', 1000),
  ('Иванова', 'Анна', 'бухгалтер', 1000),
  ('Петров', 'Петр', 'юрист', 1000),
  ('Петров', 'Сергей', 'инженер', 1000),
  ('Смирнов', 'Алексей', 'инженер', 1000);
"""

# execute_query(connection, create_employees)

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def show_all_employees():
    select_employees = "SELECT * from employees"
    employees = execute_read_query(connection, select_employees)
    return employees

def delete_employee(employee_id):
    delete_comment = f"DELETE FROM employees WHERE id = {employee_id}"
    execute_query(connection, delete_comment)
    print("Сотрудник удален из БД")

def create_employee(employee_list):
    surname, name, position, salary = employee_list
    create_employee = f"""
    INSERT INTO
      employees (surname, name, position, salary)
    VALUES
      ('{surname}', '{name}', '{position}', {salary});
    """
    execute_query(connection, create_employee)
    print("Сотрудник добавлен в БД")

def find_employees(surname):
    find_employee = f"SELECT * FROM employees WHERE employees.surname = '{surname}'"
    found_employees = execute_read_query(connection, find_employee)
    return found_employees

def import_json():
    select_employees = "SELECT * from employees"
    employees = execute_read_query(connection, select_employees)
    with open('employees.json', 'w', encoding='utf-8') as f:
        json.dump(employees, f, ensure_ascii=False)
    print("Данные успешно импортированы в JSON")

def export_json():
    with open('employees.json', 'r', encoding='utf-8') as f:
        employees = json.load(f)
    for employee in employees:
        employee_id, surname, name, position, salary = employee
        find_employee = f"""
            SELECT * FROM employees
            WHERE 
                employees.surname = '{surname}' and
                employees.name = '{name}' and
                employees.position = '{position}'
            """
        search_result = (execute_read_query(connection, find_employee))
        if search_result == []:
            create_employee = f"""
                INSERT INTO
                  employees (surname, name, position, salary)
                VALUES
                  ('{surname}', '{name}', '{position}', {salary});
                """
            execute_query(connection, create_employee)
            print(f"{surname} {name} {position} добавлен(а) в БД")
        else:
            print(f"{surname} {name} ({position}) уже существует в БД")
    return employees

