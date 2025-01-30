class todo_service:
    def __init__(self,repository):
       self.repository = repository

    def add_task(self,task):
        try:
            tasks = self.repository.get_tasks()
            tasks.append(task)
            self.repository.save_tasks(tasks)
        except Exception as e:
            raise Exception(f"Failed to add task: {e}") 

    def delete_task(self,index):
        try:
            tasks = self.repository.get_tasks()
            # Ensure tasks is a list
            if not isinstance(tasks, list):
                raise TypeError("Expected a list of tasks, got something else.")
            
            if 0 <= index < len(tasks):
                del tasks[index]
                self.repository.save_tasks(tasks)
            else:
                raise IndexError("Task index out of range.")
        except IndexError:
            raise IndexError(f"Task index {index} is invalid.")
        except Exception as e:
            raise Exception(f"Failed to delete task: {e}")

    def show_list(self):
        try:
            return self.repository.get_tasks()
        except Exception as e:
            raise Exception(f"Failed to retrieve tasks: {e}")