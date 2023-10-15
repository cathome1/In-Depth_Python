# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестирования возьмите pickle версию файла из предыдущей задачи.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
import csv
import pickle


def from_pickle_to_csv(pickle_file, csv_file="task05.csv"):
    with(open(pickle_file, "rb") as f_p,
         open(csv_file, "w", encoding="utf-8", newline="") as f_c):
        data = pickle.load(f_p)
        headers = list(data[0].keys())
        writer = csv.DictWriter(f_c, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    from_pickle_to_csv("../task03.pickle")
