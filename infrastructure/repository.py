import os

class FileRepository:
    def __init__(self, file_path):
        self.file_path =  file_path

    def get_tasks(self):
        try:    
            if not os.path.exists(self.file_path):
                return []
            with open(self.file_path,"r") as file:
                tasks = [line.strip() for line in file.readlines()]
                # Ensure tasks is always a list
                if not isinstance(tasks, list):
                    raise TypeError("Expected a list of tasks, got something else.")
                return tasks
        except Exception as e:
            raise Exception(f"Failed to read tasks from {self.file_path}: {e}")

    def save_tasks(self, tasks):
        try:
             # Ensure tasks is a list before writing
            if not isinstance(tasks, list):
                raise TypeError("Expected a list of tasks to save.")
            with open(self.file_path, "w") as file:
                for task in tasks:
                    file.write(task + "\n")
        except Exception as e:
            raise Exception(f"Failed to save tasks to {self.file_path}: {e}")