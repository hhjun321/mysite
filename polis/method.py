from paramiko.client import SSHClient
import paramiko
import os
import time
import numpy as np  
import cv2  

def shutdown(host):
    print('start Method')
    
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    #client.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host,username='han',password='93115')
    time.sleep(5)
    txt = 'C:/Users/BvSsh_VirtualUsers/Documents/out.lnk'
    time.sleep(1)
    
    print(txt)
    stdin, stdout, stderr = client.exec_command(txt)
    print(stdout.read())
   
def pingChk(host):
    print("ping")
    response = os.system("ping -c 5 " + host)
    print(response)
    return response
	
	
def openCam():
    capture = cv2.VideoCapture(0)  
    #print 'image width %d' % capture.get(3)  
    #print 'image height %d' % capture.get(4)  
      
    capture.set(3, 320)  
    capture.set(4, 240)  
      
      
    while(1):  
        ret,frame = capture.read()  
      
        cv2.imshow( 'webcam', frame )  
      
        if cv2.waitKey(1)&0xFF == ord('q'):  
            break;  
      
      
    capture.release()  
    cv2.destroyAllWindows()  