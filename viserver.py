# Importing the libraries
import socket, cv2, pickle, struct, imutils
# Create Socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Socket Bind
sock.bind(('', 9090))
# Socket Listen
sock.listen(5)

# Socket Accept
while True:
    conn, addr = sock.accept()
    print('GOT CONNECTION FROM:',addr)
    if conn:
        vid = cv2.VideoCapture(0)
        while(vid.isOpened()):
            img,frame = vid.read()
            frame = imutils.resize(frame,width=320)
            a = pickle.dumps(frame)
            message = struct.pack("Q",len(a))+a
            conn.sendall(message)

            cv2.imshow('TRANSMITTING VIDEO',frame)
            key = cv2.waitKey(1) & 0xFF
            if key ==ord('q'):
                conn.close()
                break
cv2.destroyAllWindows()
