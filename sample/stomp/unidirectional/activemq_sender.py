from stompest.config import StompConfig
from stompest.sync import Stomp
import ssl

context = ssl.create_default_context()
# Disable cert validation for demo only
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

CONFIG = StompConfig(uri='ssl://x.x.x.x:61614', login='id', passcode='password', check=False, sslContext=context)
QUEUE = '/queue/my-queue'

if __name__ == '__main__':
    client = Stomp(CONFIG)
    client.connect()
    client.send(QUEUE, 'test message 1'.encode())
    client.send(QUEUE, 'test message 2'.encode())
    client.disconnect()
