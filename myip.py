rom flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    ip_address = socket.gethostbyname(socket.gethostname())
    return f'My IP address is: {ip_address}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)