import nmap 

#  range of ports to be scanned 
begin = 75
end = 81

#  target ip to be scanned to 

target = '192.168.1.100'

scanner = nmap.PortScanner() 

for i in range(begin,end+1): 

	# scan the target port 
	res = scanner.scan(target,str(i)) 

	
	res = res['scan'][target]['tcp'][i]['state'] 

	print(f'port {i} is {res}.') 
print( "end of scan to scan more ports increase range or do another scan with a different range")