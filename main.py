class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, deadline, description):
        self.tasks.append({'deadline': deadline, 'description': description, 'status': 'не выполнено'})

    def complete_tasks(self, description):
        for task in self.tasks:
            if task['descripton'] == description:
                task['status'] = 'выполнено'
                print(f'Задача "{description}" успешно выполнена!')
            else:
                print(f'Задача "{description}" не найдена.')

    def show_tasks(self):
        print(f'Список задач:')
        for task in self.tasks:
            if task['status'] == 'не выполнено':
                print(f"{task['description']} - {task['deadline']}")


t = Task()
t.add_task('сегодня', 'помыть картошку')
t.add_task('завтра', 'почистить картошку')

t.show_tasks()