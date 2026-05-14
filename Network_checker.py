import socket

def scan_port(ip, port):
    #This create a "specialist" connection to the ip
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) #Don't wait forever 
    
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"[*] port {port} is OPEN - Target Acquired!")
    else:
        print(f"[] port {port} is closed.")
        s.close()
            
#The setup
target_ip ="127.0.0.1" 
port_to_scan = 8080

print(f"--- Scanning {target_ip} ---")
scan_port(target_ip, port_to_scan)
