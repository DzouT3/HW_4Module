def get_cats_info(path):
    cat_info_list = []
    
    try:
        with open(path, 'r', encoding='cp1251') as file:
            for line in file:
                cat_data = line.strip().split(', ')
                cat_info = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": cat_data[2]
                }
                cat_info_list.append(cat_info)
        
    except FileNotFoundError:
        print(f"Файл по пути {path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    return cat_info_list

# Пример использования функции с файлом:
cats_info = get_cats_info("path_to_cats_file.txt")
for cat in cats_info:
    print(cat)