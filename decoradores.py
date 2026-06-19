import logging


def Registro_log(func):
    def wrapper(*args):
        logging.info(f"Ejecutando {func.__name__} con args={args}")
        try:
            resultado = func(*args)
            logging.info(f"{func.__name__} devolvió {resultado}")
            return resultado
        except Exception as e:
            logging.error(f"Error en {func.__name__}: {e}")
            raise
    return wrapper