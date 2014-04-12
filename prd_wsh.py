import json
import time
import random

# Open some file
# replace this bit to use a different data source
# to read from a low level terminal type input,
# check out https://docs.python.org/2/library/termios.html
f = open("sampleinput", 'r')
spd = int(f.readline())

# send in json format
msg = json.dumps({'spd':spd}) # note, redefined below

# a reset message would look like this
reset = json.dumps({'reset':True})

# required function for the websocket handler.
# can be used to validate connections:
def web_socket_do_extra_handshake(request):
	# if request.ws_origin == 'http://example.com':
    #	return
	pass

# handle the incoming client connections and send data
# we're not expecting any data from the clients.
def web_socket_transfer_data(request):
	# example receive code:
	# line = request.ws_stream.receive_message()
	while True:
		# for more interesting output, create a random number
		msg = json.dumps({'spd':random.randint(80,105)})
		request.ws_stream.send_message(msg, binary=False)
		time.sleep(5)
		if random.randint(1,16) == 1:
			request.ws_stream.send_message(reset, binary=False)
			time.sleep(5)
		# return from the while to end execution
