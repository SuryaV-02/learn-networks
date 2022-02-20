import socket,struct,binascii,textwrap


def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('!6s6s2s',data[:14])
    return get_mac_address(dest_mac), get_mac_address(src_mac), get_protocol(proto), data[14:]

def get_mac_address(bytes_addr):
    bytes_str = map('{:02x}'.format,bytes_addr)
    mac_address = ':'.join(bytes_str).upper()
    return mac_address

def get_protocol(bytes_proto):
    bytes_str =map('{:02x}'.format,bytes_proto)
    protocol = ':'.join(bytes_str).upper()
    return protocol

hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)
print('IP : {}'.format(host_ip))

'''
Notes :-

SOCK_RAW -> bypass directly to applications thro' underlying transport protocols
IPPROTO_IP -> Creates socket that receives RAW data for transport prtocols (TCP/UDP)
IP_HDRINCL -> makes IPv4 layer to include header as mandatory
SIO_RCVALL & RCVALL_ON -> Control code enables a socket to receive all IPv4 or IPv6 packets passing through a network interface.
'''

# Creating connection
conn = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
conn.bind((host_ip,0))

# Include IP headers
conn.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
# Enable promiscous mode
conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

while True:
    # Receive Data
    raw_data,addr = conn.recvfrom(65536)
    # print(raw_data)
    #unpack th data
    dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)

    print('Ethernet Frame :-')
    print('Source MAC : {}'.format(src_mac))
    print('Destination MAC : {}'.format(dest_mac))
    print('Protocol : {}'.format(eth_proto))

