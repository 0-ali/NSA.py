from lib import smbCheck
import nmap
"""
    @copyright Mohammed Ali
"""

def Scanner(rhosts,rport="445"):
    nm = nmap.PortScanner()
    nm.scan(rhosts,rport)
    hosts = nm.all_hosts()
    smbCheck.log.info("[+] {} hosts found!".format(len(hosts)))
    for host in nm.all_hosts():
            if(nm[host].state() == "up"):
                if(nm[host].has_tcp(445)):
                    smb = smbCheck.check(host,int(rport))
                    getattr(smbCheck.log,smb[2])(smb[1])

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("{} <ip>".format(sys.argv[0]))
        sys.exit(1)
    else:
        Scanner(sys.argv[1])
