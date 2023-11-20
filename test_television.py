import pytest
from television import Television


def test_power():
    tv_pwr = Television()
    tv_pwr.power()
    assert tv_pwr.__str__() == 'Power = True, Channel = 0, Volume = 0'
    tv_pwr.power()
    assert tv_pwr.__str__() == 'Power = False, Channel = 0, Volume = 0'


def test_mute():
    tv_mute = Television()
    tv_mute.mute()
    assert tv_mute.__str__() == 'Power = False, Channel = 0, Volume =0'
    tv_mute.power()
    tv_mute.mute()
    assert tv_mute.__str__() == 'Power = True, Channel = 0, Volume = 0'


def test_channel_up():
   tv_chnl_up = Television()
    tv_chnl_up.channel_up()
    assert tv_chnl_up.__str__() == 'Power = False, Channel = 0, Volume = 0'
    tv_chnl_up.power()
    tv_chnl_up.channel_up()
    assert tv_chnl_up.__str__() == 'Power = True, Channel = 1, Volume = 0'
    tv_chnl_up.channel_up()
    assert tv_chnl_up.__str__() == 'Power = True, Channel = 2, Volume = 0'
    tv_chnl_up.channel_up()
    assert tv_chnl_up.__str__() == 'Power = True, Channel = 3, Volume = 0'
    tv_chnl_up.channel_up()
    assert tv_chnl_up.__str__() == 'Power = True, Channel = 0, Volume = 0'

def test_channel_down():
    tv_chnl_dwn = Television()
    tv_chnl_dwn.channel_down()
    assert tv_chnl_dwn.__str__() == 'Power = False, Channel = 0, Volume = 0'
    tv_chnl_dwn.power()
    tv_chnl_dwn.channel_down()
    assert tv_chnl_dwn.__str__() == 'Power = True, Channel = 3, Volume = 0'
    tv_chnl_dwn.channel_down()
    assert tv_chnl_dwn.__str__() == 'Power = True, Channel = 2, Volume = 0'
    tv_chnl_dwn.channel_down()
    assert tv_chnl_dwn.__str__() == 'Power = True, Channel = 1, Volume = 0'
    tv_chnl_dwn.channel_down()
    assert tv_chnl_dwn.__str__() == 'Power = True, Channel = 0, Volume = 0'

def test_volume_up():
    tv_vol_up = Television()
    tv_vol_up.volume_up()
    assert tv_vol_up.__str__() == 'Power = False, Channel = 0, Volume = 0'
    tv_vol_up.power()
    tv_vol_up.volume_up()
    assert tv_vol_up.__str__() == 'Power = True, Channel = 0, Volume = 1'
    tv_vol_up.volume_up()
    assert tv_vol_up.__str__() == 'Power = True, Channel = 0, Volume = 2'
    tv_vol_up.volume_up()
    assert tv_vol_up.__str__() == 'Power = True, Channel = 0, Volume = 2'


def test_volume_down():
   tv_vol_dwn = Television()
    tv_vol_dwn.volume_down()
    assert tv_vol_dwn.__str__() == 'Power = False, Channel = 0, Volume = 0'
    tv_vol_dwn.power()
    tv_vol_dwn.volume_down()
    assert tv_vol_dwn.__str__() == 'Power = True, Channel = 0, Volume = 0'
    tv_vol_dwn.volume_up()
    tv_vol_dwn.volume_up()
    tv_vol_dwn.volume_down()
    assert tv_vol_dwn.__str__() == 'Power = True, Channel = 0, Volume = 1'
    tv_vol_dwn.volume_down()
    assert tv_vol_dwn.__str__() == 'Power = True, Channel = 0, Volume = 0'


if __name__ == "__main__":
    pytest.main()
