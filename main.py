from sell_laptops import selling_customers
from read import show_items,table,show_techshop,exiting
from restock_laptops import purchase
from operations import clean


def main():
    clean()
    show_techshop()
    while True:
        print("Option 1: Show available Laptops ")
        print("Option 2: Sell Laptops ")
        print("Option 3: Purchase Laptops ")
        print("Option 4: Exit ")
        try:
            n = int(input("Choose Option: "))
            if n==1:
                clean()
                show_items()
                table()
            elif n==2:
                clean() 
                selling_customers()
                clean()
                show_techshop()
                
            elif n==3:
                clean() 
                purchase()
                clean()
                show_techshop()
                
            elif n==4:
                clean()
                exiting()
                break
            else:
                print("Please Choose correct Option")

        except:
            print("Please Choose correct Option")         

main()