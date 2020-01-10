#------------------------------------------
#		Import Hashlib & socket
import hashlib as hl
import socket

#------------------------------------------
#		Set Hashfunctions to SHA-256
first = hl.sha256()
second = hl.sha256()
third = hl.sha256()

#-------------------------------------------
#		Connect to other person
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9997 ))
s.listen(1)

clientsocket, address = s.accept()
print("Connection accepted")

#--------------------------------------------
#		Choose own Secret and compute Hash
print("Choose your Secret Number: ")
secretA = int(input())
first.update(bytes(secretA))

#--------------------------------------------
#		Exchange Hash
clientsocket.send(bytes(first.hexdigest(), "utf-8"))
secretBHash = clientsocket.recv(1024)

#--------------------------------------------
#		Choose Heads or Tails
choice = -1
while(choice != 0 and choice != 1):
    choice=int(input("Choose Heads(1) or Tails(0): "))

    if(choice == 0):
        print("You chose Tails")

    if(choice == 1):
        print("You chose Heads")

#--------------------------------------------
#		Send your Choice
clientsocket.send(bytes(str(choice), "utf-8"))

#--------------------------------------------
#		Exchange of Secrets
clientsocket.send(bytes(str(secretA), "utf-8"))
secretB = clientsocket.recv(1024)

#---------------------------------------------
#		Check his Hash & Input
second.update(bytes(int(secretB.decode("utf-8"))))
#print(hl.sha256(bytes(secretB)).hexdigest())
if(secretBHash.decode("utf-8") == (second.hexdigest())):
    print("hash from partner is valid")
else:
    print("hash from partner is invalid" )
	
#----------------------------------------------
#		Compute Hash from SecretA & SecretB
print("Now compute Heads or Tails")
third.update(bytes(int(secretB.decode("utf-8"))+secretA))
#clientsocket.send(bytes(third.hexdigest(), "utf-8"))

#----------------------------------------------
#		Get last Bit of hash
lastchar = str(third.hexdigest())[len(third.hexdigest())-2]
intlastchar = int(lastchar, 16)
#print("last hexvalue from hash as int: " + str(intlastchar))
result = intlastchar%2

#----------------------------------------------
#		Compare Result and Choice
if(choice == result):
    print("Congrats you Won")
else:
    print("You lost ... ")

#----------------------------------------------
#		Beenden
exit(0)

#----------------------------------------------
