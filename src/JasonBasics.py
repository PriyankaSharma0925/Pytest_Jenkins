import json
import os



j_var = '{ "id": 101, "name": "Mike Lang","email": "mike.lang@example.com"}'

json_to_dic = json.loads(j_var)

print(json_to_dic)


dic_to_json = json.dumps(json_to_dic)
print(dic_to_json)

for item in json_to_dic:
    print(json_to_dic[item])

with open("../Data/Json_Fundamentals.json", "r") as file:
    jfile_to_dic = json.load(file)

    for item in jfile_to_dic:
        print(jfile_to_dic[item])
