
tasks = []

def add_task():
    task = input("Introduce una nueva tarea: ")
    tasks.append({"task": task, "completed": False})
    print("Tarea añadida con éxito.")

def delete_task():
    task_index = int(input("Ingresa la tarea que deseas eliminar: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Tarea eliminada con éxito.")
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
