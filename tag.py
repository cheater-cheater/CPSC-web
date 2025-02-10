from scapy.all import *

# Define the IP for the target address
ip = IP(dst="joey15.computing.clemson.edu")

# Define a custom payload to increase the packet size (optional)
payload = "Hello world" * 500  # 2000 bytes of data (1 KB)

# List of ports to send SYN packets to
ports = [443]  # Add more ports as needed

# Loop to send SYN packets to multiple ports
for port in ports:
    for seq_num in range(1000, 9999):  # Send 10 packets with different sequence numbers
        syn = TCP(dport=port, flags="S", seq=seq_num)

        # Create a larger packet by adding the payload
        packet = ip/syn/payload

        # Send the SYN packet and wait for a response
        response = sr1(packet, timeout=1)

        # Check if a SYN-ACK response is received
        if response:
            if response.haslayer(TCP):
                tcp_layer = response.getlayer(TCP)
                # Check for SYN and ACK flags
                if tcp_layer.flags == "SA":  # "SA" means SYN-ACK
                    print(f"Received SYN-ACK for seq={seq_num} on port {port}, handshake successful!")
                else:
                    print(f"Received non-SYN-ACK response for seq={seq_num} on port {port}: {tcp_layer.flags}")
        else:
            print(f"No response received for seq={seq_num} on port {port}.")