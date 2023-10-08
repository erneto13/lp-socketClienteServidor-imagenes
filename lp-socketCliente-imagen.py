import socket

HOST = '192.168.100.10'  
PORT = 8000

RUTA_IMG = r'C:\Users\Ernesto Amaral\Desktop\amlo_pelon.jpg'  # Ruta de la donde esta la img
TAMANIO_BUFFER = 1024  # Tamaño del búfer

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    with open(RUTA_IMG, 'rb') as file:
        while True:
            image_data = file.read(TAMANIO_BUFFER)
            if not image_data:
                break
            s.sendall(image_data)

print('Imagen enviada desde el cliente')