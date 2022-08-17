from tcp_latency import measure_latency

while(True):    
    try:
        #write here the server's IP address , the port to connect and the timeout.
        ping = measure_latency(host='192.168.1.2', port=50061, timeout=2.5)
        print(ping, "ms")
    except KeyboardInterrupt:
        break
