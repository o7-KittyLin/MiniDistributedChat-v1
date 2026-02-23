📄 **Estructura basada en:**  
La guía para crear READMEs profesionales de DevXP (https://github.com/Organization-DevXP/Guia-para-crear-READMEs-Profesionales)

# MiniDistributedChat v1 💬🌐

## Descripción
MiniDistributedChat v1 es una aplicación de chat distribuido desarrollada en **Python**, que permite la comunicación en tiempo real entre múltiples clientes conectados a través de una red LAN utilizando sockets TCP.

El sistema implementa un servidor concurrente basado en threading, capaz de manejar múltiples conexiones simultáneamente, mantener estado compartido y gestionar un protocolo de comunicación estructurado.

Este proyecto corresponde a la Parte 2 — Implementación de la materia *Sistemas Distribuidos*.

## 🚀 ¿Qué encontrarás aquí?
* **Servidor concurrente:** implementación usando `threading`.
* **Protocolo de comandos estructurado:**
  * `JOIN <nombre>`
  * `MSG <texto>`
  * `EXIT`
* **Estado compartido:**
  * Lista de clientes conectados.
  * Lista de nombres activos.
* **Sistema de broadcast:** los mensajes se reenvían a todos los clientes conectados.
* **Manejo de fallos:** soporte para desconexiones inesperadas sin que el servidor se detenga.
* **Prueba funcional real:** ejecución en dos computadores conectados por red LAN.

## 🎯 Objetivo
Desarrollar un sistema de comunicación distribuido que cumpla con los siguientes requerimientos obligatorios:
* Aceptar múltiples clientes simultáneamente.
* Implementar un protocolo estructurado de comandos.
* Mantener un estado compartido consistente.
* Reenviar mensajes a todos los clientes conectados.
* Soportar fallos y desconexiones sin que el servidor se detenga.
* Validar funcionamiento en entorno real de red local.

## 👩‍💻 ¿A quién está dirigido?
* Estudiantes de redes o sistemas distribuidos.
* Desarrolladores que desean comprender la comunicación cliente-servidor con sockets.
* Personas interesadas en implementar servidores concurrentes en Python.

## 📂 Estructura del Proyecto
```
MiniDistributedChat/
│
├── client.py     # Cliente TCP interactivo
├── server.py     # Servidor concurrente
└── README.md
```

# ⚙️ Instalación
## 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/MiniDistributedChat.git
```

Luego entra al proyecto:

```bash
cd MiniDistributedChat
```

## 2️⃣ Verificar Python
Este proyecto requiere **Python 3.8 o superior**.

Verifica tu versión:

```bash
python --version
```

Si no lo tienes instalado, descárgalo desde:
[https://www.python.org/downloads/]

# 🖥️ Configuración de Red (MUY IMPORTANTE) 🌐
El servidor utiliza:

```
HOST = "0.0.0.0"
PUERTO = 5000
```

Esto significa que escucha en **todas las interfaces de red** del computador.

Para que los clientes se conecten correctamente:

1. Ejecuta el servidor.
2. Obtén la IP local del servidor.

### Windows

```bash
ipconfig
```

### Linux / Mac

```bash
ifconfig
```

Busca la dirección IPv4, por ejemplo:

```
192.168.1.15
```

## 🔧 Configurar el cliente

En `client.py`, debes colocar la IP LAN del servidor:

```
HOST = "192.168.1.15"
PUERTO = 5000
```

⚠️ **NOTA:** Si no cambias la IP por la del servidor real, el cliente no podrá conectarse.


# ▶️ Instrucciones de Ejecución 🚀
## 1️⃣ Ejecutar el servidor
En el computador que actuará como servidor:

```bash
python server.py
```

El servidor comenzará a aceptar múltiples conexiones simultáneamente.

## 2️⃣ Ejecutar el cliente
En el mismo computador o en otro conectado a la misma red LAN:

```bash
python client.py
```
- Ingresa tu nombre cuando lo solicite.
- Puedes ejecutar varios clientes al mismo tiempo.

# 📜 Protocolo de Comunicación
El sistema implementa el siguiente protocolo obligatorio:

## 🔹 Unirse al chat
```
JOIN <nombre>
```

Ejemplo:

```
JOIN Carlos
```

## 🔹 Enviar mensaje
```
MSG <texto>
```

Ejemplo:

```
MSG Hola a todos
```

## 🔹 Salir del chat
```
EXIT
```


# 🧠 Funcionamiento Interno
El servidor:
* Crea un hilo nuevo por cada cliente conectado 🧵
* Mantiene una lista compartida de clientes activos
* Gestiona nombres únicos asociados a cada conexión
* Reenvía mensajes a todos los clientes excepto al emisor 📢
* Detecta desconexiones inesperadas y limpia recursos automáticamente
* Continúa funcionando aunque un cliente falle 🛡️

# 🌐 Prueba en Red LAN
Para cumplir el requerimiento obligatorio:
1. Ejecuta el servidor en el Computador A.
2. Obtén su IP local.
3. Desde el Computador B (misma red WiFi o LAN), ejecuta el cliente.
4. Conéctate usando la IP real del servidor.
5. Verifica envío y recepción de mensajes en tiempo real.

- Validación realizada en entorno real de red local.
- Soporte para múltiples clientes simultáneos.

# ✅ Estado del Proyecto
* Servidor concurrente funcional
* Protocolo estructurado implementado
* Broadcast operativo
* Manejo de fallos
* Prueba en red LAN completada

# 🎓 Conclusión
MiniDistributedChat v1 demuestra los fundamentos de:
* Comunicación cliente-servidor
* Concurrencia con hilos
* Manejo de estado compartido
* Implementación de protocolos de aplicación
* Sistemas distribuidos básicos

