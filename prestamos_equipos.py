from datetime import datetime

# Estructura principal de datos:
# Diccionario anidado para almacenar equipos.
# Cada equipo es un diccionario con su estado (disponible) y una lista de préstamos.
# Cada préstamo es una tupla inmutable (usuario, fecha).
equipos = {
    "Laptop A": {
        "disponible": True,
        "prestamos": []
    },
    "Proyector B": {
        "disponible": False,
        "prestamos": [("Ana", "2025-08-28 14:30:00")]
    },
    "Monitor C": {
        "disponible": True,
        "prestamos": []
    }
}

# --- Funciones de gestión ---

def mostrar_equipos():
    """Muestra todos los equipos registrados y su estado de disponibilidad."""
    print("\n--- Estado Actual de los Equipos ---")
    if not equipos:
        print("No hay equipos registrados en el sistema.")
        return

    for nombre, datos in equipos.items():
        estado = "Disponible" if datos["disponible"] else "Prestado"
        print(f"- {nombre}: {estado}")

def registrar_prestamo():
    """Permite registrar un nuevo préstamo de un equipo."""
    mostrar_equipos()
    print("\n--- Registrar Nuevo Préstamo ---")
    
    equipo_a_prestar = input("Ingresa el nombre del equipo a prestar: ")
    
    if equipo_a_prestar in equipos:
        if equipos[equipo_a_prestar]["disponible"]:
            usuario = input("Ingresa el nombre del usuario: ")
            
            # Obtiene la fecha y hora actual en un formato legible
            fecha_prestamo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Crea la tupla inmutable con los datos del préstamo
            nuevo_prestamo = (usuario, fecha_prestamo)
            
            # Agrega la tupla a la lista de préstamos del equipo
            equipos[equipo_a_prestar]["prestamos"].append(nuevo_prestamo)
            
            # Actualiza el estado del equipo a no disponible
            equipos[equipo_a_prestar]["disponible"] = False
            
            print(f"Préstamo de '{equipo_a_prestar}' a '{usuario}' registrado exitosamente.")
        else:
            print(f"El equipo '{equipo_a_prestar}' ya está prestado.")
    else:
        print(f"El equipo '{equipo_a_prestar}' no se encuentra en el inventario.")

def devolver_equipo():
    """Permite marcar un equipo como devuelto."""
    print("\n--- Devolver un Equipo ---")
    equipo_a_devolver = input("Ingresa el nombre del equipo a devolver: ")

    if equipo_a_devolver in equipos:
        if not equipos[equipo_a_devolver]["disponible"]:
            # Cambia el estado del equipo a disponible
            equipos[equipo_a_devolver]["disponible"] = True
            print(f"El equipo '{equipo_a_devolver}' ha sido devuelto y está nuevamente disponible.")
        else:
            print(f"El equipo '{equipo_a_devolver}' no está actualmente prestado.")
    else:
        print(f"El equipo '{equipo_a_devolver}' no se encuentra en el inventario.")

def ver_historial():
    """Muestra el historial completo de préstamos de todos los equipos."""
    print("\n--- Historial de Préstamos ---")
    if not equipos:
        print("No hay equipos registrados en el sistema.")
        return

    for nombre, datos in equipos.items():
        print(f"\n- Historial de '{nombre}':")
        if datos["prestamos"]:
            # Recorre la lista de tuplas de préstamos
            for usuario, fecha in datos["prestamos"]:
                print(f"  · Prestado a '{usuario}' en la fecha: {fecha}")
        else:
            print("  Sin préstamos registrados.")

def agregar_equipo():
    """Permite agregar un nuevo equipo al inventario."""
    print("\n--- Agregar Nuevo Equipo ---")
    nuevo_equipo = input("Ingresa el nombre del nuevo equipo: ")
    
    # Verifica si el equipo ya existe para evitar duplicados
    if nuevo_equipo in equipos:
        print(f"El equipo '{nuevo_equipo}' ya existe en el inventario.")
    else:
        # Crea una nueva entrada en el diccionario con los datos iniciales
        equipos[nuevo_equipo] = {
            "disponible": True,
            "prestamos": []
        }
        print(f"El equipo '{nuevo_equipo}' ha sido agregado exitosamente al inventario.")

# --- Menú principal de la aplicación ---

def menu():
    """Función principal que muestra el menú interactivo y maneja las opciones del usuario."""
    while True:
        print("\n" + "="*40)
        print("  SISTEMA DE PRÉSTAMOS DE EQUIPOS")
        print("="*40)
        print("1. Ver equipos disponibles")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial de préstamos")
        print("5. Agregar nuevo equipo")
        print("6. Salir")
        print("="*40)
        
        opcion = input("Selecciona una opción (1-6): ")
        
        if opcion == "1":
            mostrar_equipos()
        elif opcion == "2":
            registrar_prestamo()
        elif opcion == "3":
            devolver_equipo()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            agregar_equipo()
        elif opcion == "6":
            print("\n¡Gracias por usar el sistema!")
            break
        else:
            print("Opción no válida. Por favor, selecciona un número del 1 al 6.")

# El programa comienza aquí
if __name__ == "__main__":
    menu()