import socket
import json
import pandas as pd
import ast
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((socket.gethostname(),9999))

def send(client_sock,msg):
    client_sock.send(bytes(msg,'utf-8'))

# Registered user or not
reg_prompt = client.recv(2048).decode()
reg_status = input(reg_prompt)
send(client,reg_status)

if reg_status == "Y":# User is registered
    reg_intro_msg = client.recv(2048).decode()#intro msg

    uname_prompt = client.recv(2048).decode()#give username
    user_name = input(uname_prompt)
    send(client,user_name)

    passw_prompt = client.recv(2048).decode()#give password
    password = input(passw_prompt)
    send(client,password)
    
    auth_result = client.recv(2048).decode()#get auth result(password wrong/right)
    
    if auth_result == "Authentication Details invalid":#wrong details
        print("Try again")
        client.close()
    print("Authentication Successfull!")
    stu_name_prompt = client.recv(2048).decode()#give stu name
    stu_name = input(stu_name_prompt)
    send(client,stu_name)

    stu_name_result = client.recv(2048).decode()#give stu name
    #print("is stu there? ",stu_name_result)

    if stu_name_result == "Yep":
        #print("inside yep block")
        stu_grades = client.recv(2048).decode()#receive req student's grades
        stu_grades = json.loads(stu_grades)
        #print(stu_grades)
        stu_grades = ast.literal_eval(stu_grades)
        #print(type(stu_grades))
        stu_df = pd.DataFrame.from_dict(stu_grades, orient="index")
        print(stu_df)

    elif stu_name_result == "Nope":
        print("Student does not exist, try again.")
        client.close()


elif reg_status == "N":# New user
    nuser_intro_prompt = client.recv(2048).decode()#intro prompt

    clg_id_prompt = client.recv(2048).decode()#give Ashoka id
    Ashoka_id = input(clg_id_prompt)

    send(client,Ashoka_id)

    nuser_password = client.recv(2048).decode()#receive password
    print(nuser_password)

    congrats_msg = client.recv(2048).decode()#successfully created account msg
    print(congrats_msg)

    pass


else:
    print("Invalid response")