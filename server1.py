import socket
import threading

Puerto_servidor = 12345

# Crea un socket TCP/IP para escuchar conexiones entrantes
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincula el socket al host local y a un puerto entrante
server.bind(('127.0.0.1', Puerto_servidor))

# Escuchar conexiones entrantes (la cantidad máxima de conexiones pendientes)
server.listen()

# Lista para realizar un seguimiento de los clientes conectados 
clientela = []

def manejar_cliente(cliente_socket):
    """
    Función para gestionar la comunicacion con un cliente conectado.
    Escucha los mensajes entrantes del cliente y los transmite 
    el mensaje a todos los demas clientes conectados 
    """
    while True:
        try:
            # Recibir mensaje del cliente
            mensaje_cliente = cliente_socket.recv(1024).decode('utf-8')
            
            # Transmite el mensaje a todos los demas clientes
            for cliente in clientela:
                if cliente != cliente_socket:
                    cliente.send(mensaje_cliente.encode('utf-8'))
        except:
            # Maneja la desconexion del cliente y elimina el cliente de la lista
            clientela.remove(cliente_socket)
            cliente_socket.close()
            break

# Bucle principal para aceptar conexiones entrantes de cliente
while True:
    print("El servidor esta escuchando conexiones...")
    
    # Acepta una nueva conexion del cliente
    cliente, addr = server.accept()
    
    # Agrega un nuevo cliente a la lista de clientes conectados
    clientela.append(cliente)
    
    print(f"Nueva conexión desde {addr}")
    
    # Inicia un nuevo hilo para manejar la comunicación con el cliente conectado 
    client_handler = threading.Thread(target=manejar_cliente, args=(cliente,))
    client_handler.start()