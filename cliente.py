import socket

cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente.connect((socket.gethostname(),1234))
# Se envia como byte,se recibe como byte,se maneja todo con byte
"""Recibir mensaje de bienvenida"""
mensaje = cliente.recv(1024)
print("Servidor dice:",mensaje.decode("utf-8"))
# Enviar respuesta
cliente.send(bytes("Gracia por aceptarme,servidor", "utf-8"))

# Esperar respuesta del servidor (si decide enviar algo más)

respuesta = cliente.recv(1024)
print("Servidor respondido:", respuesta.decode("utf-8"))

cliente.close()