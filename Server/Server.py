from laboratoryTools.network import Socket, ServerSocket, ClientSocket
from laboratoryTools.logging import logger
from select import select


class Server:
    def __init__(self, name):
        self.serverSocket:"ServerSocket" = ServerSocket(name=name)
        self.serverSocket.msgReceivedCallback = self.echoMsg

    def echoMsg(self, clientSocket:"ClientSocket", msg:"str"):
        logger.info(msg="Message receive from {}:\n\t{}".format(clientSocket, msg))
        clientSocket.send_s(data="I received \"{}\" from you.".format(msg))

    def start(self):
        self.serverSocket.start()

    def stop(self):
        self.serverSocket.stop()

if __name__ == "__main__":
    try:
        server:"Server" = Server(name="Laboratory")
        server.start()
    except Exception as e:
        logger.error(msg=e)
    finally:
        server.stop()