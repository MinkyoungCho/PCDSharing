import socket
import time
import struct
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--port', default=8000, help='foo help')
parser.add_argument('--bw', default=10, help='foo help')
args = parser.parse_args()

lidar_frequency = 1 # LiDAR sweeps at 10 Hz 

HOST = "141.212.108.156" # Server IP
PORT = int(args.port)
BW = int(args.bw)

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((HOST,PORT))

# file_name = "draco_1_pcd.drc" # when sending draco compressed PCD
file_name = "shared_pcd.npy" # when sending original PCD (without compression)

file_send = open(file_name,"rb")
content = file_send.read()
 
start_time = time.time()
for i in range(lidar_frequency):
    ret = soc.send(content) # returns the number of bytes sent

ack = soc.recv(1024).decode()
print (f"{BW} {(time.time() - start_time):.5f}") 

        
soc.close()


