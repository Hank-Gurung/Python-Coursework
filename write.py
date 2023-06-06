from read import items_list
# all the function in this file is used in the creation of bill


# this function write the first part of bill with name and date
def first_part_of_bill(name,date):
    text="""                                                   Bill
---------------------------------------------------------------------------------------------------------------------------------------------- 
Name:{}. 

Date:{}.
----------------------------------------------------------------------------------------------------------------------------------------------
||{:<4}||{:<24}||{:<24}||{:<24}||   
--------------------------------------------------------------------------------------           
""".format(name,date,"SN","Name","Quantity","Price")

    customer="{0}'s bill.txt".format(name)
    file= open(customer,"a")
    file.write(text)

# this function writes the middle part of bill 
def middle_part_of_bill(name,b,c,price):
    customer="{0}'s bill.txt".format(name)
    sn=items_list()
    file=open(customer,"r")
    i=(len(file.readlines())-7)
    file.close
    Laptop_name = sn[b-1][0]
    text="||{:<4}||{:<24}||{:<24}||{:<24}||\n".format(i,Laptop_name,c,"$"+str(price))
    file=open(customer,"a")
    file.write(text)
    file.close

# this function write the last part of bill after the purchase of laptops with 13% VAT
def total_with_vat(name,sum):
    customer="{0}'s bill.txt".format(name)
    vat=0.13*sum
    tot=sum+vat
    text="--------------------------------------------------------------------------------------\n"               
    text1="||{:>56}||{:>24}||\n".format("Net Amount","$"+str(sum))
    text2="||{:>56}||{:>24}||\n".format("Vat amount","$"+str(vat))
    text4="||{:>56}||{:>24}||\n".format("Gross Amount","$"+str(tot))
    file = open(customer,"a")
    file.write(text)
    file.write(text1)
    file.write(text)
    file.write(text2)
    file.write(text)
    file.write(text4)
    file.write(text)
    file.close
 
# this function write the last part of bill after the selling of laptops with shipping cost  
def total_with_ship_cost(name,sum,ship):
    customer="{0}'s bill.txt".format(name)
    tot=ship+sum
    text="-------------------------------------------------------------------------------------\n"               
    text1="||{:>56}||{:>24}||\n".format("Net Amount","$"+str(sum))
    text3="||{:>56}||{:>24}||\n".format("Ship Amount","$"+str(ship))
    text4="||{:>56}||{:>24}||\n".format("Gross Amount","$"+str(tot))
    file = open(customer,"a")
    file.write(text)
    file.write(text1)
    file.write(text)
    file.write(text3)
    file.write(text)
    file.write(text4)
    file.write(text)
    file.close


    


