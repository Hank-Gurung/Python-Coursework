from operations import subtraction_of_quantity,clean
from read import items_list
from read import table
from read import show_items
from read import showing_bill
import datetime
from write import first_part_of_bill,middle_part_of_bill,total_with_ship_cost

# import items
def selling_customers():
    clean()
    show_items()
    table()
    items=items_list()
    while True:
        name = input("Name: ")
        if name=="":
            print("Please enter name")
            
            continue
        else:
            break
    date=datetime.date.today()
    first_part_of_bill(name,date)
    # buying()
    print("Which laptop do you want?")
    sum=0
    while True:
        print("Select from Options 1 to ",(len(items)))
        try:
            option = int(input("Option: "))
            if option >= (len(items)+1):
                print("Enter options from 1 to ",len(items))
            elif option <=0:
                print("Enter positive value")
            else:
                try:
                    quantity=int(input("How much do you want: "))
                    if quantity > int(items[option-1][3]):
                        print("It's beyond our stock")
                    elif quantity <=0:
                            print("Enter positive value")   
                    else:
                        #calculating new quantity 
                        subtraction_of_quantity(items,option,quantity)
                          
                        qsn=input("Do you want to buy more? yes/no : ")
                        rs = items[option-1][2]
                        rss = rs.split("$")
                        price = int(rss[1])*quantity
                        middle_part_of_bill(name,option,quantity,price)
                        sum = sum + price
                        
                        
                        if qsn=="yes":
                            continue
                        elif qsn=="no":
                            
                            ship=input("enter shipping cost: ")
                            if str(ship) =="":
                                ship = 0
                                
                            else:
                                ship=int(ship)
                            total_with_ship_cost(name,sum,ship)
                            clean()
                            showing_bill(name) 
                            e=input("Press enter to continue")
                            if e =="":
                                break
                            else:
                                break
                        else:
                            print("Enter yes or no")
                            
                except:
                    print("Enter correct option")

        except:
            print("Enter correct option")