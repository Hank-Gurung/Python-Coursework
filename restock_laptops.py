from operations import addition_of_quantity,clean
from read import items_list
from read import table
from read import show_items,showing_bill
from write import first_part_of_bill,middle_part_of_bill,total_with_vat
import datetime

def purchase():
    clean()
    show_items()
    table()
    items=items_list()
    date=datetime.date.today()
    while True:
        name= input("Enter distributor Name:")
        if name == "":
            print("Please enter name")
            continue
        else:
            break
    
    first_part_of_bill(name,date)
    
    print("Which Laptop do you want to restock")
    sum=0
    while True:
        print("Select from Options 1 to ",(len(items)))
        try:
            option=int(input("Option:"))
            if option>=(len(items)+1):
                print("Enter options from 1 to ",len(items))
            elif option <=0:
                print("Enter positive value")
            else:
                try:
                    quantity=int(input("How much do you want to:"))
                    if quantity <=0:
                        print("Enter positive value.")
                    else:
                        addition_of_quantity(items,option,quantity)
                        qsn= input("Do you want to add more? yes/no:")
                        rs = items[option-1][2]
                        rss = rs.split("$")
                        price = int(rss[1])*quantity
                        middle_part_of_bill(name,option,quantity,price)
                        sum = sum + price
                        
                        if qsn=="yes":
                            continue
                        elif qsn=="no":
                            total_with_vat(name,sum)
                            clean()
                            showing_bill(name)
                            e=input("Press enter to continue")
                            if e =="":
                                break
                            else:
                                break
                        else:
                            print("Enter yes or no ")
                except:
                    print("Enter integers ")

        except:
            print("Enter options from 1 to ",len(items))

