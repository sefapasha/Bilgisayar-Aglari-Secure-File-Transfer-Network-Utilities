import socket
import struct

def checksum(data):
    """IP header için basit checksum hesaplayici"""
    if len(data) % 2:
        data += b'\x00'
    res = sum((data[i] << 8) + data[i+1] for i in range(0, len(data), 2))
    res = (res >> 16) + (res & 0xffff)
    res += (res >> 16)
    return (~res) & 0xffff

def create_ip_header(src_ip, dst_ip, ttl=64):
    """Özel IP header oluşturur"""
    version_ihl = (4 << 4) + 5
    tos = 0
    total_length = 20  # Sadece IP header
    identification = 12345
    flags_fragment = 0
    protocol = socket.IPPROTO_TCP
    header_checksum = 0
    src_addr = socket.inet_aton(src_ip)
    dst_addr = socket.inet_aton(dst_ip)

    ip_header = struct.pack('!BBHHHBBH4s4s',
                            version_ihl, tos, total_length,
                            identification, flags_fragment,
                            ttl, protocol, header_checksum,
                            src_addr, dst_addr)

    header_checksum = checksum(ip_header)

    ip_header = struct.pack('!BBHHHBBH4s4s',
                            version_ihl, tos, total_length,
                            identification, flags_fragment,
                            ttl, protocol, header_checksum,
                            src_addr, dst_addr)

    return ip_header

def send_packet(src_ip, dst_ip, ttl=64):
    """IP header içeren bir paket gönderir"""
    ip_header = create_ip_header(src_ip, dst_ip, ttl)

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
        sock.sendto(ip_header, (dst_ip, 0))
        print(f" IP paketi gönderildi ➜ {src_ip} → {dst_ip} | TTL: {ttl}")
    except PermissionError:
        print(" Bu komut için yönetici (admin/root) yetkisi gerekir.")
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    # Loopback adresine paket gönder
    send_packet("127.0.0.1", "127.0.0.1", ttl=42)
