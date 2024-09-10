import random
from dotenv import load_dotenv
from json import *
import os
import time
load_dotenv()

key= os.getenv("MASTER_KEY")

def passgenerator():
    """ No paramertres are required.
    This function gives gives the password (mixture of symbols, numbers, characters).
    Also prefered for on time use. 
    """
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    t=True
    lis=[]
    c1,c2,c3=0,0,0
    while t==True:
        i=random.randint(1,200)
        if i%3==0 and c3!=3:
            s1=random.randint(0,8)
            lis.append(symbols[s1])
            c3+=1
        elif i%2==0 and c2!=2 :
            n1=random.randint(0,9)
            lis.append(numbers[n1])
            c2+=1
        elif i%1==0 and c1!=6 :         
            l1=random.randint(0,51)
            lis.append(letters[l1])
            c1+=1
        if c1==6 and c2==2 and c3==3 :
            t=False        
    g_pass="".join(lis)
    return g_pass

def Search():
    """ No paramertres are required.
    searches the website name from the file. This is function is only avaliable for json format.  
    """
    see = input("Enter the website name")
    
    try :
        with open("./password.json", mode="r") as json_obj:
            dic2=load(json_obj)    
            
    except FileNotFoundError as error:
             print(f" No file found {FileNotFoundError}")
    else:
        try:
            flag=0
            for i in dic2:
            
                if see==i:
                    flag=1
                    break
            if flag==0:
                raise ValueError
        except ValueError:
            print(f" Entered website {see} isn't in repository ")
        else:
           print(f"  Email : {dic2[i]["email"]} Password : {dic2[i]["password"]}")
    finally:
        print("more to do?")
def Save():
    
    """ No paramertres are required.
        This function add the Entry boxes details to file.
    """
    web_ent=input("Enter Website name :")
    user_email_ent=input("Enter Email name :")
    
    ch = input(" Do you want us to generate password!!! \n yes / or ").lower()
    
    if ch == "yes":
        pass_ent = passgenerator()
    else :
        pass_ent=input("Enter Password name :")
        
    new_dic={web_ent:
               { 
                "email":user_email_ent, "password":pass_ent
                }
            }
    
    with open("./password.json", mode="r") as json_obj:
            dic=load(json_obj)    
            dic.update(new_dic)
            
    with open("./password.json", mode="w") as j_obj:
            dump(dic, j_obj, indent=4)           
            
def  Delete():
        """this function delete the sub json block from the main Json Storage"""
        entered_key = input("Enter master key for authority:"):
        if key ==  entered_key:   
            with open("./password.json", mode="r") as json_obj:
                        dic=load(json_obj)    
                        
                        if len(dic) == 0 :
                            print("THe jspn file is empty !!! \n first add data")
                        else :
                            website = input("Enter the website name to be ")
                            for j in dic :
                                if j == website:
                                    del dic[website]
                                    with open("./password.json", mode="w") as j_j:
                                            dump(dic, j_j, indent=4)
                                    print(f" website : {website} deleted")        
        else :
            print("Your are not a authorize person!!!")
            
                                    
def Display():
    """this function is for displaying all the content of json file format with master key """
    entered_key = input("Enter the mater key:")
    if key == entered_key:
        with open("./password.json", mode="r") as jjk:
                dic = load(jjk)
                print(dic)  
    else :
        print("incorrect master key !!!")                                  
                
work = input("Do you want to work with password manager: \n Enter True or False:").capitalize()
while(work):
    print(" Enter 1 to Display data \n Enter 2 to Delete Password \n Enter 3 to Save Password \n Enter 4 to Search Password \n Enter 5 to Exit System")
    ch = input()
    if(ch ==1):
        Display()   
    elif(ch ==2):
        Delete()
    elif(ch ==3):
        Save()
    elif(ch ==4):
        Search()
    elif(ch ==5):
        print("Your getting exit from system...3")
        time.sleep(3)
        work = False
        os.system('cls')