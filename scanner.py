from scapy.all import ARP, Ether, srp

print("=" * 40)
print("        Network Scanner")
print("=" * 40)

network = input("Enter Network (Example 192.168.1.0/24): ")

# Create ARP request
arp_request = ARP(pdst=network)

# Create Ethernet broadcast frame
broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

# Combine Ethernet + ARP
packet = broadcast / arp_request

# Send packet
answered, unanswered = srp(packet, timeout=2, verbose=False)

print("\nDevices Found\n")

for sent, received in answered:
    print(f"IP Address : {received.psrc}")
    print(f"MAC Address: {received.hwsrc}")
    print("-" * 35)