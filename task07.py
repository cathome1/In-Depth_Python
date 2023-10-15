# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import os, csv, json, pickle

def parse_listdir(dir_):
    results = []
    for root,folders,files in os.walk(dir_):
        for file in files:
            path = os.path.join(root,file)
            results.append({"parent_dir":root,
                            "is_file":True,
                            "name":file,
                            "size":os.path.getsize(path)})
        for folder in folders:
            path = os.path.join(root, folder)
            results.append({"parent_dir":root,
                            "is_file":False,
                            "name":folder,
                            "size":os.path.getsize(path)})
    with(open(dir_.split('/')[-1]+'.json', "w", encoding="utf-8") as f_j,
         open(dir_.split('/')[-1]+'.csv', "w", encoding="utf-8", newline="") as f_c,
         open(dir_.split('/')[-1]+'.pickle', "wb") as f_p):
        json.dump(results, f_j, indent=2)
        pickle.dump(results,f_p)
        writer = csv.DictWriter(f_c, fieldnames=["parent_dir","is_file","name","size"])
        writer.writeheader()
        for row in results:
            writer.writerow(row)

if __name__ == '__main__':
    parse_listdir(os.getcwd())