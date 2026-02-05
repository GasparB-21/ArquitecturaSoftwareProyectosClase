#Creamos el menú que ejecutara al inciar la app

#Menu de la app
def menu():
    print("Bienvenido a TODO App")
    print("¿Que función deseas ejecutar?")
    print("1. Añadir una tarea a la lista")
    print("2. Marcara una tarea como completada")
    print("3. Eliminar una tarea de la lista")
    print("4. Salir")

#Creamos la función para añadir una tarea a la lista
def add_tarea(tarea_file):
    tarea = input("Ingrese la tarea que desea añadir: ")
    with open(tarea_file, "a") as file:
        file.write(tarea + "\n")
    print("Tarea añadida exitosamente.")

#Creamos la función para marcar una tarea como completada
def complete_tarea(tarea_file):
    with open(tarea_file, "r") as file:
        tareas = file.readlines()
    if not tareas:
        print("No hay tareas para marcar como completadas.")
        return
    for i, tarea in enumerate(tareas):
        print(f"{i + 1}. {tarea.strip()}")
    try:
        tarea_index = int(input("Ingrese el número de la tarea que desea marcar como completada: ")) - 1
        if 0 <= tarea_index < len(tareas):
            tareas[tarea_index] = f"[Completada] {tareas[tarea_index]}"
            with open(tarea_file, "w") as file:
                file.writelines(tareas)
            print("Tarea marcada como completada exitosamente.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número.")

#Creamos la función para eliminar una tarea de la lista
def delete_tarea(tarea_file):
    with open(tarea_file, "r") as file:
        tareas = file.readlines()
    if not tareas:
        print("No hay tareas para eliminar.")
        return
    for i, tarea in enumerate(tareas):
        print(f"{i + 1}. {tarea.strip()}")
    try:
        tarea_index = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
        if 0 <= tarea_index < len(tareas):
            del tareas[tarea_index]
            with open(tarea_file, "w") as file:
                file.writelines(tareas)
            print("Tarea eliminada exitosamente.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número.")

#Función principal para ejecutar la app
def main():
    tarea_file = "./Clase_05-02-26/tareas.txt"
    while True:
        menu()
        choice = input("Ingrese el número de la función que desea ejecutar: ")
        if choice == "1":
            add_tarea(tarea_file)
        elif choice == "2":
            complete_tarea(tarea_file)
        elif choice == "3":
            delete_tarea(tarea_file)
        elif choice == "4":
            print("Gracias por usar TODO App. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor ingrese un número del 1 al 4.")

if __name__ == "__main__":
    main()