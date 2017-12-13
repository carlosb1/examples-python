from scapy.all import *
packet = IP() / TCP() 
Ether() / packet

ls (IP, verbose=True)
print "tcp" 
ls (TCP, verbose=True)
p = Ether() / IP(dst="www.secdev.org") / TCP()
print p.summary()

print p.dst
print p[IP].src

print p.sprintf("%Ether.src% > %Ether.dst%\n%IP.src% > %IP.dst%)")


print p.sprintf("%TCP.flags% %TCP.dport%")

[p for p in IP(ttl=(1,5)) / ICMP()]


sr1(IP(dst="8.8.8.8")/UDP()/DNS(qd=DNSQR()))

#p[DNS].an

r, u = srp(Ether()/IP(dst='8.8.8.8', ttl=(5,10))/UDP()/DNS(rd=1, qd=DNSQR(qname="www.example.com")))
r, u

print r[0][0].summary()
print r[0][1].summary()

r[0][1][ICMP]

wrpcap("scapy.pcap",r)

pcap_p = rdpcap("scapy.pcap")
pcap_p[0]

s = sniff(count=2)
s

sniff(count=2, prn=lambda p: p.summary())

import socket
sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sck.connect(("8.8.8.8",53))

ssck = StreamSocket(sck)
ssck.basecls = DNS

ssck.sr1(DNS(rd=1,qd=DNSQR(qname='www.example.com')))


ans, unans = srloop(IP(dst=["8.8.8.8","8.8.4.4"])/ICMP(), inter=.1, timeout=.1, count=100, verbose=False)

ans.multiplot(lambda (x,y): (y[IP].src, (y.time, y[IP].id)),plot_xy=True)

pkt = IP() / UDP() / DNS(qd=DNSQR())

print repr(str(pkt))

print pkt.summary()

hexdump(pkt)
pkt.show()
pkt.canvas_dump()
