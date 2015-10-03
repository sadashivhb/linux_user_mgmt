import os
import crypt
import logging
class Pwd(object):
    def userPasswd(self, login, password):
        encPass = crypt.crypt(password, password)
        command = "sudo usermod -p '{0:s}' {1:s}".format(encPass, login)
        result = os.system(command)
        if result != 0:
            logging.error(command)
        return result

pp = Pwd()
a = pp.userPasswd('sada', 'sad')

password = 'sada'
encpass = crypt.crypt(password, '22')

a= os.system("sudo useradd sada -p "+encpass+" -m -s /bin/bash")
a= os.system("sudo useradd sada -p "+encpass+" -m")
