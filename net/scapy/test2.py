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


sr1(IP(dst="8.8.8.8") / UDP() / DNS(qd=DNSQR()))

p[DNS].an
