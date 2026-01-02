import socket

HOST = "127.0.0.1"
PORT = 8080

def start_proxy():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[+] Proxy listening on {HOST}:{PORT}")

    while True:
        client, addr = server.accept()
        print(f"[+] Connection from {addr}")
        client.close()

if __name__ == "__main__":
    start_proxy()
