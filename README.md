# Wi-Fi Deauthentication Attack

this code will make wifi deauthentication attack.

# short brief:

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

in order to run the code you need to do the next steps:

1. sudo -i.
2. chmod a+x wifiAttack.py.
3. ./wifiAttack.py 'wifi adapter name'





















