# coding:utf-8
import socket
import csconf
import thread
import sys

def paddingid(id):
    id_padded = id+'\0'*(csconf.maxidlen - len(id))
    return id_padded

class Client:
    def __init__(self,id):
        if len(id) > csconf.maxidlen:
            raise Exception('id too long')
        self.id = paddingid(id)
        self.socket = socket.socket()
    def login(self):
        self.socket.connect((csconf.servername,csconf.port))
        self.socket.send(self.id)
    def send_msg(self,userto,msg):
        if(len(msg)>0):
            self.socket.send(userto+msg)
    def real_loop_recv(self):
        while True:
            msg = self.socket.recv(csconf.maxmsglen)
            print msg
            if msg=='':# means closed at server
                self.socket.close()
                import os
                os._exit(-1)
    def start_recv(self):    
        thread.start_new_thread(self.real_loop_recv, ())
    def start(self):
        self.start_recv();
        while True:
            line = sys.stdin.readline()
            self.send_msg(line[0:10],line[10:])
        
        
if __name__=='__main__':
    userid = ''
    helpinfo = 'input userid please'
    if len(sys.argv)<2:
        print helpinfo
        raise Exception(helpinfo)
    userid = sys.argv[1]
    client = Client(userid)
    client.login()
    client.start()