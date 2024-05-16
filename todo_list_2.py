import json
# si el archivo task no existe, se cra un nuevo archivo task

# Esta función carga las tareas desde un archivo JSON
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No se encuentra el archivo de tareas.")
        create_new_list = input("¿Deseas crear una nueva lista de tareas? (s/n): ").lower()
        if create_new_list == "s":
            return []
        else:
            print ("Se ha cerrado el programa")
            exit()  # Salir del programa si el usuario elige no crear una nueva lista



# Esta función guarda las tareas en un archivo JSON
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Cargar las tareas al inicio del programa
tasks = load_tasks()

def add_task():
    task = input("Introduce una nueva tarea: ")
    tasks.append({"task": task, "completed": False})
    save_tasks()  # Guardar las tareas después de agregar una nueva

def delete_task():
    task_index = int(input("Ingresa la tarea que deseas eliminar: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Tarea eliminada con éxito.")
        save_tasks()  # Guardar las tareas después de eliminar una
    else:
        print("La tarea no existe.")

def show_tasks():
    if tasks:
        print("Lista de tareas: ")
        for i, task in enumerate(tasks, 1):
            status = "Completada" if task["completed"] else "Pendiente"
            print(f"{i}. [{status}] {task['task']}")
    else:
        print("No hay tareas pendientes.")

def mark_task_completed():
    task_index = int(input("Ingresa el número de la tarea completada: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Tarea marcada como completada.")
        save_tasks()  # Guardar las tareas después de marcar una como completada
    else:
        print("La tarea no existe.")

def main():
    option = 0

    while option != 5:
        print("\n --- Lista de tareas pendientes --- ")
        print("1. Agregar nueva tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar tareas")
        print("4. Marcar tarea como completada")
        print("5. Salir")

        option = int(input("Selecciona una opción: "))

        if option == 1:
            add_task()
        elif option == 2:
            delete_task()
        elif option == 3:
            show_tasks()
        elif option == 4:
            mark_task_completed()
        elif option == 5:
            print("Has salido de la aplicación")
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()