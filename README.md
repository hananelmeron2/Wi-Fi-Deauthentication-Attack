# Wi-Fi Deauthentication Attack

this code will make wifi deauthentication attack.

# working environment:

the code was written in python 3.6.

# prerequest

wifi adapter card.
airmon-ng , (aircrcak-ng,).
scapy.
prettytable.

monitor mode :

1. sudo ifconfig IFACE down
2. sudo iwconfig IFACE mode monitor
3. sudo ifconfig IFACE up

where IFACE is your wifi adapter card name.

#run the code

1. sudo -i.
2. chmod a+x wifiAttack.py.
3. ./wifiAttack.py 'wifi adapter name'

# usage
base operation for more complicated attacks like mitm, evil twin, wifi passwords cracker and more..
in the future the code will include  base gui.



























