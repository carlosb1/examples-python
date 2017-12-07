import socket
dn = 'google.com'

l = socket.getaddrinfo(dn,443,socket.INADDR_ANY, socket.SOCK_STREAM, socket.IPPROTO_TCP)

assert len(l) > 0, 'No address found :('

s = socket.socket(l[0][0],l[0][1],l[0][2])
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT,1)
ip_and_port = l[0][4]

import ssl

assert (ssl.HAS_ALPN)

ssl_ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ssl_ctx.set_ciphers(':'.join([  # List from ANSSI TLS guide v.1.1 p.51
                'ECDHE-ECDSA-AES256-GCM-SHA384',
                'ECDHE-RSA-AES256-GCM-SHA384',
                'ECDHE-ECDSA-AES128-GCM-SHA256',
                'ECDHE-RSA-AES128-GCM-SHA256',
                'ECDHE-ECDSA-AES256-SHA384',
                'ECDHE-RSA-AES256-SHA384',
                'ECDHE-ECDSA-AES128-SHA256',
                'ECDHE-RSA-AES128-SHA256',
                'ECDHE-ECDSA-CAMELLIA256-SHA384',
                'ECDHE-RSA-CAMELLIA256-SHA384',
                'ECDHE-ECDSA-CAMELLIA128-SHA256',
                'ECDHE-RSA-CAMELLIA128-SHA256',
                'DHE-RSA-AES256-GCM-SHA384',
                'DHE-RSA-AES128-GCM-SHA256',
                'DHE-RSA-AES256-SHA256',
                'DHE-RSA-AES128-SHA256',
                'AES256-GCM-SHA384',
                'AES128-GCM-SHA256',
                'AES256-SHA256',
                'AES128-SHA256',
                'CAMELLIA128-SHA256'
            ]))    
ssl_ctx.set_alpn_protocols(['h2']) #h2 is a RFC7540-hardcoded value
ssl_sock = ssl_ctx.wrap_socket(s,server_hostname=dn)

ssl_sock.connect(ip_and_port)
assert('h2' == ssl_sock.selected_alpn_protocol())


import scapy.supersocket as supersocket
import scapy.contrib.http2 as h2
import scapy.config

scapy.config.conf.debug_dissector = True
ss = supersocket.SSLStreamSocket(ssl_sock, basecls=h2.H2Frame)
srv_set = ss.recv()
srv_set.show()


