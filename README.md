# usermgmt
Manage user Account in Linux
This repositary is going to help AddUser, ModifyUser and DelUser in Linux only.

Step1 : clone git repo either of way you feel compfort. 
        git clone https://github.com/Sadashiv/usermgmt
        or
        git clone git@github.com:Sadashiv/usermgmt  

step2 : cd usermgmt/
        Install customized python
        ./installpy.sh -s
        Once above command execution success
        check python installed in the current working directory
        ./usr/bin/python

Step3 : ./usr/bin/python manage.py migrate
        ./usr/bin/python manage.py makemigrations
        
step4 : ./usr/bin/python manage.py runserver
         Note : Default port is going to be 8000
         
         Try to access below url in browser
         http://localhost:8000/home

         Run with cutomized port say xxxx
	 ./usr/bin/python manage.py runserver xxxx

         If it's not able to access into other machine
	 ./usr/bin/python manage.py runserver 0.0.0.0:xxxx
         
