# Server example:
from threading import Thread
import socket, pickle, logging

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 12354))

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(lineno)s %(message)s', level=logging.DEBUG)                                                                 
client_list = []
max_clients = 2 
global started  
started = 0                                                                                                                                                         

class Client():
    def __init__(self, conn = ''):

        self.conn = conn
        # add to global clients list
        client_list.append(self)                             
        self.client_thread = Thread(target = self.process_messages)
        self.client_thread.start()


    def process_messages(self):                                                                                                                                     
        while True:
            try:
                data = self.conn.recv(1024)
                # send to all in client_list except self                                     
                data = pickle.loads(data)                                                                                                                               
                data.append(started)                                                                                                                                    
                logging.info("Sending Data: {0}".format(data))
                data = pickle.dumps(data)
                for client in client_list:
                    if client != self:                                                                                                                                 
                        client.conn.sendall(data)                                                                                                                           
                data = ""
            except ConnectionResetError:
                logging.debug("Client Disconnected")
                break


def connection_manager():
    while len(client_list) < max_clients:
        logging.info('Listening for connections...')
        s.listen(1)
        conn, addr = s.accept()
        logging.info("Client connected: {0}".format(addr))
        x = Client(conn)
        logging.debug(client_list)
    logging.warning("Max clients reached")
    logging.info("No longer listening..")
    started = 0

accept_connections_thread = Thread(target = connection_manager)
accept_connections_thread.start()