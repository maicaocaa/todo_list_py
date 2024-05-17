import json         # importa modulo jszon, permite trabajar con datos en formato JSON.
# si el archivo task no existe, se cra un nuevo archivo task
# Esta función carga las tareas desde un archivo JSON

""" ------------------------
Crea clase Task, para la creacion de tareas
__init__ inicializa las tareas nuevas como false
se define el metodo para marcar como completado que cambia la porpiedad completed a True
------------------------"""   

class Task:
    def __init__(self, title, description, completed=False):
            self.completed = completed
            self.title = title
            self.description = description

    def mark_completed(self):
        self.completed=True

""" ------------------------
Creamos clase para la gestion de tareas
El constructor __init__ elige el archivo llamado tasks.json

El metodo load_tasks intenta cargar el archivo tasks.json y si no existe entra en la excepcion  para crear un nuevo archivo
Si existe lo abre en modo lectura "r" y lo guarda en file
Luego los valores de la variable file los guarda en  task_data
Esto se hace asi, en varios pasos en vez de todo en un paso 
para que cada línea de codigo tenga olo una finalidad y sea más legible
Task_data será una lista de diccionarios y cada tarea un diccionario.
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
    """
    save_tasks Este método guarda las tareas actuales. abre el archivo json en modo escritura (w) 
    y añade con el metodo dump los valores introducidos.

    add_tasks, necesita un titulo y una descripcion
    crea una nueva tarea llamando a al clase Task y genera un objeto nuevo
    luego llama al metodo save_tasks que lo guarda en el json   
    """
    def save_tasks(self):
        with open (self.file_name, "w") as file:
            json.dump([{"title": task.title, "description": task.description, "completed": task.completed} for task in self.tasks], file, indent=4)

    def add_task(self, title, description):
        new_task=Task(title.upper(), description)
        self.tasks.append(new_task)
        self.save_tasks()

        """ ------------------------
        delete_tasks , con el uso de "del" se borra la tarea indicada desde el pront 
        y se le resta 1 para que coincida con el index real. luego se llama al metodo save_tasks

        show_tasks, revisa si hay tareas, valorando el indice es menos o ingua a la longitud de tasks
        luego itera las tareas guardadas en self.tasks (self.tasks=self.load_tasks())
        realiza n for i para iterar una por una  y valora si esta completada o no. 
        Empieza en el valor 1 y lo imprime
        Si no hay tareas, no entra en la condicion y salta al else 
        devuelve el mensaje de "no hay tareas"

        mark_task_as_completed valora el index si existe, osea, que no sea menos a 0  ç
        y que sea igual o menor a la longitud de la lista task

        si existe, llama al metodo de la clase Task através de self.tasks , mark_completed 
        luego a al metodo de la clase TaskManager save_task
        ------------------------"""   

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
                print(f"{i}. [{status}] \n   {task.title} - {task.description}")

        else:
            print("No hay tareas.")

    def mark_task_as_completed(self,index):
        if 0 <= index <= len(self.tasks):
            self.tasks[index-1].mark_completed()
            self.save_tasks()
        else:
            print("La tarea no existe.")
        
""" ------------------------
Funcion principal main()

Se define la funcion principal  que de primeras llama a la clase TaskManager que comprobará 
si existe o no archivo json de tareas

si existe y es true, imprime las opciones en la consola y espera la entrada de un numero entero

si no es un un numero entero, entra en la excepcion, y muestra al usuario que debe ingresar un numero
si el usuario ingresa un numero que no está conteplado, imprime "Opcion no válida"

Cada opcion llama a un metodo de TaskManager y dicha clase se invocó al iniciar la función main
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

"""
El orden de ejecucion es el siguiente

se ejecuta main()

main invoca la clase TaskManager()

desde TaskManager se carga o se crea el archivo .json

cuando se crea, borra o meodifica una tarea 
"""