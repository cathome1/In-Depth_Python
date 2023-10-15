# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. Распечатайте его как pickle строку.

import csv
import pickle


def from_csv_to_pickle(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        data = list(csv.reader(file))
        access, id_, name, hash = data[0]
        dct = []
        for row in data[1:]:
            dct.append({access: row[0], id_: row[1], name: row[2], hash: row[3]})
        a = pickle.dumps(data)
        print(a)


if __name__ == '__main__':
    from_csv_to_pickle("../task05.csv")
