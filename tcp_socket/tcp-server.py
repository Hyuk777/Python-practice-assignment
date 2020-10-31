import socket

# 접속할 서버 주소.여기서는 루프백 인터페이스 주소 즉, localhost 사용
Host = '127.0.0.1'
# 클라이언트 접속을 대기하는 포트 번호
PORT = 9999

# 소켓 객체 생성
# 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 포트 사용중이라 연결할 수 없다는
# WinError 10048 에러 해결 위해 필요
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind 함수는 소켓을 특정 네트워크 인터페이스와 포트 번호에 연결하는데 사용
# HOST는 hostname, ip address, 빈 문자열 ""이 될 수 있음
# PORT는 1-65535 사이의 숫자를 사용할 수 있음
server_socket.bind((Host,PORT))

# 서버가 클라이언트의 접속을 혀용하도록 함
server_socket.listen()

# accept 함수에서 대기하다가 클라이언트가 접속하면 새로운 소켓 리턴
client_soket, addr = server_socket.accept()

# 접속한 클라이언트의 주소
print('Connected by', addr)

# 무한 루프를 돌면서
while True:

    # 클라이언트가 보낸 메시지를 수신하기 위해 대기
    data = client_soket.recv(1024)

    # 빈 문자열을 수신하면 루프 중지
    if not data:
        break

    # 수신받은 문자열을 출력
    print('Received from', addr, data.decode())

    # 받은 문자열을 다시 클라이언트로 전송해줌 (에코)
    client_soket.sendall(data)

# 소켓 닫음
client_soket.close()
server_socket.close()