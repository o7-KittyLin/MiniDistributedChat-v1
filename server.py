import socket
import threading

# Crear socket del servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Dirección y puerto
HOST = "0.0.0.0"  # Todas las interfaces (LAN)
PUERTO = 5000

# Enlazar y escuchar
servidor.bind((HOST, PUERTO))
servidor.listen()
print(f"ᓚ₍⑅^..^₎♡ Servidor activo en {HOST}:{PUERTO}")

# Estado compartido
clientes = []
nombres = {}

# Broadcast simple
def broadcast(msg, remitente=None):
    for c in clientes:
        if c != remitente:
            try:
                c.send(msg.encode())
            except:
                clientes.remove(c)
                nombres.pop(c, None)
                c.close()

# Manejar un cliente
def manejar_cliente(cliente):
    while True:
        try:
            msg = cliente.recv(1024).decode()
            if not msg:
                break

            if msg.startswith("JOIN"):
                nombre = msg.split(" ", 1)[1]
                nombres[cliente] = nombre
                clientes.append(cliente)
                broadcast(f"(っˆ▿ˆ)☞  {nombre} se unió al chat ₍^. .^₎⟆")
                continue

            if msg.startswith("MSG"):
                texto = msg.split(" ", 1)[1]
                nombre = nombres.get(cliente, "(¬_¬) Desconocido")
                broadcast(f"{nombre}: {texto}", remitente=cliente)
                continue

            if msg.startswith("EXIT"):
                break

        except:
            break

    # Limpiar al desconectarse
    nombre = nombres.get(cliente, "( ╹ -╹)? Alguien")
    if cliente in clientes:
        clientes.remove(cliente)
    nombres.pop(cliente, None)
    broadcast(f"(˶°ㅁ°)!! {nombre} salió del chat.")
    cliente.close()
    print(f"(⇀‸↼‶) {nombre} se desconectó.")

# aceptar conexiones 
while True:
    cliente, addr = servidor.accept()
    print("Conexión recibida desde:", addr)
    threading.Thread(target=manejar_cliente, args=(cliente,), daemon=True).start()