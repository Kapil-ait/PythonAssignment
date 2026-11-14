from DAO.employeedao import Employeedao
class EmployeeService:
    def addemployee(self,employee):
        print("service: processing employee")
        dao = Employeedao()
        dao.saveemployee(employee)
