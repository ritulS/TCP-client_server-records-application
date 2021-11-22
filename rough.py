import json
import ast
import pandas as pd


# m = '{"Unnamed: 0":2,"Name":"Bruce","A1":95,"A1 max":100,"A2":36,"A2 max":50,"A3":18,"A3 max":20,"Midterm":89,"Midterm max":100,"Password":"B"}'
# m = ast.literal_eval(m)
# #m = json.loads(m)

# print(type(m))
# Grades = pd.read_csv("networks_grades_df.csv")
# new_data = {"Name":['jindal_id'],'A1':[0],'A1 max':[0],'A2':[0],'A2 max':[0],\
#             'A3':[0],'A3 max':[0], 'Midterm':[0],'Midterm max':[0],'Password':[0]}
# #Add password to the new row
# new_data['Password'] = 'res'
# new_data = pd.DataFrame(new_data)
# Grades = Grades.append(new_data, ignore_index = True)
# print(new_data)
# print(Grades)
##################################################
# new_data = {"Name":['jindal_id'],'A1':[0],'A1 max':[0],'A2':[0],'A2 max':[0],\
#             'A3':[0],'A3 max':[0], 'Midterm':[0],'Midterm max':[0],'Password':[0]}

# new_data = pd.DataFrame(new_data)
Grades = pd.read_csv("networks_grades_df.csv",index_col=0)
# Grades = Grades.append(new_data, ignore_index = True)

# Grades.to_csv("networks_grades_df.csv", index = False)
# Grades = Grades.reset_index()
# Grades.to_csv("networks_grades_df.csv", index = False)
# print(Grades.index.tolist())
# print(list(Grades["Name"]))
# print(list(Grades['Name']).index('ritul'))

m = 'ritul@ashoka.edu.in'


print(m[-14:])