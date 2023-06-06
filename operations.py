import os

# it calculates and rewrites the quantity in data file
def subtraction_of_quantity(items_list,option,quantity):
    n=(" "+str(int(items_list[option-1][3])-quantity))
    items_list[option-1][3]=n 
    file=open("data.txt","w")
    for i in range (len(items_list)):
        for j in range (len(items_list[i])):
            if j == (len(items_list[i])-1):
                file.write(items_list[i][j])
            else:
                line=items_list[i][j]+","
                file.write(line)
        file.write("\n")
    file.close


# it calculates and rewrites the quantity in data file
def addition_of_quantity(items_list,option,quantity):
    n=(" "+str(int(items_list[option-1][3])+quantity))
    items_list[option-1][3]=n 
    file=open("data.txt","w")
    for i in range (len(items_list)):
        for j in range (len(items_list[i])):
            if j == (len(items_list[i])-1):
                file.write(items_list[i][j])
            else:
                line=items_list[i][j]+","
                file.write(line)
        file.write("\n")
    file.close

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')
    
   
 