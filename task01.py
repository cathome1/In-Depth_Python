# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов.
# * При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>
import os

def group_rename_files(new_name, old_extention, new_extention):
    count = 0
    for i in os.listdir():
        if i.split(".")[-1] == old_extention:
            count+=1
            os.rename(i,str(*i.split('.')[0:-1])+"_"+new_name+'_'+str(count)+'.'+new_extention)


if __name__ == '__main__':
    group_rename_files('work','txt','bin')