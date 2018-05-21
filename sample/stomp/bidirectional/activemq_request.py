from stompest.config import StompConfig
from stompest.protocol import StompSpec
from stompest.sync import Stomp
import ssl

context = ssl.create_default_context()
# Disable cert validation for demo only
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

CONFIG = StompConfig(uri='ssl://x.x.x.x:61614', login='id', passcode='password', check=False, sslContext=context)
QUEUE = '/queue/my-queue'
RQUEUE = '/queue/my-reply'


if __name__ == '__main__':
    client = Stomp(CONFIG)
    client.connect()
    client.send(QUEUE, 'test message 1'.encode(), headers={'reply-to': RQUEUE, 'correlation-id': 0})

    client.subscribe(RQUEUE, {StompSpec.ACK_HEADER: StompSpec.ACK_CLIENT_INDIVIDUAL})
    recv_frame = client.receiveFrame()
    print('Got %s' % recv_frame.info())
    client.ack(recv_frame)
    client.disconnect()
