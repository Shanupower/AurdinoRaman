import socket
import threading

# Global variable to store the received data
receivedData = ""

def start_udp_server():
    global receivedData

    # Set up the UDP server
    udp_ip = "127.0.0.1"
    udp_port = 1234
    buffer_size = 1024

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        sock.bind((udp_ip, udp_port))
        print(f"UDP server up and listening on {udp_ip}:{udp_port}")
    except socket.error as e:
        print(f"Error binding UDP server to {udp_ip}:{udp_port} - {e}")
        return

    while True:
        try:
            data, addr = sock.recvfrom(buffer_size)
            receivedData = data.decode('utf-8')
            print(f"Received data: {receivedData} from {addr}")
        except Exception as e:
            print(f"Error receiving data: {e}")

# Start the UDP server in a separate thread
udp_thread = threading.Thread(target=start_udp_server)
udp_thread.daemon = True
udp_thread.start()
