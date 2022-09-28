def main_menu():
    action = input("\nГлавное меню\n"
                "Введите:\n"
                "1 - для просмотра всех сотрудников\n"
                "2 - для добавления нового сотрудника\n"
                "3 - для поиска сотрудника\n"
                "4 - для удаления сотрудника\n"
                "5 - для импорта в JSON\n"
                "6 - для экспорта из JSON\n"
                "q - для выхода\n"
                "-> ")
    return action

def menu_show_all_employees(employees):
    print("Список всех сотрудников:")
    for employee in employees:
        print(f"id сотрудника: {employee[0]}, Фамилия: {employee[1]}, Имя: {employee[2]}, "
              f"Должность: {employee[3]}, Зарплата: {employee[4]}")

def menu_delete_employee(employees):
    for employee in employees:
        print(f"id сотрудника: {employee[0]}, Фамилия: {employee[1]}, Имя: {employee[2]}, "
              f"Должность: {employee[3]}, Зарплата: {employee[4]}")
    employee_id = int(input("Введите id сотрудника -> "))
    return employee_id

def menu_create_employee():
    employee_list = []
    print("Введите данные нового сотрудника:")
    employee_list.append(input("Фамилия -> "))
    employee_list.append(input("Имя -> "))
    employee_list.append(input("Должность -> "))
    employee_list.append(int(input("Зарплата -> ")))
    return employee_list

def menu_find_employees():
    surname = input("Введите фамилию -> ")
    return surname

def output_of_found_employees(found_employees):
    if found_employees == []:
        print("Сотрудник не найден")
    for employee in found_employees:
        print(f"id сотрудника: {employee[0]}, Фамилия: {employee[1]}, Имя: {employee[2]}, "
              f"Должность: {employee[3]}, Зарплата: {employee[4]}")

