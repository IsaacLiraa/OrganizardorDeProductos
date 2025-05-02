import os
import shutil

def crear_carpetas_y_copiar_imagenes(rango_carpetas_origen, rango_imagenes_origen, directorio_destino, directorio_imagenes_origen):
    """
    Crea un rango de carpetas y copia las imágenes de otro directorio según los rangos dados.
    
    :param rango_carpetas_origen: Tuple con el rango para las carpetas en el directorio destino (min, max)
    :param rango_imagenes_origen: Tuple con el rango de imágenes a copiar (min, max)
    :param directorio_destino: Ruta del directorio donde se crearán las carpetas
    :param directorio_imagenes_origen: Ruta del directorio donde se encuentran las imágenes
    
    :return: None
    """
    
    # Crear las carpetas en el directorio destino
    for i in range(rango_carpetas_origen[0], rango_carpetas_origen[1] + 1):
        carpeta_destino = os.path.join(directorio_destino, str(i))
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
            print(f"Carpeta {carpeta_destino} creada.")
        else:
            print(f"La carpeta {carpeta_destino} ya existe.")

    # Copiar las imágenes a las carpetas correspondientes
    for i in range(rango_imagenes_origen[0], rango_imagenes_origen[1] + 1):
        carpeta_imagen_origen = os.path.join(directorio_imagenes_origen, str(i))
        
        if os.path.exists(carpeta_imagen_origen):
            imagenes = os.listdir(carpeta_imagen_origen)
            for imagen in imagenes:
                # Asumimos que las imágenes son archivos, no subdirectorios
                if os.path.isfile(os.path.join(carpeta_imagen_origen, imagen)):
                    # El número de la carpeta de destino será el mismo que el de la imagen
                    carpeta_destino = os.path.join(directorio_destino, str(i - rango_imagenes_origen[0] + rango_carpetas_origen[0]))
                    if os.path.exists(carpeta_destino):
                        # Copiar la imagen a la carpeta correspondiente
                        destino_imagen = os.path.join(carpeta_destino, imagen)
                        shutil.copy(os.path.join(carpeta_imagen_origen, imagen), destino_imagen)
                        print(f"Imagen {imagen} copiada a {carpeta_destino}")
                    else:
                        print(f"Carpeta de destino {carpeta_destino} no encontrada para la imagen {imagen}.")
        else:
            print(f"No se encontró la carpeta de origen {carpeta_imagen_origen}.")
    
    print("Proceso completado.")

# Rango de las carpetas que quieres crear (1-100)
rango_carpetas = (500, 519)

# Rango de imágenes que quieres copiar (200-300)
rango_imagenes = (490, 632)

# Directorio destino donde se crearán las carpetas y se copiarán las imágenes
directorio_destino = "C:\\tuDirectorioDestino\\ruta"

# Directorio origen donde se encuentran las imágenes
directorio_imagenes_origen = "C:\\tuDirectorioOrigen\\ruta"

# Llamada a la función
crear_carpetas_y_copiar_imagenes(rango_carpetas, rango_imagenes, directorio_destino, directorio_imagenes_origen)
