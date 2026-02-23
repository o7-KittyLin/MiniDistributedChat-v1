import socket
import threading

# 1. Crear socket del cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Dirección del servidor
HOST = "20.20.1.128" # Se pone la ip del servidor :)
PUERTO = 5000

# jp 10.225.127.65

# 3. Conectarse al servidor
cliente.connect((HOST, PUERTO))

# 4. Pedir nombre y enviar JOIN
nombre = input("(ɔ◔‿◔)ɔ  Nombre: ")
cliente.send(f"JOIN {nombre}".encode())

# 5. Función para recibir mensajes
def recibir():
    while True:
        try:
            mensaje = cliente.recv(1024).decode()
            if not mensaje:
                break
            print("\n" + mensaje)
        except:
            # Manejo de desconexión
            print("\n(¬⤙¬ ) Desconectado del servidor.")
            break

# 6. Iniciar hilo para recibir
threading.Thread(target=recibir, daemon=True).start()

# 7. Enviar mensajes
while True:
    texto = input()
    if texto.upper() == "EXIT":
        cliente.send("EXIT".encode())
        break
    cliente.send(f"MSG {texto}".encode())

# 8. Cerrar conexión
cliente.close()