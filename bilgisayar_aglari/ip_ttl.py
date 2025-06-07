from scapy.all import IP, TCP, send

def send_packet_with_ttl(src_ip, dst_ip, ttl_value):
    packet = IP(src=src_ip, dst=dst_ip, ttl=ttl_value) / TCP(dport=12345, sport=54321) / b"Test Packet"
    send(packet)
    print(f"Paket gönderildi! {src_ip} -> {dst_ip} | TTL: {ttl_value}")

if __name__ == "__main__":
    send_packet_with_ttl("127.0.0.1", "127.0.0.1", 42)