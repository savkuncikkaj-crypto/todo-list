tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Задача "{task}" добавлена.')

def show_tasks():
    if not tasks:
        print("Нет задач.")
    else:
        print("Список задач:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task(task_index):
    if 0 <= task_index < len(tasks):
        removed = tasks.pop(task_index)
        print(f'Задача "{removed}" удалена.')
    else:
        print("Некорректный индекс задачи.")

# Пример использования функций
add_task("Купить молоко")
add_task("Прочитать книгу")
show_tasks()
remove_task(0)
show_tasks()
