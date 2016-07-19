#!/usr/bin/python
from scapy.all import *
from optparse import OptionParser

# A script to send a single IP packet using a
# specific VLAN e.g., if you want to send a packet
# to 10.0.0.1 using VLAN 10 on eth0, you could write:
# ./vlan.py -i eth0 -d 10.0.0.1 -v 10
#
# You can verify the reachability by using tcpdump on the other
# host, and verify that the packet has actually been received.
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-i", "--iface", dest="iface", default='eth0',
            help="Interface to use")
    parser.add_option("-d", "--dest", dest="ip", default='10.0.0.1',
            help="Destination IP")
    parser.add_option("-v", "--vlan", dest="vlan", default=1,
            help="VLAN")

    (options, args) = parser.parse_args()
    sendp(Ether()/Dot1Q(vlan=int(options.vlan))/IP(dst=options.ip), iface=options.iface)
