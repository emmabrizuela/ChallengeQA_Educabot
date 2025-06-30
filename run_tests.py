
import os
import subprocess
import sys

def main():
    # Verificar si estamos en un entorno virtual
    if sys.prefix == sys.base_prefix:
        print("No estás en un entorno virtual. Recomendado: crear y activar uno.")

    # Crear carpetas necesarias
    os.makedirs("reports", exist_ok=True)
    os.makedirs("screenshots", exist_ok=True)

    # Ejecutar Pytest con reporte HTML
    print("Ejecutando pruebas...")
    result = subprocess.run(["pytest", "--html=reports/reporte.html"], text=True)

    # Verificar resultado
    if result.returncode == 0:
        print("Pruebas completadas exitosamente.")
    else:
        print("Algunas pruebas fallaron. Verifica el reporte en reports/reporte.html")

if __name__ == "__main__":
    main()
