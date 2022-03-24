#importing library
import json
import os

#input as filepath
filepath = str(input("Enter the file location: "))
#extracting filename from filepath
filename = os.path.basename(filepath)

# Read the sql file
with open(filename, 'r') as sql_query:
    query_string = sql_query.read()
    
#splitting sql queries in sql file
codes = query_string.split(";")
    
#initilizing an empty list to add in information
json_list = []
#first code in sql file
code_id = 1
#looping ot extract information
for code in codes:
    code_type = code.strip().split(' ')[0].strip()
    local_dict = {
        "statement_id": code_id,
        "statement_type": code_type,
        "target_table_name": []
    }
        
    #splitting lines  
    statements = code.splitlines()
    code_id += 1
        
    #looping to strip table names and other information
    for statement in statements:
        for type in ["FROM","JOIN"]:
            if statement.find(type) != -1:
                table_name = statement.strip().split(type)[1]
                if table_name.strip().find(" ") != -1:
                    table_name
                if table_name.find(".") != -1:
                    table_name = table_name.split(".")[0]
                    
                #adding to the details to dictionary
                local_dict["target_table_name"].append({
                    "type": type,
                    "name": table_name,
                    "full query": statement
                })
                    
    #appending the dictionry to the list            
    json_list.append(local_dict)

#writing the information to a json file and savinf it    
file_json = filename.replace('.sql','.json')
with open(file_json,'w') as wf:
    json.dump(json_list,wf,indent=4)
    print(file_json)

