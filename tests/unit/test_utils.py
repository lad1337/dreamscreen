
import pytest

from dreamscreen.utils import Packet


@pytest.mark.parametrize('packet, upper, lower, payload',[
    (b'fc06004103600011', 0x03, 0x60, [0x00]),
    (b'fc060041031401e0', 0x03, 0x14, [0x01]),
    (b'fc060041030100f1', 0x03, 0x01, [0x00]),
    (b'fc05ff30010a2a', 0x01, 0x0a, []),
])
def test_cmd_parsing(packet, upper, lower, payload):
    p = Packet.from_bytes(packet)
    assert upper == p.upper
    assert lower == p.lower
    assert payload == p.payload
