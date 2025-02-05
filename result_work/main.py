from task_manager import TaskManager

my_task = TaskManager()
my_task.add_task('Wash the dishes')
my_task.add_task('Do homework')
my_task.complete_task(0)
my_task.add_task('Go walk')
my_task.remove_task(0)
my_task.save_to_json('Tasks.json')

