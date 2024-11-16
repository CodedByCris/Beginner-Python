import socket

ip = input("Enter the IP address: ")

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} is open")
        s.close()
    else:
        print(f"Port {port} is closed")