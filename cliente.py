import socket
import threading

Puerto = 12345

# Crea un socket TCP/IP para conectar al servidor 
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecte el socket a la direccion y puerto del servidor
cliente.connect(('127.0.0.1', Puerto))

def recibir_mensajes():
    """
    Función para manejar la recepción de mensajes del servidor.
    Escucha continuamente los mensajes entrantes del servidor y los 
    imprime en la consola
    """
    while True:
        try:
            # Recibe el mensaje del servidor
            mensaje = cliente.recv(1024).decode('utf-8')
            print(mensaje)
        except:
            # Maneja cualquier error que pueda ocurrir(por ejemplo desconexion del servidor )
            print("Conexión cerrada por el servidor.")
            break

# Inicia un hilo separado para gestionar la recepción de mensajes del servidor 
hilo_recepcion = threading.Thread(target=recibir_mensajes)
hilo_recepcion.start()

# Bucle principal para enviar mensaje al servidor
while True:
    # Mensaje de entrada del usuario
    mensaje_cliente = input("Tú: ")
    
    # Envía el mensaje al servidor
    cliente.send(mensaje_cliente.encode('utf-8'))