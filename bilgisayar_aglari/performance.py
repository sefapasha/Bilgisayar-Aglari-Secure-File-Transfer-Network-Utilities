import subprocess
import time

def measure_ping(host='8.8.8.8'):
    """Belirtilen host'a 1 ping atarak gecikme süresini ölçer"""
    start = time.time()
    result = subprocess.call(['ping', '-n', '1', host], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    end = time.time()

    if result == 0:
        return round((end - start) * 1000, 2)  # ms cinsinden döner
    else:
        return None

if __name__ == "__main__":
    print("Ag Performansı Ölçümü Başlatılıyor...\n")

    ping_ms = measure_ping()
    if ping_ms is not None:
        print(f"Ping süresi: {ping_ms} ms")
    else:
        print("Ping başarısız.")
