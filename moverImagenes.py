import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Selección del directorio raíz
root = tk.Tk()
root.withdraw()
selected_dir = filedialog.askdirectory(title="Selecciona el directorio raíz con subcarpetas de imágenes")

if not selected_dir:
    print("❌ No se seleccionó ninguna carpeta. Saliendo.")
    exit()

print(f"📂 Directorio seleccionado: {selected_dir}")

image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.avif')
moved_count = 0

# Recorre todas las carpetas y subcarpetas
for dirpath, dirnames, filenames in os.walk(selected_dir):
    if dirpath == selected_dir:
        continue  # Saltar el directorio raíz

    for filename in filenames:
        if filename.lower().endswith(image_extensions):
            original_path = os.path.join(dirpath, filename)
            base_name, ext = os.path.splitext(filename)

            # Evitar sobrescritura: crear un nombre único
            counter = 1
            new_name = filename
            new_path = os.path.join(selected_dir, new_name)
            while os.path.exists(new_path):
                new_name = f"{base_name}_{counter}{ext}"
                new_path = os.path.join(selected_dir, new_name)
                counter += 1

            shutil.move(original_path, new_path)
            print(f"✅ Movido: {filename} → {new_name}")
            moved_count += 1

print(f"\n🎉 Total de imágenes movidas: {moved_count}")
