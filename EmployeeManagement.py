def add_employee(employee_dict,id,name,department):
    if id not in employee_dict:
        employee_dict[id]={"Name":name,"Department":department}
        print("Employee added successfully")
    else:
         print("Employee id already exists")   
def list_employee(employee_dict):
    print("Employee Records")
    if not employee_dict:
        print("No employees to display")
    for emp_id , details in employee_dict.items():
        print(f"ID:{emp_id},Name:{details["Name"]},Departments:{details["Department"]}")
def remove_employee(employee_dict,id):
    if id in employee_dict:
        del employee_dict[id]
        print("Employee removed successfully")
    else:
        print("Employee id is not found")

def update_emp(employee_dict,id,name,departemnt):
    if id in employee_dict:
        if name:
            employee_dict[id]["Name"]=name
            
        if departemnt:
            employee_dict[id]["Departments"]=departemnt

        print("Employee updated successfully...........")
    else:
        print("Employee id not found........")                    

if __name__=="__main__":
    employess={}
    
    while True:
        print("\n###########Employee Management System ###########")
        print("Press 1 to add an employee")
        print("Press 2 to remove an employee")
        print("Press 3 to update an employee")
        print("Press 4 to list")
        print("Press 5 to exit")

        choice=int(input("Enter your choice (1,2,3,4,5)"))

        if choice==1:
            id=int(input("Enter the employee id "))
            name=input("Enter the name ")
            department=input("Enter the department")
            print(id,name,department)
            add_employee(employess,id,name,department) 
        elif choice==2:
            id=int(input("Enter the employee id"))
            remove_employee(employess,id)
        elif choice==3:
            id=int(input("Enter the employee id if blank")) 
            name=input("Enter the name if blank")
            department=input("Enter the department if blank") 
            update_emp(employess,id,name if name else None,department if department else None)    
        elif choice==4:
            list_employee(employess)
        elif choice==5:
            print("Exiting the system...............")
            break        
        else:
            print("Please enter correct choice")     
    # print(employess)
    # print(type(employess))
    # for key, values in employess.items():
    #     print(f"{key}:{values}")    