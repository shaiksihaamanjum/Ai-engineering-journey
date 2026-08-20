import math
def multiplication():
    num=int(input("enter a number"))
    for i in range(1,11):
       print(f"{num} * {i} = {num*i}")

def number_guessing_game():
    num1=int(input())
    while(num1!=25):
        num1=int(input())
        
    print("gotchaa!!")
             
        

def find_area_perimeter():
 def circle(r):
    area_c=math.pi*(r*r)
    perimeter_c=2*math.pi*r
    return area_c,perimeter_c
 def rectangle(l,b):
    area_r=l*b 
    perimeter_r=2*(l+b)
    return area_r,perimeter_r 
 def triangle(ba,h,a,b,c):
    area_t=0.5*ba*h 
    perimeter_t=a+b+c
    return area_t,perimeter_t 
 choice=input("circle/rectangle/triangle").lower()
 if(choice=='circle'):
     r=float(input("radius:"))
     print(circle(r))
 elif(choice=='rectangle'):
     l,b=map(int,input().split())
     print(rectangle(l,b))
 else:
     ba,h,a,b,c=map(int,input().split())
     print(triangle(ba,h,a,b,c))
tolist=[]
def to_do_list():
   
   def add_items():
    ni=int(input("no.of items to add"))
    for i in range(ni):
        tolist.append(input())
    print(f'list:{tolist}')    
   def add_at_index():
    nj=int(input())
    for j in range(nj):
        ele=input()
        index=int(input())
        tolist.insert(index,ele)
    print(f'list: {tolist}')            
   def remove_items():
    try:
        nk=int(input())
        for k in range(nk):
          ele=input()
          tolist.remove(ele)
          print(f"removed : {ele}")  
        print(f'updated list:{tolist}')
    except Exception as e:
        print(e)    
   def view_items():
    print(f' to do list :{tolist}') 
   choice=input("add/add at index/remove/view").lower()
   if(choice=='add'):
       add_items()
   elif(choice=='add at index'):
       add_at_index()
   elif(choice=='remove'):
       remove_items()
   else:
       view_items()          

mydict={}
def contact():

 def add_contacts():
    ni=int(input("enter no.of contacts you want to add:"))
    for i in range(ni):
        name=input("enter name:")
        number=int(input("number:"))
        address=input("address:")
        mydict[name]=[number,address]
    print(mydict)

 def update_details():
    search_name=input("enter name of contact to update:")
    if search_name in mydict:
        number,address=mydict[search_name]
        choice=input("update name/number/address:").lower()
        if(choice=='name'):
           new_name=input("new name:")
           mydict[new_name]=mydict.pop(search_name)
           print(mydict)
        elif(choice=='number'):
           new_number=int(input("new number:"))
           mydict[search_name]=[new_number,address]
           print(mydict)
        else:
           new_address=input("new address:")
           mydict[search_name]=[number,new_address]
           print(mydict)
    else:
        print("contact not found")

 def delete_contacts():
    nj=int(input("enter no.of contacts you want to delete:"))
    for j in range(nj):
        name=input("enter name of the contact you wanna delete:")
        try:
            del mydict[name]
            print(f"removed: {name}")
        except KeyError:
            print(f"{name} not found")
    print(mydict)

 def view_details():
    print(mydict)



 ch=input("add/update/delete/view: ").lower()
 if(ch=='add'):
    add_contacts()
 elif(ch=='update'):
    update_details()
 elif(ch=='delete'):
    delete_contacts()
 else:
    view_details()    
def calculator():
 def add(a,b):
    return a+b
 def subtract(a,b):
    return a-b
 def multiply(a,b):
    return a*b
 def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: division by zero"

 op=input("choose operation +/-/*/: ")
 a=float(input("enter first number: "))
 b=float(input("enter second number: "))
 if(op=='+'):
     print(f"result: {add(a,b)}")
 elif(op=='-'):
     print(f"result: {subtract(a,b)}")
 elif(op=='*'):
     print(f"result: {multiply(a,b)}")
 elif(op=='/'):
     print(f"result: {divide(a,b)}")
 else:
     print("invalid operation")     
print("MINI TOOLKIT")
choice=input("multiplication/number_guessing_game/find_area_perimeter/to_do_list/contact/calculator/exit: ").lower()
while(choice!='exit'):
 if(choice=='multiplication'):
    multiplication()
    print("---------------")
 elif(choice=='number_guessing_game'):
     number_guessing_game()
     print("---------------")
 elif(choice=='find_area_perimeter'):
      find_area_perimeter()
      print("---------------")
 elif(choice=='to_do_list'):
     to_do_list()
     print("---------------")
 elif(choice=='contact'):
      contact() 
      print("---------------")
 elif(choice=='calculator'):
      calculator()
      print("---------------")
 else:
     print("invalid choice")
 choice=input("multiplication/number_guessing_game/find_area_perimeter/to_do_list/contact/calculator/exit: ").lower()

           
 
