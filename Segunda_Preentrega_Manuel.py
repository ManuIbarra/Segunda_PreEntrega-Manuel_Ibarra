import os
import tarfile

class Cliente:
    def __init__(self, id_cliente, nombre, correo, direccion):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion

    def obtener_info(self):
        return f"ID: {self.id_cliente}, Nombre: {self.nombre}, Correo: {self.correo}, Dirección: {self.direccion}"

    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion

    def __str__(self):
        return f"Cliente: {self.nombre}"

def main():
    id_actual = 1
    while True:
        nombre = input("Ingresa el nombre del cliente: ")
        correo = input("Ingresa el correo electrónico: ")
        direccion = input("Ingresa la dirección: ")

        cliente = Cliente(id_actual, nombre, correo, direccion)

        with open("clientes.txt", "a") as archivo:
            archivo.write(cliente.obtener_info() + "\n")

        print(cliente.obtener_info())

        print(cliente)

        id_actual += 1

        respuesta = input("¿Desea agregar otro cliente? (Si/No): ")

        if respuesta.lower() != "si":
            break

def make_tar_gz(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

main()

output_filename = "clientes.tar.gz"
source_dir = "."

make_tar_gz(output_filename, source_dir)
