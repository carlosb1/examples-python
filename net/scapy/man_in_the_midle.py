from scapy.all import *
import nfqueue, socket

def scapy_cb(i, payload):
    s = payload.get_data()

    p = IP(s)

    if p.dst == "8.8.8.8" and ICMP in p:
        del(p[IP].chksum, p[ICMP].chksum)
        p[ICMP].seq=0
        ret = payload.set_verdict_modified(nfqueue.NF_ACCEPT, str(p), len(p))

    else:
        payload.set_verdict(nfqueue.NF_ACCEPT)


q = nfqueue.queue()

q.set_callback(scapy_cb)
q.fast_open(2807, socket.AF_INET)

q.try_run()
