budget={
    "Income":{},
    "Expences":{}
}
def add_income(income_category,amount):
    if income_category in budget["Income"]:
        budget["Income"][income_category]+=amount
    else:
        budget["Income"][income_category]=amount
    print(f"Amount {amount} to {income_category} income") 

def add_expences(category,amount,description):
    if category in budget["Expences"]:
        budget["Expences"][category].append({"amount":amount,"description":description}) 
    else:
        budget["Expences"][category]=[{"amount":amount,"description":description}]  
    print(f"Added expense :{description}, amount :{amount} to {category}")
def view_summary():
    total_income=sum(budget["Income"].values())
    total_expences=sum((sum((item["amount"] for item in expenses)) for expenses in budget["Expences"].values()))
    balance=total_income-total_expences
    print("\n-----Budget Summary-------")
    print(f"Total income: ${total_income}")
    print(f"Total Expences: ${total_expences}")
    print(f"Balance: ${balance}")
    print("\n------Expense Breakdown--------")

    for category, expences in budget["Expences"].items():
        total_category_expences=sum(item['amount'] for item in expences)
        print(f"{category}: ${total_category_expences}")

    if balance < 0:
        print("\n Warning Yor are overspending")
    else:
        print("\nYou are managing your budget well")    




while True:
    print("\n1-->Add income\n2--> Add expences\n3--> View summary\n4--> Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        income_category=input("Enter income category (e.g, Salary, Freelance): ")
        amount=float(input("Enter income amount"))
        add_income(income_category,amount)
    elif choice==2:
        expences_category=input("Enter expences category (e.g., Groseries,Utilities,Entertainment ): ")    
        amount=float(input("Enter expences amount: "))
        description=input("Enter description of the exepences: ")
        add_expences(expences_category,amount,description)
    elif choice==3:
        view_summary()
    elif choice==4:
        break
    else:
        print("Invalid Input!")        