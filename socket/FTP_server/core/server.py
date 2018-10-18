
import  os,sys
import socketserver
import json
import configparser
from conf import  settings
class ServerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while 1:
            #conn=self.request
            data=self.request.recv(1024).strip()
            data=json.loads(data.decode("utf8"))

            if data.get("action"):
                if hasattr(self,data.get("action")):
                    func=getattr(self,data.get("action"))
                    func(**data)
                else:
                    print("Invald cmd")
            else:
              print("Invald cmd")
    def send_reponse(self,status_code):
        reponse={"status_code":status_code}#,
        self.request.sendall(json.dumps(reponse).encode("utf8"))
    def auth(self,**data):
        username=data.get("username")
        password=data.get("password")

        user=self.authenticate(username,password)
        if user:
            self.send_reponse(0)
        else:
            self.send_reponse(1)
    def authenticate(self,username,password):
        cfg=configparser.ConfigParser()
        cfg.read(settings.ACCOUNT_PATH)

        if username in cfg.sections():
            if cfg[username]["Password"]==password:
                self.user=username
                self.mainPath=os.path.join(settings.BASE_DIR,"home",self.user)
                print("passed")
                return username


    def put(self,**data):
        print("data",data)
        file_name=data.get("file_name")
        file_size=data.get("file_size")
        target_path=data.get("target_path")
        abs_path=os.path.join(self.mainPath,target_path,file_name)
        has_received=0
        if os.path.exists(abs_path):
            file_has_size=os.stat(abs_path).st_size
            if file_has_size<file_size:
                self.request.sendall("4".encode("utf8"))
                choice=self.request.recv(1024).decode("utf8")
                if choice=="Y":
                    self.request.sendall(str(file_has_size).encode("utf8"))
                    has_received+=file_has_size
                    f = open(abs_path, "ab")
                else:
                    f = open(abs_path, "wb")
            else:
                self.request.sendall("3".encode("utf8"))
                return
        else:
            self.request.sendall("2".encode("utf8"))
            f = open(abs_path, "wb")


        while has_received<file_size:
            try:
               data=self.request.recv(1024)
            except Exception as err:
                break
            f.write(data)
            has_received+=len(data)
        f.close()


