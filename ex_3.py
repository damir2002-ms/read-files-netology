import os

# Функция для считывания содержимого файла и подсчета количества строк
def read_file(file_path):
    with open(file_path, 'r', encoding='cp866') as file:
        lines = file.readlines()
    return lines

# Путь к папке с файлами
folder_path = "D:/рс/python/NETOLOGY/cook_book/1-3"

# Получаем список файлов в папке
file_names = os.listdir(folder_path)

# Сортируем файлы по количеству строк
file_names_sorted = sorted(file_names, key=lambda x: len(read_file(os.path.join(folder_path, x))))

# Создаем результирующий файл и записываем в него содержимое файлов
with open("result_1-3.txt", "w", encoding='cp866') as result_file:
    for file_name in file_names_sorted:
        file_path = os.path.join(folder_path, file_name)
        lines = read_file(file_path)
        # Записываем служебную информацию (имя файла и количество строк)
        result_file.write(f"{file_name}\n")
        result_file.write(f"{len(lines)}\n")
        # Записываем содержимое файла
        result_file.writelines(lines)
        result_file.write("\n")  # Добавляем пустую строку между файлами
