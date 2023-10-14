# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.
import json
import csv

def json_to_csv(file_name: str):
    fieldnames = ["access","id","name"]
    with (open(file_name, "r",encoding="utf-8") as f_j,
          open(file_name.strip(".json")+".csv","w",encoding="utf-8", newline='') as f_c):
        data = json.load(f_j)
        writer = csv.DictWriter(f_c, fieldnames=fieldnames)
        writer.writeheader()
        for item in data.items():
            for person in item[1].items():
                writer.writerow({"access":item[0],"id":person[0],"name":person[1]})

if __name__ == '__main__':
    json_to_csv("file.json")