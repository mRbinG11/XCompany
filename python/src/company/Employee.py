from typing import List
from src.company import Gender


class Employee:
    def __init__(self,name: str , gender: Gender) -> None:
        self._name = name
        self._gender = gender
        self._manager = None
        self._direct_reports = []

    def get_name(self) -> str:
        return self._name

    def get_gender(self) -> str:
        return self._gender

    # TODO: CRIO_TASK_MODULE_XCOMPANY
    # Please define all the methods required here as mentioned in the XCompany BuildOut Milestone before implementing the logic.
    # This will ensure that the project can be compiled successfully.

    # Method 1: assign_manager
    def assign_manager(self, employee) -> None:
        self._manager = employee

    # Method 2: get_direct_reports
    def get_direct_reports(self) -> List:
        return self._direct_reports

    # Method 3: get_team_mates
    def get_team_mates(self) -> List:
        man = self._manager
        dr_list = man.get_direct_reports()
        result = [man]
        result.extend(dr_list)
        return result

    def __repr__(self) -> str:
        return f'Employee [name={self._name}, gender={self._gender.value}]'





    

