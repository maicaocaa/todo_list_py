import json
# si el archivo task no existe, se cra un nuevo archivo task
# Esta función carga las tareas desde un archivo JSON

""" ------------------------
Creados de objeto tarea Task
------------------------"""   

class Task:
    def __init__(self, title, description, completed=False):
            self.completed = completed
            self.title = title
            self.description = description

    def mark_completed(self):
        self.completed=True

""" ------------------------
Gestor de Tareas
------------------------"""   

class TaskManager:
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name
        self.tasks=self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_name, "r") as file:
                task_data = json.load(file)
                return [Task(**task)for task in task_data]
        except FileNotFoundError:
            print("No se encuentra el archivo de tareas.")
            create_new_list= input ("Desea crear una nueva lista de tareas? (s/n)")
            if create_new_list == "s":
                return []
            else:
                print("Se ha cerrado el programa")
                exit()
    
    def save_tasks(self):
        with open (self.file_name, "w") as file:
            json.dump([{"title": task.title, "description": task.description, "completed": task.completed} for task in self.tasks], file, indent=4)

    def add_task(self, title, description):
        new_task=Task(title.upper(), description)
        self.tasks.append(new_task)
        self.save_tasks()

    def delete_task(self,index):
        if 0 <= index <= len(self.tasks):
            del self.tasks[index -1]
            print ("Tarea eliminada con exito.")
            self.save_tasks()
        else:
            print ("La tarea no existe.") 

    def show_tasks(self):
        if self.tasks:
            print("Lista de tareas: ")
            for i, task in enumerate(self.tasks, 1):
                status = "Completada" if task.completed else "Pendiente"
                print(f"{i}. [{status}] {task.title} - {task.description}")

        else:
            print("No hay tareas.")

    def mark_task_as_completed(self,index):
        if 0 <= index <= len(self.tasks):
            self.tasks[index-1].mark_completed()
            self.save_tasks()
        else:
            print("La tarea no existe.")
        
""" ------------------------
funcion principal
------------------------"""

def main():
    task_manager=TaskManager()

    while True:
        print("\n --- Lista de tareas  --- ")
        print("1. Agregar nueva tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar tareas")
        print("4. Marcar tarea como completada")
        print("5. Salir")
      
        try:
            option = int(input("Selecciona una opción: "))
        except ValueError:
            print("Error: Debes ingresar un número entero. Inténtalo de nuevo.")
            continue

        if option == 1:
            title = input("Introduce el título de la tarea: ")
            description = input("Indica la descripción: ")
            task_manager.add_task(title, description)
        elif option == 2:
            index = int(input("Introduce el número  de la tarea a ELIMINAR: "))
            task_manager.delete_task(index)
        elif option == 3:
            print("Estas son todas tus tareas: ")
            task_manager.show_tasks()
        elif option == 4:
            index = int(input("Ingresa el nº de la tarea que quieres COMPLETAR: "))
            task_manager.mark_task_as_completed(index)
        elif option == 5:
            print("Has salido de la aplicación")
            break
        else:
            print("Opción no válida. Intentalo de nuevo.")

if __name__ == "__main__":
    main()