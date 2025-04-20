def AddMembers(memdict,id,name,Gender,Plan):
    if id not in memdict:
        memdict[id]={"Name":name,"Gender":Gender,"GymPlan":Plan}
        print(f"{id} added successfully")
    else:
        print(f"{id} is already exist")    
def RemoveMembers(memdict,id):
    if id in memdict:
        del(memdict[id])
        print(f"{id} is deleted sucessfully")

    else:
        print(f"{id} is not present")
def ShowMembers(memdict):
    
    if not memdict:
        print("There is no one in members list")
    else:
        print("Members Details")
        for key,value in memdict.items():
            print(f"ID:{key} Name:{value["Name"]} Gender:{value["Gender"]}")  
def UpdateMembers(memdict,id,name,gender):
    if id in memdict:
        if name:
            memdict[id]["Name"]=name 
        if gender:
            memdict[id]["Gender"]=gender
        print(f"Member with {id} is updated successfully")
    else:
        print("Employee id is not found")
def showMemberships(memdict):
    membership_plans = {
    "basic": {"duration": "1 month", "price": 50},
    "premium": {"duration": "3 months", "price": 120},
    "annual": {"duration": "12 months", "price": 400}
    }
    for k, v in memdict.items():  
        gym_plan = v.get("GymPlan") 
        if gym_plan in membership_plans: 
            plan_details = membership_plans[gym_plan] 
            print(f"Member {k} has plan {gym_plan} with duration {plan_details['duration']} and price {plan_details['price']}")

if __name__=="__main__":
    members={}
    while True:
        print("-------------------GYM Manangement System-----------------------")
        print(members)
        print("Select any option")
        print("1-->Add Members")
        print("2-->Remove Members")
        print("3-->Show Members")
        print("4-->Update Members")
        print("5-->Show Memberships")
        print("6-->For Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            id=int(input("Enter the id of the person : "))
            Name=str(input("Enter the name :" ))
            Gender=str(input("Select the Gender (Male-->M/Female-->F):" ))
            membership_plan=str(input("Enter your Membership plan :"))

            AddMembers(members,id,Name,Gender,membership_plan)
            
        elif choice==2:
            id=int(input("Enter the id of the person : "))
            RemoveMembers(members,id)
        elif choice==3:
            ShowMembers(members)   
        elif choice==4:
            id=int(input("Enter the id of the person : " ))
            Name=str(input("Change the name if you want :" ))
            Gender=str(input("CHange the Gender if you want (Male-->M/Female-->F):" ))
            UpdateMembers(members,id,Name if Name else None,Gender if Gender else None)
        elif choice==5:
            showMemberships(members)
            
        elif choice==6:
            break    
