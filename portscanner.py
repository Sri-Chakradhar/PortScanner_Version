import socket

def scan(target,ports):
	print("\n"+"Starting Scan for " + str(target)
	for port in  range(1,ports):
		scanning_port(target,port)

def scanning_port(ip,port):
	try:
		socke =  socket.socket()
		socke.connect((ip,port))
		print("[+] port opened "+ str(port))
		socke.close()
	except:
		pass

targets = input("[#] Enter your targets ip(split by ','): ")
ports = int(input("[#] Enter how many target ports to scan: "))

if ',' in targets:
	print("[()]Multple targets ")
	for ip in targets.split(','):
		scan(ip.strip(' '),ports)
else:
	scan(targets,ports)
