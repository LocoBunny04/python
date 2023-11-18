import pytest
from television import Television


def test_init_power():
    assert Television.power == False


def test_mute():
    assert Television.mute == False


def test_channel_up():
    assert Television.channel_up(1)


def test_channel_down():
    assert Television.channel_down(0)


def test_volume_up():
    assert Television.volume_up(1)


def test_volume_down():
    assert Television.volume_down(0)


if __name__ == "__main__":
    pytest.main()
