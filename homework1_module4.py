def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total_salary = 0
            count = 0

            for line in file:
                name, salary = line.strip().split(',')
                total_salary += int(salary)
                count += 1

            if count == 0:
                return (0, 0)

            average_salary = total_salary / count
            return total_salary, average_salary

    except FileNotFoundError:
        print(f"Файл по пути {path} не найден.")
        return (0, 0)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return (0, 0)

# Пример использования функции:
path_to_file = r"\git\hw_4module\work_salary.txt"
total, average = total_salary(path_to_file)
print(f"total_salary: {total}, average_salary: {average}")