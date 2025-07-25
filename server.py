'''Los sockets es solo el punto final que recibe datos, no es la comunicacion,
es solo el punto final que recibe esa comunicacion y ese punto final se encuentra en una IP y un puerto'''
import socket # biblioteca estandar
# LE estoy diciendo que quiero un socket del paquete socket
# En el () se especifica el tipo de socket, lo mas comun es el internet socket, l osegundo que se especifica si es orientado
# a conexion o sin TCP o UDP.
"""TCP es una conexion e intercambio de mensajes a traves de esa conexion """
"""UDP simplemente envio y recibo sin mantener una conexion"""
"""El tipo de familia de socket es AF_INET y el tipo real de socket es SOCK_STREAM"""
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Le paso la direccion de IP y el puerto 
server.bind((socket.gethostname(),1234))
# Permitimos 5 conexiones pendientes
server.listen(5)
"""Escuchamos conexiones para siempre"""
while True:
    #Se almacena el objeto externo de socket en la variable clientesocket
    # address es de donde viene osea su IP basicamente
    clientesocket,address = server.accept() # Esto es -> si alguien se conecta, nos vamos a conectar
    print(f"Conexion aceptada {address}")
    clientesocket.send(bytes("Bienvenido al servidor","utf-8"))
                                                    #Son bytes "utf-8"
    #Esperamos un mensaje de respuesta del cliente
    respuesta= clientesocket.recv(1024)
    print(f"Mensaje del cliente: {respuesta.decode('utf-8')}")
    # Respondemos al cliente con un eco
    clientesocket.send(bytes("Recibí tu mensaje","utf-8"))
    clientesocket.close()
    