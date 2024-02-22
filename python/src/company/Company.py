from typing import List
from src.company import Employee, Gender


class Company:
    def __init__(self,company_name: str, founder: Employee) -> None:
        self._company_name = company_name
        self._founder = founder
        self._employee_book = {}
        self._employee_book[founder.get_name()] = founder

    def get_company_name(self) -> str:
        self._company_name

    # TODO: CRIO_TASK_MODULE_XCOMPANY
    # Please define all the methods required here as mentioned in the XCompany BuildOut Milestone before implementing the logic.
    # This will ensure that the project can be compiled successfully.

    # Method 1: register_employee
    def register_employee(self, employee_name: str, gender: Gender) -> None:
        emp = Employee(employee_name, gender)
        self._employee_book[employee_name] = emp

    # Method 2: get_employee
    def get_employee(self, employee_name: str) -> Employee:
        try:
            return self._employee_book[employee_name]
        except:
            return None

    # Method 3: delete_employee
    def delete_employee(self, employee_name: str) -> None:
        self._employee_book.pop(employee_name)

    # Method 4: assign_manager
    def assign_manager(self, employee_name: str, manager_name: str) -> None:
        emp = self._employee_book[employee_name]
        man = self._employee_book[manager_name]
        man._direct_reports.append(emp)
        emp.assign_manager(man)

    # Method 5: get_direct_reports
    def get_direct_reports(self, manager_name: str) -> List[Employee]:
        man = self._employee_book[manager_name]
        return man.get_direct_reports()

    # Method 6: get_team_mates
    def get_team_mates(self, employee_name: str) -> List[Employee]:
        emp = self._employee_book[employee_name]
        return emp.get_team_mates()

    # Method 7: get_employee_hierarchy
    def get_employee_hierarchy(self, manager_name: str) -> List[List[Employee]]:
        man = self._employee_book[manager_name]
        dr_list = man.get_direct_reports()
        result = [[man]]
        if dr_list != []:
            result.append(dr_list)
        for ele in dr_list:
            temp = ele.get_direct_reports()
            if temp != []:
                result.append(temp)
        return result



    




    

    