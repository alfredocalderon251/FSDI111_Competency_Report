from datetime import datetime
import pickle
import os

from Item import Item

logs_list=[]
Items_list=[]
items_file="items.data"
id_count=1
logs_file="logs.data"


def register_item():
    global id_count

    title=input("Please Type Title ")
    category=input("Please Type Category ")
    price=float(input("Please Type Price "))
    stock=int(input("Please Type Stock "))

    NewItem=Item(id_count,title,category,price,stock)

    Items_list.append(NewItem)

    log_line=get_time()+" | Register | "+str(NewItem.id)+ " "+NewItem.title    
    save_log(log_line)

    id_count+=1
    print("Item Created")


def display_Items():

    print (" ")
    print(10*'*'+ " Items List "+ '*'*10 )
    print("ID          |Title                    |Category                    |Price          |Stock")

    for itm in Items_list:
        display_Item(itm)

        
    print("Total Items: "+str(len(Items_list)))
    print (" ")




def display_Item(itm):
    print(str(itm.id).ljust(13)+itm.title.ljust(26)+itm.category.ljust(29)+str(itm.price).ljust(16)+str(itm.stock).ljust(5))


def update_stock():
    display_Items()
    itemID=input("Type the ID of the Item you want to Update ")
    found=False

    for item in Items_list:
        if(str(item.id)==itemID):
            quantity_update=input("Type New Stock Quantity ")

            item.stock=quantity_update
            found=True
            log_line=get_time()+" | Update Stock | "+str(item.id)+ " "+item.title            
            save_log(log_line)

            print("Stock Updated!! ")
    
    if(found==False):
        print("No Item was Found")


def list_empty_stock():

    founditem=False

    for item in Items_list:
        if(item.stock==0):
            founditem=True
            display_Item(item)
    
    if(founditem==False):
        print("No Items Without Stock were found ")


def clear():
    return os.system("clear")

def get_time():
    now = datetime.now()
    time=now.strftime("%d/%m/%Y %H:%M:%S")
    return time

def save_items():
    writer=open(items_file,"wb")
    print("saving "+str(len(Items_list) )+"Items ")
    pickle.dump(Items_list,writer)
    writer.close()

    print("Data File saved!")

def save_log(log_line):
    logs_list.append(log_line)

    writer=open(logs_file,"wb")
    pickle.dump(logs_list,writer)
    writer.close()
    print("Log was saved")


def read_items():
    global id_count
    lastest_id=0

    try:
        reader=open(items_file,"rb")
        temp_list=pickle.load(reader)

        for item in temp_list:
            Items_list.append(item)

            last=item.id
            if(last>=lastest_id):
                id_count=last+1
            
        print("loaded: "+str(len(temp_list))+" items")
    except:
        print("Error: Data items could not be loaded!")


def read_log():
    try:
        reader=open(logs_file,"rb")
        temp_list=pickle.load(reader)
        for log in temp_list:
            logs_list.append(log)

        print("Loaded: "+str(len(temp_list))+"log events")
    except:
        print("Error: Data log could not be loaded!")


def Remove_Item():
    display_Items()
    ItemID= input("Which ID Item you want to remove? ")

    for Item in Items_list:
       if(ItemID==str(Item.id)):
           Items_list.remove(Item)
           print("Item id: "+ItemID +" was Removed!! ")
           log_line=get_time()+" | Removed | "+ItemID+" "+Item.title           
           save_log(log_line)
           save_items()
           break
        
    
    

def print_categories():
    temp_list=[]

    for item in Items_list:
        if(item.category not in temp_list):
            temp_list.append(item.category)
    

    for item in temp_list:
        print(item)
        


def register_purchase():
    display_Items()

    itemID=input("Select an ID to purchase")

    found=False

    for Item in Items_list:
        if(str(Item.id)==itemID):
            stock=input("How Many you want purchase? ")
            Item.stock+=int(stock)
            
            found=True

            log_line=get_time()+" | Purchase | "+str(Item.id)+" "+stock         
            save_log(log_line)

            save_items()

    if(not found):
        print("Item was not found")

def register_sell():

    display_Items()
    itemID=input("Select an ID to Sell")

    found=False

    for Item in Items_list:
        if(str(Item.id)==itemID):
            stock=input("How Many you want to sell? ")
            Item.stock=  Item.stock-int(stock)
            found=True

            log_line=get_time()+" | Sell | "+str(Item.id)+" "+stock         
            save_log(log_line)

            save_items()

    if(not found):
        print("Item was not found")

def print_stock_value():
    total=0.0

    for item in Items_list:
        total+=(item.price*float(item.stock))
    
    print("Total Stock Value: "+str(total))


def display_log():

    print(10*'*' +"Logs"+(10*'*'))
    for item in logs_list:
        print(item)
    
    print(" ")



    


    


# def register_item():
#     global id_count
def menu():
    clear()
    print("Welcome to Warehouse,  Menu")
    print ("[1] - Add Item")
    print ("[2] - Update Stock")  
    print ("[3] - Display All Items")  
    print ("[4] - Display Items Without Stock") 
    print ("[5] - Remove")    
    print ("[6] - See Event Log")
    print ("[7] - Purchase")
    print ("[8] - Sell")
    print ("[9] - See Total Stock Value")
    print ("[10] - See All Categories")
    print ("[x] - Exit")


read_items()
read_log()
# read_log()
#menu()

opc=""
while(opc!="x"):
    menu()
    opc= input("Select an option ")
    if(opc=="x"):
        break    

    if(opc=="1"):
        register_item()
        save_items()
    
    if(opc=="2"):
        update_stock()
        save_items()


    if(opc=="3"):
        display_Items()

    if(opc=="4"):
        list_empty_stock()
    
    if(opc=="5"):
        Remove_Item()
    
    if(opc=="6"):
        display_log()

    if(opc=="7"):
        register_purchase()

    if(opc=="8"):
        register_sell()

    if(opc=="9"):
        print_stock_value()
    
    if(opc=="10"):
        print_categories()
    
    input("Press Enter to go back")





    



    


