import shutil
import os

folder_path = r'C:\Users\IPS\.gemini\antigravity\scratch\smartlife-controller'
zip_name = 'smartlife_app'

# List of files/folders to include
to_include = ['backend', 'frontend', 'requirements.txt', 'Procfile', 'README_DEPLOY.md']

print("Creando archivo ZIP...")
shutil.make_archive(zip_name, 'zip', folder_path)

# If we want a cleaner zip (only specific files), we'd do it manually, 
# but for now, zipping the whole folder is safer to ensure nothing is missed.
print(f"¡Listo! Archivo {zip_name}.zip creado con éxito.")
