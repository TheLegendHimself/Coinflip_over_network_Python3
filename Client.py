#------------------------------------------
#		Import socket & hashlib
import socket
import hashlib

#--------------------------------------------
#		Connect to partner
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 9997))
#print("connected")

#------------------------------------------
#		Choose own Secret and compute Hash
valueB = int(input("Enter your number: "))
#print(hashlib.sha256(bytes(valueB)).hexdigest())

#------------------------------------------
#		Exchange Hash
s.send(bytes(hashlib.sha256(bytes(valueB)).hexdigest(),"utf-8"))
msg1 = s.recv(1024)
#print(msg1.decode("utf-8"))

#------------------------------------------
#		Receive Choice
msg3 = s.recv(1024)

#------------------------------------------
#		Exchange Secrets
s.send(bytes(str(valueB), "utf-8"))
msg2 = s.recv(1024)
#print(msg2.decode("utf-8"))

#------------------------------------------
#		Check partners Hash
if((msg1.decode("utf-8")) == hashlib.sha256(bytes(int(msg2.decode("utf-8")))).hexdigest()):
    print("Partners Hash looks good")

#------------------------------------------
#		Compute Hash from SecretA & SecretB
#msg4 = s.recv(1024)
result = hashlib.sha256()
result.update(bytes(valueB+int(msg2.decode("utf-8"))))

#------------------------------------------
#		Get Last Bit from hash
lastchar = str(result.hexdigest())[len(result.hexdigest())-2]
intlastchar = int(lastchar, 16)
#print("last hexvalue from hash as int: " + str(intlastchar))
result2 = intlastchar%2

#------------------------------------------
#		Check Choice And last bit
if((int(msg3.decode("utf-8")))!=result2):
	print("You won lol")
else:
	print("You lost :(")

#------------------------------------------