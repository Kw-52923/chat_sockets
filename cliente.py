import socket
import threading
import os  # Solo si está permitido en tu challenge

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Puerto = 12345

# --- Reintenta la conexión hasta 3 veces ---
intentos = 0
max_intentos = 3
while intentos < max_intentos:
    try:
        cliente.connect(('127.0.0.1', Puerto))
        print(f" Conectado al servidor en el intento {intentos + 1}")
        break
    except:
        intentos += 1
        print(f"Fallo al conectar (intento {intentos}/{max_intentos})")

# Si después de 3 intentos no se conecta, se termina el programa
if intentos == max_intentos:
    print(" No se pudo conectar al servidor después de 3 intentos.")
    exit()

# --- Función para recibir mensajes del servidor ---
def recibir_mensajes():
    while True:
        try:
            mensaje = cliente.recv(1024).decode('utf-8')
            if not mensaje:
                print("\n Conexión cerrada por el servidor.")
                break
            print(mensaje)
        except:
            print("\n Error en la conexión con el servidor.")
            break
    cliente.close()
    os._exit(0)  # Solo si está permitido. Si no, usá `exit()` o `break`.

# --- Inicia un hilo para recibir mensajes ---
hilo_recepcion = threading.Thread(target=recibir_mensajes)
hilo_recepcion.start()

# --- Bucle principal de envío ---
while True:
    try:
        mensaje_cliente = input("Tú: ")
        if mensaje_cliente.lower() == "/exit":
            print(" Cerrando conexión...")
            cliente.close()
            break
        cliente.send(mensaje_cliente.encode('utf-8'))
    except:
        print(" No se pudo enviar el mensaje.")
        break
