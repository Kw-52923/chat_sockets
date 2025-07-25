import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(("127.0.0.1",1234))
# Escuchar conexiones entrantes(la cantidad máxima de conexiones pendientes se establece de forma predeterminada)
server.listen()

while True:
    # Acepta conexiones entrantes.
    clientesocket,address = server.accept()
    
    print(f"Conexion aceptada {address}")
    # Envia mensaje de bienvenida
    clientesocket.send(bytes("Bienvenido al servidor","utf-8"))
    # Recibe una respuesta del cliente
    respuesta= clientesocket.recv(1024)
    print(f"Mensaje del cliente: {respuesta.decode('utf-8')}")
    # Envia una respuesta final y cierra la conexion 
    clientesocket.send(bytes("Recibí tu mensaje","utf-8"))
    clientesocket.close()