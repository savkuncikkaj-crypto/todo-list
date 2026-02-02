tasks = []

def add_task(task, priority):
    """Добавляет новую задачу с указанным приоритетом в список."""
    tasks.append((task, priority))
    print(f'Задача "{task}" с приоритетом "{priority}" добавлена.')

def show_tasks():
    """Отображает все задачи с их приоритетами."""
    if not tasks:
        print("Нет задач.")
    else:
        print("Список задач:")
        for i, (task, priority) in enumerate(tasks, start=1):
            print(f"{i}. {task} (Приоритет: {priority})")

def remove_task(task_index):
    """Удаляет задачу по индексу."""
    if 0 <= task_index < len(tasks):
        removed = tasks.pop(task_index)
        print(f'Задача "{removed[0]}" удалена.')
    else:
        print("Некорректный индекс задачи.")

# Пример использования функций
add_task("Купить молоко", "Высокий")
add_task("Прочитать книгу", "Средний")
show_tasks()
remove_task(0)  # Удаляем первую задачу
show_tasks()
