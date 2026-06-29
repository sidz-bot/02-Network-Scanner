from scapy.all import ARP, Ether

print("=" * 40)
print("      Network Scanner")
print("=" * 40)

network = input("Enter Network (Example 192.168.1.0/24): ")

# Create ARP request
arp_request = ARP(pdst=network)

# Create Ethernet broadcast frame
broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

print("\nARP Packet:")
arp_request.show()

print("\nEthernet Frame:")
broadcast.show()