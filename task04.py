# Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
import json
import pickle
import os
def from_json_to_pickle(dir_):
    for file in os.listdir(dir_):
        if file.endswith(".json") and os.path.isfile(file):
            with(open(file, "r", encoding="utf-8") as f_j,
                 open(file.rstrip("json")+'pickle', "wb") as f_p):
                data = json.load(f_j)
                pickle.dump(data,f_p)

# def pickle_read(file):
#     with open(file, "rb") as pick:
#         data = pickle.load(pick)
#         print(data)

if __name__ == '__main__':
    from_json_to_pickle(os.getcwd())
    # pickle_read("task03.pickle")