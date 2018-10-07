from dreamscreen.utils import Packet


class CMD:
    def __init__(self, name: str, raw: bytes):
        self.name = name
        self.raw = raw
        packet = Packet.from_bytes(self.raw)
        self.upper = packet.upper
        self.lower = packet.lower
        self.payload = packet.payload

    def __repr__(self):
        return "<{name}: {upper:02X} {lower:02X} {payload}>".format(
            name=self.name,
            upper=self.upper,
            lower=self.lower,
            payload= "[{}]".format(":".join(["{:02X}".format(c) for c in self.payload])),
        )


EnableCECPassthrough = CMD(None, b'fc06004103260133')

