import socket
import os
import threading
import numpy as np
import pandas as pd
import json
import string
import random

# Create server TCP socket 
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind((socket.gethostname(),9999))
print('Waiting for connection from Client')
sock.listen(5)

# Create a dataframe
Grades = pd.read_csv("networks_grades_df.csv",index_col=0)

def send(client_sock,msg):
    client_sock.send(bytes(msg,'utf-8'))

def reg_client(client_sock,Grades):
    Grades = pd.read_csv("networks_grades_df.csv",index_col=0)
    send(client_sock,"Welcome, pls enter your details:)")#intro msg

    send(client_sock,"Enter Student Ashoka ID: ")#get username
    name = client_sock.recv(2048).decode()

    send(client_sock, "Enter Password: ")#get password
    password = client_sock.recv(2048).decode()

    print(list(Grades['Name']))
    u_idx = list(Grades['Name']).index(name)# get user index in df
    
    if name in Grades['Name'].to_numpy() and password == Grades.iloc[u_idx]['Password']:
        print('Authentications details Valid!')
        send(client_sock,'Authentication Sucessfull!') 

        #Ask for student name
        send(client_sock,'Enter Student Ashoka id for Student data: ')
        stu_name = client_sock.recv(2048).decode()
        print("student name entered is ",stu_name)

        if stu_name in Grades['Name'].to_numpy():
            send(client_sock,"Yep")

            stu_idx = list(Grades['Name']).index(str(stu_name))#get stu index

            m = Grades.iloc[stu_idx].to_json(orient='index')#convert df to dict
            g = json.dumps(m)#convert dict to json
            # print(json.loads(g))
            
            client_sock.send(g.encode())#send req df

            #print(Grades.iloc[stu_idx])
            
        else:
            send(client_sock,"Nope")
            
    
    else:
        send(client_sock,'Authentication Details invalid')
        
        
        

    

def new_client(client_sock,Grades):
    send(client_sock,"Lets make an account now!") #New client intro msg

    send(client_sock,"Enter Ashoka id: ")#get Ashoka id
    Ashoka_id = client_sock.recv(2048).decode()

    if Ashoka_id[-14:] != '@ashoka.edu.in':#check if ashoka id
        send(client_sock,'Not a valid ashoka id')
        client_sock.close()

    # Generate password
    res = ''.join(random.choices(string.ascii_uppercase +
                            string.digits, k = 5))
    send(client_sock,f"Password Assigned to you is: {res}")
    print("password assigned")

    #Add empty row to df with id
    new_data = {"Name":[Ashoka_id],'A1':[0],'A1 max':[0],'A2':[0],'A2 max':[0],\
            'A3':[0],'A3 max':[0], 'Midterm':[0],'Midterm max':[0],'Password':[0]}
    #Add password to the new row
    new_data['Password'] = res
    new_data = pd.DataFrame(new_data)
    
    
    
    
    #add the row to the main df
    Grades = pd.read_csv("networks_grades_df.csv",index_col=0)
    Grades = Grades.append(new_data, ignore_index = True)
    
    Grades.to_csv("networks_grades_df.csv", index = True)
    
    print(Grades)
    send(client_sock,"congrats! you have created an account. Reopen application to login")
    client_sock.close()
    pass



def client_func(client_sock):
    send(client_sock,"Are you a registered user? 'Y' for Yes and 'N' for No: ")
    reg_info = client_sock.recv(2048).decode()


    if reg_info == "Y":
        
        reg_client(client_sock,Grades)

    elif reg_info == "N":
        
        new_client(client_sock,Grades)
        pass





    






while True:
    client_sock, client_addr = sock.accept()
    print(f'Connected to client with address {client_addr}')
    #putting a client onto a thread
    client_handler = threading.Thread(target=client_func,
        args=(client_sock,) )
    client_handler.start()
    
sock.close()