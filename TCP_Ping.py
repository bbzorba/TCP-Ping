from tcp_latency import measure_latency

while(True):    
    try:
        ping = measure_latency(host='81.95.107.155', port=50061, timeout=2.5)
        print(ping, "ms")
    except KeyboardInterrupt:
        break