import os
import re
import tkinter as tk
from tkinter import filedialog

# Mostrar selector de carpetas
root = tk.Tk()
root.withdraw()
selected_dir = filedialog.askdirectory(title="Selecciona el directorio raíz que contiene carpetas numeradas")

if not selected_dir:
    print("❌ No se seleccionó ninguna carpeta. Saliendo.")
    exit()

print(f"📂 Directorio seleccionado: {selected_dir}")

image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.avif')

# Obtener solo carpetas con nombre numérico
numeric_folders = [f for f in os.listdir(selected_dir)
                   if os.path.isdir(os.path.join(selected_dir, f)) and re.fullmatch(r'\d+', f)]

total_folders = len(numeric_folders)
print(f"🔍 Se encontraron {total_folders} carpetas numeradas.")

for idx, folder_name in enumerate(sorted(numeric_folders), start=1):
    folder_path = os.path.join(selected_dir, folder_name)
    print(f"\n📁 Procesando carpeta {idx}/{total_folders}: {folder_name}")

    try:
        image_files = [f for f in os.listdir(folder_path)
                       if f.lower().endswith(image_extensions) and os.path.isfile(os.path.join(folder_path, f))]
        
        if not image_files:
            print("   ⚠️  No se encontraron imágenes.")
            continue

        image_files.sort()
        for i, filename in enumerate(image_files, start=1):
            _, ext = os.path.splitext(filename)
            new_name = f"{folder_name}-{i}{ext}"
            src = os.path.join(folder_path, filename)
            dst = os.path.join(folder_path, new_name)

            if os.path.exists(dst):
                print(f"   ⚠️  Ya existe {new_name}, saltando...")
                continue

            os.rename(src, dst)
            print(f"   ✅ Renombrado: {filename} → {new_name}")
    
    except Exception as e:
        print(f"   ❌ Error al procesar {folder_name}: {e}")
