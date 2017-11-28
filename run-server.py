import subprocess
import socket
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
s = socket.gethostbyname(socket.gethostname())
if( s == "127.0.0.1" ):
    s = socket.getfqdn()
msg = "Hello, the new server ip is:       " + s
 
arr = [ "6035715222@txt.att.net", "6035532414@txt.att.net", "6039656041@vtext.com", "6033622083@vtext.com" ]

fromaddr = "i.promise.im.not.a.virus@gmail.com"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()	
server.login(fromaddr, "itsnevernottimetofast")

for address in arr:
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = address
	msg['Subject'] = "Server ip"
	body = "The live server ip is:   " + s + ":25565"
	msg.attach(MIMEText(body, 'plain'))
	 
	
	text = msg.as_string()
	server.sendmail(fromaddr, address, text)
server.quit()


subprocess.Popen("runable.bat", creationflags=subprocess.CREATE_NEW_CONSOLE)

