import os

def crear_carpetas():
    try:
        ruta_base = input("Pega el directorio donde quieres crear las carpetas: ").strip()
        
        if not os.path.isdir(ruta_base):
            print("La ruta ingresada no es válida.")
            return

        inicio = int(input("Ingrese el número de inicio: "))
        fin = int(input("Ingrese el número final: "))
        excluir_input = input("Ingrese los números a excluir, separados por comas (ej: 28,39,30): ")
        
        # Convertimos la entrada de exclusiones a un conjunto de enteros
        excluir = set(int(x.strip()) for x in excluir_input.split(',') if x.strip().isdigit())

        print("Directorio base:", ruta_base)

        for i in range(inicio, fin + 1):
            if i not in excluir:
                nombre_carpeta = os.path.join(ruta_base, str(i))
                if not os.path.exists(nombre_carpeta):
                    os.makedirs(nombre_carpeta)
                    print(f"Carpeta creada: {nombre_carpeta}")
                else:
                    print(f"La carpeta {nombre_carpeta} ya existe. Se omite.")
            else:
                print(f"Número {i} está en la lista de exclusión. Se omite.")
    
    except ValueError:
        print("Error: Asegúrese de ingresar solo números válidos.")

if __name__ == "__main__":
    crear_carpetas()
