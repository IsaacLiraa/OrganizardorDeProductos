import os

# Función para renombrar las carpetas seleccionadas dentro de un rango con nombres temporales
def renombrar_carpetas(directorio, inicio_rango_original, fin_rango_original, inicio_rango_nuevo, fin_rango_nuevo):
    try:
        # Obtener una lista de todas las carpetas en el directorio
        carpetas = [carpeta for carpeta in os.listdir(directorio) if os.path.isdir(os.path.join(directorio, carpeta))]
        
        # Ordenar las carpetas alfabéticamente (o numéricamente si las carpetas son números)
        carpetas.sort(key=lambda x: int(x))

        # Verificar que el rango original esté dentro de los límites válidos
        if inicio_rango_original > fin_rango_original:
            print("El rango original de inicio debe ser menor o igual al de fin.")
            return

        # Verificar que el rango nuevo esté dentro de los límites válidos
        if inicio_rango_nuevo > fin_rango_nuevo:
            print("El rango de nuevos nombres debe ser válido.")
            return

        # Determinar cuántas carpetas queremos renombrar
        carpetas_a_renombrar = [carpeta for carpeta in carpetas if inicio_rango_original <= int(carpeta) <= fin_rango_original]
        cantidad_carpetas_a_renombrar = len(carpetas_a_renombrar)

        # Verificar que hay suficientes nuevos nombres en el rango
        cantidad_nombres_disponibles = fin_rango_nuevo - inicio_rango_nuevo + 1
        if cantidad_carpetas_a_renombrar > cantidad_nombres_disponibles:
            print(f"No hay suficientes nombres disponibles en el rango nuevo para renombrar {cantidad_carpetas_a_renombrar} carpetas.")
            return

        # Paso 1: Renombrar las carpetas seleccionadas a nombres temporales
        renombradas = 0
        for carpeta in carpetas_a_renombrar:
            # Ruta original
            ruta_actual = os.path.join(directorio, carpeta)

            # Nombre temporal
            nombre_temporal = f"{carpeta}_TEMP"
            ruta_temporal = os.path.join(directorio, nombre_temporal)

            # Renombrar a nombre temporal para evitar conflictos
            os.rename(ruta_actual, ruta_temporal)
            print(f"Renombrada {carpeta} a {nombre_temporal}")

            renombradas += 1

        # Paso 2: Renombrar las carpetas temporales a los nuevos nombres
        renombradas = 0
        for carpeta in carpetas_a_renombrar:
            # Ruta de la carpeta temporal
            ruta_temporal = os.path.join(directorio, f"{carpeta}_TEMP")

            # Nuevo nombre basado en el rango
            nuevo_nombre = str(inicio_rango_nuevo + renombradas)
            nueva_ruta = os.path.join(directorio, nuevo_nombre)

            # Renombrar a los nuevos nombres
            os.rename(ruta_temporal, nueva_ruta)
            print(f"Renombrada {carpeta}_TEMP a {nuevo_nombre}")

            renombradas += 1

    except FileNotFoundError:
        print("El directorio especificado no existe.")
    except PermissionError:
        print("No se tienen permisos suficientes para realizar esta operación.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Función para obtener el rango de nombres original y nuevo del usuario
def obtener_rangos():
    while True:
        try:
            # Entrada del rango original (inicio y fin)
            rango_original = input("Introduce el rango original de carpetas (inicio y fin) separados por un guion (por ejemplo: 1-10): ").strip()
            # Entrada del rango nuevo de nombres
            rango_nuevo = input("Introduce el rango de nuevos nombres (inicio y fin) separados por un guion (por ejemplo: 100-200): ").strip()

            # Dividir los rangos
            inicio_rango_original, fin_rango_original = map(int, rango_original.split('-'))
            inicio_rango_nuevo, fin_rango_nuevo = map(int, rango_nuevo.split('-'))

            # Verificar que el inicio sea menor que el fin
            if inicio_rango_original > fin_rango_original:
                print("El valor de inicio del rango original debe ser menor que el valor de fin.")
                continue
            if inicio_rango_nuevo > fin_rango_nuevo:
                print("El valor de inicio del rango nuevo debe ser menor que el valor de fin.")
                continue

            return inicio_rango_original, fin_rango_original, inicio_rango_nuevo, fin_rango_nuevo
        except ValueError:
            print("Formato incorrecto. Asegúrate de ingresar dos números separados por un guion.")
            continue

# Función principal
def main():
    # Ruta del directorio donde están las carpetas
    directorio = input("Introduce la ruta del directorio: ").strip()

    # Obtener los rangos de nombres original y nuevo
    inicio_rango_original, fin_rango_original, inicio_rango_nuevo, fin_rango_nuevo = obtener_rangos()

    # Ejecutar la función de renombrado
    renombrar_carpetas(directorio, inicio_rango_original, fin_rango_original, inicio_rango_nuevo, fin_rango_nuevo)

# Ejecutar el script
if __name__ == "__main__":
    main()
