# -*- coding:utf-8 -*
'''
Created on 2018-04-20

@author: llin4
'''
import socket
import thread
import csconf

class User(object):
    def __init__(self,id,socket,clients):
        self.id = id
        self.socket = socket
        self.all_clients = clients
    def forward(self,content):
        self.socket.send(content)
    def real_loop(self):
        while True:
            content = self.socket.recv(csconf.maxmsglen)
            print('recved: '+content)
            if content == '':
                self.socket.close()
                self.all_clients.pop(self.id)
                del self
                print(self.id + ' client has closed')
                break
            username_to = content[0:csconf.maxidlen]
            # username_to = username_to.strip('\0')
            if self.all_clients.has_key(username_to):
                user_to = self.all_clients[username_to]
                if len(content[csconf.maxidlen :])>0:
                    user_to.forward(content[csconf.maxidlen :])
    def start_loop(self):
        thread.start_new_thread(self.real_loop, ())
            
        
class CsServer(object):
    def __init__(self):
        self.clients = {}
        self.ssocket =  socket.socket()
        
    def start(self):
        import socket
        ip = socket.gethostname()
        if len(csconf.servername) > 0:
            ip = csconf.servername
        print(ip)
        self.ssocket.bind((ip, csconf.port))
        self.ssocket.listen(10);
        while True:
            socket,addr = self.ssocket.accept()
            loginid = socket.recv(csconf.maxidlen)
            if not self.clients.has_key(loginid):
                print(loginid+' login')
                user = User(loginid,socket,self.clients)
                self.clients[loginid] = user
                user.start_loop()
            else:
                errinfo = 'user'+loginid+' has logged in, close this socket'
                socket.send(errinfo)
                socket.shutdown(2)
                socket.close()
                print(errinfo)
    
"""used in server"""
def getmsg(localsocket):
    while True:
        msg = localsocket.recv(5000)
        print msg,

    
def startserver():
    s = socket.socket()
    host=socket.gethostname()
#     host="xxx"
    port=37777
    s.bind((host,port))
    s.listen(5)
    simsocket,addr=s.accept()
    getmsg(simsocket)
    print 'start new thread except'

if __name__== '__main__':
    csserver = CsServer()
    csserver.start()