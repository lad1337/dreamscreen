from functools import partialmethod
import socket
from dreamscreen.utils import crc8

from dreamscreen.cmd import EnableCECPassthrough

class Client(object):

    def __init__(self, endpoint, group=None):
        self.endpoint = endpoint
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.group = 0 if group is None else group

    def send_packet(self, packet):
        self._sock.sendto(packet, self.endpoint)

    def build_packet(self, cmd):
        flags = 17  # no idea what to do with this for now
        if cmd.payload is None:
            payload = []
        packet = [
            0xFC,  # 0: always this
            len(cmd.payload) + 5,  # 1: length
            cmd.group,  # 2: group address, the group number which the device belongs.
            # 0x00 indicates "No specified Group",
            # 0x01 indicates group 1, 0x02 indicates group 2,
            # etc. If the Group Address is incorrect, DreamScreen will discard the message.k
            flags,  # 3: flags, provides context for handling the message
            cmd.upper,  # 4: command upper, specifies command namespace
            cmd.lower,  # 5: command lower, specifies individual command within namespace
        ]
        if payload is not None:
            for i in payload:
                packet.append(i)
        packet.append(crc8(packet))
        resp = bytearray(packet)
        return resp

    def send_cmd(self, cmd):
        packet = self.build_packet(cmd)
        self.send_packet(packet)

    enable_cec_passthrough = partialmethod(EnableCECPassthrough)
