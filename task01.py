# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
def filedata(path: str) -> tuple:
    file_name = path.split("/")[-1].split(".")[0]
    file_type = path.split("/")[-1].split(".")[1]
    file_path = "/".join(path.split("/")[0:-1])
    return file_path, file_name, file_type


print(filedata("/gbfv/thygft/thyjyht/rgh.fgs"))
