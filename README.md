# Wi-Fi Deauthentication Attack
this code will make wifi deauthentication attack.

short brief:

the code was written in python 3.6.
in order to run the code you need to work with linux (vm will probably not work because there is some issues with the monitor mode),
and have wifi adapter card
and then turn the computer into monitor mode .
you also need scapy install in your pc, and air-crack-ng.
because we use prettytable you need to install prettytable with the commend : sudo pip3 install PTable.
you can do this opperations(monitor mode) with the next commends:

1. sudo ifconfig IFACE down
2. sudo iwconfig IFACE mode monitor
3. sudo ifconfig IFACE up

where IFACE is your wifi adapter card name, you can find his name and then know
if you on monitor mode with the commend : iwconfig.

run the code :

in order to run the code you need to do the next steps:

1. sudo -i.
2. chmod a+x wifiAttack.py.
3. ./wifiAttack.py 'wifi adapter name'

inside the code:

when the code will run you will see the list of ap in your area (that will take 10 seconds, you can change that in the scapy filter).
then you need to choose the SSID mac,and then the SSID name and finaly the mac of the victim.
after this opperations the attack will start with no time limit, you can stop the attack by 
pressing ctrl-c .
the code use scapy libary in python for the sniffing operation, and aireplay-ng.




















