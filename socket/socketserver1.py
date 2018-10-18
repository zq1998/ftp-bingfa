import  re
# ret=re.findall(r'(ad)+', 'add')
# ret=re.search(r'(ab)|\d','rabhdg8sd')
# ret=re.findall('www.(?:baidu|oldboy).com','www.oldboy.com')
# """
# obj=re.compile('\d{3}')
# ret=obj.search('abc123eeee')
# print(ret.group())
# """
import  socketserver
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("conn is",self.request)
        print("addr is",self.client_address)
        while True:
            try:
               data=self.request.recv(1024)
               print(data)
               self.request.sendall(data.upper())
            except Exception as err:
                print(err)
                break

if __name__=="__main__":
    s=socketserver.ThreadingTCPServer(("127.0.0.1",8006),MyServer) #多线程 多进程ForkingTCPServer
    s.serve_forever()

