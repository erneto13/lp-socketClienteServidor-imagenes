import socket

HOST = '192.168.100.10'
PORT = 8000
RUTA_GUARDADO = 'imagen_recibida.jpg'  # Donde se guardará la img
TAMANIO_BUFFER = 1024

# Crear un socket del servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Vincular el socket al host y puerto
    server_socket.bind((HOST, PORT))
    
    # Socket en modo escucha para el cliente
    server_socket.listen()
    
    print(f"Esperando conexiones en {HOST}:{PORT}...")
    
    # Acepta la conexión del cliente
    client_socket, client_address = server_socket.accept()
    print(f"Conexión entrante desde {client_address}")
    
    # Abrir el archivo para escritura binaria
    with open(RUTA_GUARDADO, 'wb') as file:
        while True:
            image_data = client_socket.recv(TAMANIO_BUFFER)
            if not image_data:
                break
            file.write(image_data)
    
    print("Imagen recibida y guardada como 'imagen_recibida.jpg'")
    
    # Se cierra el socket
    client_socket.close()
