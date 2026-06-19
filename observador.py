import logging

class Observador_alta():
    def __init__(self):
        self.total_clientes=0

    def actualizar(self, cliente):
        logging.info(f"Nuevo cliente registrado: {cliente['dni']} - {cliente['nombre']} {cliente['apellido']}")

        self.total_clientes +=1
        logging.info(f"El cliente: {cliente['nombre']} {cliente['apellido']}, es el numero {self.total_clientes}")



