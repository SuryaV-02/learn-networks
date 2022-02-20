from asyncio import protocols
import nmap

# from nmap import PortScanner
# s=nmap.PortScanner
portScanner = nmap.PortScanner()
host_scan = input('Host Scan : ')
l_ports = '21,22,23,25,80'
portScanner.scan(host_scan,arguments='-n -p' + l_ports)
print(portScanner.command_line())
hosts_list = [(x, portScanner[x]['status']['state']) for x in portScanner.all_hosts()]
for host,status in hosts_list:
    print(host,status)
    for protocol in portScanner[host].all_protocols():
        print('Protocol : ',protocol)
        list_port = portScanner['host']['tcp'].keys()
        for port in list_port:
            print('Port : {} State : {}'.format(port,portScanner[host][protocol]['state']))