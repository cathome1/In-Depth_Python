# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями. В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора. Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь. Имя исходного и конечного файлов передавайте как аргументы функции
import csv
import json

def from_csv_to_json(start_file,end_file):
    with(open(start_file,"r",encoding="utf-8") as data,
         open(end_file,"w",encoding="utf-8") as f_data):
        rows = csv.reader(data)
        new_data = []
        for row in list(rows)[1:]:
            uaccess, uid, uname = row
            dct = {"access":uaccess,
                       "id":(10-len(uid))*"0"+uid,
                       "name":uname,
                       "hash":hash(uname+uid)}
            new_data.append(dct)
        json.dump(new_data,f_data, indent=2, ensure_ascii=False)




if __name__ == '__main__':
    from_csv_to_json("../file.csv", "task03.json")
