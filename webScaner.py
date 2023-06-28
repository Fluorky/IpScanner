import subprocess


def ping_ip(ip):

    (output, error) = subprocess.Popen((['ping',ip,'-n','1']),stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True).communicate()

    if b'bytes=32' in output:
        return "Work"
    elif b'Destination host unreachable.' in output:
        return "Host not response"
    elif error:
        return "DNS Error"
    else:
        return "Unknown error"


addr = input("Write 3 first octets ip addres like XXX.XXX.XXX. : ")
a = input("Write start scanning adres between 1 and 255: ")
b = input("Write end scanning adres between 1 and 255: ")
file = "Documents/python/pingHosts.txt"
f = open(file, "w")
for ip in range(int(a),int(b)+1):
    ip =str(addr)+str(ip)
    ip = ip.strip('\n')
    response= ping_ip(ip)
    result = ('%s, %s \n' %(ip,response))
    print(result)
    f.write(str(result))


f.close()
print("Done")

        
