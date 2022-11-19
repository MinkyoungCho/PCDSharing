import socket
import time

lidar_frequency = 1 # fix this to 1 to measure the delay for 1 point cloud frame
HOST = "" # Server IP
PORT = 8000

try:
    while True:

        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('[1] socked created. waiting for connecting to server...')

        soc.bind((HOST, PORT))
        soc.listen()
        print('[2] connected to the server.')

        print ("[3] waiting client..")
        con, addr = soc.accept()
        fragments = []

        for i in range(lidar_frequency):
            chunk = con.recv(40000)
            fragments.append(chunk)
                
        ret = con.send(str.encode("ACK from server"))
        if ret == 0:
            raise RuntimeError("socket connection broken")
        print ("[4] ACK is just sent to client..")

        PORT += 1
        con.close()
        soc.close()


except socket.error as err:
    print(f"{str(err)}")