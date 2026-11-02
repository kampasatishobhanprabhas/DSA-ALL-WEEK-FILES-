def search_employee(emp_list, emp_id, index) :
     if index == len (emp list) :
        return False
     if emp_list [index] ==  emp_id:

         return search_employee (emp_list, emp_id, index + 1)
emp list = list (map(int, input ("Enter employee IDs: ") .split ()))
emp_id = int (input ("Enter employee ID to search: "))
if search_employee (emp_list, emp_id, 0):
      print ("Employee ID found")
else:
     print ("Employee ID not found")

return True

