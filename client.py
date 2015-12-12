import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = raw_input("IP-Adresse: ")
nachricht = raw_input("Nachricht: ")

s.sendto(nachricht, (ip, 5000))
s.close()
