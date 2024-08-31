from http import client
from pydoc import classify_class_attrs
import socket


def text_splitter(input_text: str):
    new_text=input_text.split("{")
    new_text = new_text[1]
    

def start_server(host: str ='127.0.0.1',port: int= 6000):
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host,port))
    server_socket.listen()
    print(f'listening on {host}:{port}')


    while True:
        print('Waiting for a connection:')
        client_socket , client_address = server_socket.accept()
        print(f"connection from{client_socket}:{client_address}")
        try:
            while True:
                data=client_socket.recv(2048)
                if data:
                    print(f'{data.decode("utf-8")}')
                    text_splitter(data.decode("utf-8"))
                else:
                    print(f"client {client_address} dicsonnected")
                    break
        finally:
            client_socket.close()



if __name__ == "__main__" :
    start_server()

