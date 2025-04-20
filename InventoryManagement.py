
inventory={}
def add_item(name,price,stock):
    inventory[name]={"Price":price,"Stock":stock}
def Display_items():
    if inventory:
        for name,details in inventory.items():
            print(f"Items:{name},Price:{details['Price']},Stock:{details['Stock']}") 
    else:
        print("Inventory is empty")           
def updateitem(name,stock):
    if name in inventory:
        inventory[name]['stock']+=stock
    else:
        print(f"Item {name} not found in inventory")
    
def SearchItem(name):
    if name in inventory:
        print(f"Item {name}")
        print(f"Price {inventory[name]["Price"]}")
        print(f"Stock {inventory[name]["Stock"]}")
    else:
        print(f"Item {name} not found in inventory")    


while True:
    print("\n1-->Add Items\n2--> Update Stocks\n3--> Search Items\n4--> Display Inventory\n5--> Exit")
    choice=int(input("Enter your choice: "))

    if choice==1:
        item_name=input("Enter the item name: ")
        price=float(input("Enter price: "))
        stock=int(input("Enter the stock"))
        add_item(item_name,price,stock)
    elif choice==2:
        item_name=input("Enter the item name: ")
        stock=int(input("Enter the stock to update:"))
        updateitem(item_name,stock)
    elif choice==3:
        item_name=input("Enter the item name: ")   
        SearchItem(item_name) 

    elif choice==4:
        Display_items()    
    elif choice==5:
        break 
    else:
        print("Invalid Choice")

