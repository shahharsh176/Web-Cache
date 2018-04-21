from LFU import *
import socket
import sys
import thread
import time
import os
import pickle


cache = LFUCache(3);
hit = 0
miss = 0

def cache_fn(messageString, client_socket):
    
    HttpTypeMethod = messageString[0]
    URLpath = messageString[1]
    URLpath = URLpath[1:]
    print "--------------------------------------------------"
    print "Request is ", HttpTypeMethod, " to URL : ", URLpath
    print "--------------------------------------------------"
    start = time.clock()	
    current_file = "/" + URLpath
    try:
        #Search and open the current cache file for the URL entered
        file = open(current_file[1:], "r")
        contents = file.readlines()
        print "Match found in cache and reading the file\n"
        global hit
        hit += 1.0
        print "Hit-ratio: ",float(hit/(hit+miss))
        cache.insertItem(URLpath)
        print_cache(cache)
        for i in range(0, len(contents)):
            client_socket.send(contents[i])
        print "The above is the file read from Cache\n", "Time taken to read from Cache:",time.clock() - start , " Secs"
    
    except IOError:
        start = time.clock()
        print "Cache File not Found\n File is being fetched from Server to Create Cache\n"
        global miss
        miss += 1.0
        print "Hit-ratio: ",float(hit/(hit+miss))
        Proxy_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host_url = URLpath
        try:
            Proxy_server.connect((host_url, 80))
            cache.insertItem(URLpath)
            save_object(cache)
            print_cache(cache)
            print "Socket Connected on default Port 80 to fetch"
            ser_cache_file = Proxy_server.makefile('r', 0)
            ser_cache_file.write("GET " + "http://" + URLpath + " HTTP/1.0\n\n")           
            br = ser_cache_file.readlines()
            temp = open("./" + URLpath, "wb")
            for i in range(0, len(br)):
                temp.write(br[i])
                client_socket.send(br[i])
        except:
            print "Not Valid URL"
        print "Time taken to read from Server:",time.clock() - start," Secs"
    client_socket.close()

def save_object(obj):
    try:
        os.remove('cache.pkl')
        # print("try save")
    except:
        print "Creating cache file"
        # print("except save")
    with open('cache.pkl', 'wb') as output:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def main():
	if len(sys.argv) <= 1: 
    		print "Please specify (valid) port number."
    		sys.exit(2)
	try:
		global cache
		with open('cache.pkl', 'rb') as input:
			cache = pickle.load(input)
		print_cache(cache)
		# print("try main")
	except:
		print "Cache file doesn't exist. It will be created later"
	print "*********Computer Networks Project**********\n*******Web Cache/Proxy Implementation*******\n"
	port_server = int(sys.argv[1]) 
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Prepare a server socket
	print "Server is started"
	server_socket.bind(('', port_server))
	server_socket.listen(5)
	while True:
			print "Bind Successful"
			print "Connection Accepted"
			print "-------------------------------------"
			client_socket, addr = server_socket.accept() 
			print "Received Connection from <Host,Port> ", addr
			message = client_socket.recv(1024)
            # print message
			messageString = message.split()
			if len(messageString) <= 1:
				continue		
			thread.start_new_thread(cache_fn ,(messageString, client_socket))

if __name__ == '__main__':
	main()
