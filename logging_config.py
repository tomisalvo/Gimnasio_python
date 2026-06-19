import logging
from pathlib import Path

# Guardado en archivo accesos.log
def configurar_logging():
    log_file = Path(__file__).parent / "registros.log" #creamos el archivo en la misma carpeta que la app

    logging.basicConfig(
        filename=log_file,       # archivo registro de accesos
        level=logging.INFO,           # nivel de registro: Informacion (nivel minico)
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # Agregar salida en consola
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)