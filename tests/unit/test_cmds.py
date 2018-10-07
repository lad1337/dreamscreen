import pytest

from dreamscreen.cmds import EnableCECPassthrough

@pytest.mark.parametrize('cmd, upper, lower, payload', [
    (EnableCECPassthrough, 0x03, 0x26, [0x01])
])
def test_cmd(cmd, upper, lower, payload):
    assert cmd.upper == upper
    assert cmd.lower == lower
    assert cmd.payload == payload
