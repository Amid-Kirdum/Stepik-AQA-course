import os

# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
print(os.path.abspath(__file__))

# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'file')
print(os.path.abspath(os.path.dirname(__file__)))
