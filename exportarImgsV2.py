import os
import shutil

def distribuir_imagenes_en_carpetas(carpeta_inicial_origen, carpeta_inicial_destino, cantidad_carpetas_destino, directorio_destino, directorio_imagenes_origen):
    """
    Distribuye imágenes de un directorio a una cantidad específica de carpetas en el directorio destino.
    
    :param carpeta_inicial_origen: Carpeta inicial en el directorio origen donde se comenzará a buscar imágenes
    :param carpeta_inicial_destino: Carpeta inicial en el directorio destino donde se distribuirán las imágenes
    :param cantidad_carpetas_destino: Número de carpetas en el directorio destino para distribuir las imágenes
    :param directorio_destino: Ruta del directorio donde se encuentran las carpetas de destino
    :param directorio_imagenes_origen: Ruta del directorio donde se encuentran las imágenes
    
    :return: None
    """
    
    # Listar todas las carpetas en el directorio destino a partir de la carpeta inicial de destino
    carpeta_inicial_destino_num = int(carpeta_inicial_destino)
    carpetas_destino = [str(i) for i in range(carpeta_inicial_destino_num, carpeta_inicial_destino_num + cantidad_carpetas_destino)]
    
    # Verificar que las carpetas destino existen
    carpetas_destino_existentes = []
    for carpeta in carpetas_destino:
        carpeta_destino = os.path.join(directorio_destino, carpeta)
        if os.path.exists(carpeta_destino):
            carpetas_destino_existentes.append(carpeta_destino)
        else:
            print(f"La carpeta {carpeta_destino} no existe, no se moverán archivos ahí.")

    # Asegurarse de que hay carpetas suficientes para distribuir
    if len(carpetas_destino_existentes) < cantidad_carpetas_destino:
        print(f"Advertencia: Solo se encontraron {len(carpetas_destino_existentes)} carpetas disponibles.")
        cantidad_carpetas_destino = len(carpetas_destino_existentes)

    # Listar todas las carpetas en el directorio origen a partir de la carpeta inicial de origen
    carpeta_inicial_origen_num = int(carpeta_inicial_origen)
    for i in range(carpeta_inicial_origen_num, carpeta_inicial_origen_num + cantidad_carpetas_destino):
        carpeta_imagen_origen = os.path.join(directorio_imagenes_origen, str(i))
        
        if os.path.exists(carpeta_imagen_origen):
            # Verificar si la carpeta tiene imágenes, omitirla si está vacía
            imagenes = [img for img in os.listdir(carpeta_imagen_origen) if os.path.isfile(os.path.join(carpeta_imagen_origen, img))]
            
            if imagenes:  # Solo si la carpeta tiene imágenes
                for imagen in imagenes:
                    # Determinar en qué carpeta de destino se pegará la imagen (distribuir por cantidad de carpetas)
                    index_destino = (i - carpeta_inicial_origen_num) % cantidad_carpetas_destino
                    carpeta_destino = carpetas_destino_existentes[index_destino]
                    
                    # Copiar la imagen a la carpeta de destino
                    destino_imagen = os.path.join(carpeta_destino, imagen)
                    shutil.copy(os.path.join(carpeta_imagen_origen, imagen), destino_imagen)
                    print(f"Imagen {imagen} copiada a {carpeta_destino}")
            else:
                print(f"La carpeta {carpeta_imagen_origen} está vacía, se omite.")
        else:
            print(f"No se encontró la carpeta de origen {carpeta_imagen_origen}.")
    
    print("Proceso completado.")

# Carpeta inicial en el directorio origen (por ejemplo, "500")
carpeta_inicial_origen = "2664"

# Carpeta inicial en el directorio destino (por ejemplo, "500")
carpeta_inicial_destino = "2848"

# Número de carpetas destino a las que quieres distribuir las imágenes (20 en este caso)
cantidad_carpetas_destino = 24

# Directorio destino donde se encuentran las carpetas existentes
directorio_destino = "C:\\tuDirectorioDestino\\ruta"

# Directorio origen donde se encuentran las imágenes
directorio_imagenes_origen = "C:\\tuDirectorioOrigen\\ruta"

# Llamada a la función
distribuir_imagenes_en_carpetas(carpeta_inicial_origen, carpeta_inicial_destino, cantidad_carpetas_destino, directorio_destino, directorio_imagenes_origen)
