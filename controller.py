import view as v
import model as m

def main():
    while True:
        action = v.main_menu()
        match (action):
            case "1":
                employees = m.show_all_employees()
                v.menu_show_all_employees(employees)
            case "2":
                employee_list = v.menu_create_employee()
                m.create_employee(employee_list)
            case "3":
                surname = v.menu_find_employees()
                found_employees = m.find_employees(surname)
                v.output_of_found_employees(found_employees)
            case "4":
                employees = m.show_all_employees()
                employee_id = v.menu_delete_employee(employees)
                m.delete_employee(employee_id)
            case "5":
                m.import_json()
            case "6":
                m.export_json()
            case "q":
                break

