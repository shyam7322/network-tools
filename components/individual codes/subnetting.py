import random
import sys

def subnet_calculation(ip_address, subnet_mask):
        print("\n")

        
        #calculate subnet based on IP and subnet mask

        #convert the mask to binary string

        mask_octets_pad = []
        mask_octets_dec = subnet_mask.split(".")
        
        for i in range(0, len(mask_octets_dec)):
            binary_octet = bin(int(mask_octets_dec[i])).split("b")[1]
            
            if len(binary_octet) ==8:
                mask_octets_pad.append(binary_octet)
            elif len(binary_octet) < 8:
                binary_octect_pad = binary_octet.zfill(8)
                mask_octets_pad.append(binary_octect_pad)
                
            dec_mask = "".join(mask_octets_pad)
            
            #calculate and count num of bits in host or a subnet
            
            num_zeros = dec_mask.count("0")
            num_ones = (32 - num_zeros)
            num_of_hosts = abs(2 ** num_zeros -2)
            
            wildcard_octets = []
            for i in mask_octets_dec:
                wi_octet = 255 - int(i)
                wildcard_octets.append(str(wi_octet))
                
            wildcard_mask = ".".join(wildcard_octets)
            
            #print(wildcard_mask)
          
        #convert the IP to binary 
        
        ip_octet_pad = []
        ip_octet_dec = ip_address.split(".")
        
        for i in range(0, len(ip_octet_dec)):
            binary_octet = bin(int(ip_octet_dec[i])).split("b")[1]
            
            if len(binary_octet) <8:
                binary_octect_pad = binary_octet.zfill(8)
                ip_octet_pad.append(binary_octect_pad)
            else:
                ip_octet_pad.append(binary_octet)
        
        binary_ip = "".join(ip_octet_pad)
        
        
        binary_network_address = binary_ip[:(num_ones)] + "0" * num_zeros
        #print(binary_network_address)
        
        
        binary_broadcast_address = binary_ip[:(num_ones)] + "1" * num_zeros 
        
            
        #print(binary_broadcast_address)
        
        net_ip_octets =[]
        for i in range(0, len(binary_network_address), 8):
            n_ip_octet = binary_network_address[i:i+8]
            net_ip_octets.append(n_ip_octet)
            
            
        net_ip_address =[]
        for i in net_ip_octets:
            net_ip_address.append(str(int(i,2)))
        
        network_address = ".".join(net_ip_address)
        
        max_ip_octets = []
        for i in range(0, len(binary_broadcast_address),8):
            m_ip_octets = binary_broadcast_address[i:i+8]
            max_ip_octets.append(m_ip_octets)
        
        max_ip_address = []
        for i in max_ip_octets:
            max_ip_address.append(str(int(i,2)))
            
        
        broadcast_address = ".".join(max_ip_address)
        
        #printing all the results
        print("\n")
        print("Network address is: %s" % network_address)
        print("Broadcast address is: %s" % broadcast_address)
        print("Number of hosts in subnet: %s" % num_of_hosts)
        print("Wildcard mask is: %s " % wildcard_mask)
        print("Mask bit is: %s " % num_ones)
        
        
if __name__ == "__main__":
    ip_address = input(" Enter your IP address: ")
    subnet_mask = input("Enter your subnet mask: ")
    subnet_calculation(ip_address, subnet_mask)
