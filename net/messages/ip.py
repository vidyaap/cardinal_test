from .msg import Msg


class IPMsg(Msg):
    def __init__(self, pid: int, ip: str):
        super().__init__(pid)
        self.msg_type = "IP"
        self.ip = ip

    def __str__(self):
        return f"IPMsg({self.pid}): {self.ip}"