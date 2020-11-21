import subprocess, os, sys

if os.name == 'nt':
    print 'This is a Windows PC, dumping the Wifi passwords.'
    a = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    a = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]
    for i in a:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).split('\n')
        command = 'netsh wlan show profile "' + str(i) + '" key=clear'
        os.system(command)
else:
    print 'Sorry, this program is only for Windows OS'
    sys.exit()
    
 


            
