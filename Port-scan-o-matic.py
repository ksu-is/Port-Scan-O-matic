import nmap 

#  range of ports to be scanned 
begin = int(input("input port between 1-65,535 to start port scan at: "))
end = int(input("input port between 1-65,535 to end port scan at: "))

#  target ip to be scanned to 

target = input("Input an IP address to scan for open ports: ")

scanner = nmap.PortScanner() 

for i in range(begin,end+1): 

	# scan the target port 
	res = scanner.scan(target,str(i)) 

	
	res = res['scan'][target]['tcp'][i]['state'] 

	print(f'port {i} is {res}.') 
print( "end of scan, to scan more ports increase port range or do a different scan with a different range")
