import  hashlib
s=hashlib.md5()
s.update("1".encode("utf8"))
s.update("2".encode("utf8"))
print(s.hexdigest())