class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Checks to see if the T.V is off; if not it turns the T.V. on and vice versa.
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False
        # print(f'Power is {self.__status}')

    def mute(self) -> None:
        """ Checks to see if the T.V is powered on before changing the status of the
        different methods and their respective variables. If the status is false then nothing changes
        methods and variables If the t.v. is muted then it will be un-muted and vice versa.
        """
        if not self.__status:
            return
        elif not self.__muted:
            self.__muted = True

    def channel_up(self):
        """If the status of the T.V is true, then the channel will increase. However, if the channel reaches
        max, it will go back to the minimum."""
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
                # print(self.__channel)
            elif self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """If the status of the T.V is true, then the channel will decrease. However, if the channel reaches
        its minimum, it will go back to the max."""

        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
                # print(self.__channel)
            elif self.__channel == Television.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self):
        """Checks to see the status of the muted function. If its muted, it will unmute and increase the value of the volume.
                if the volume is already at maximum level then nothing changes."""
        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                if self.__muted:
                    self.__muted = False
                self.__volume += 1
                # print(self.__volume)
            # else:
            #     return self.__volume

    def volume_down(self):
        """Checks to see the status of the muted function. If its muted, it will unmute and decrease the value of the volume.
        if the volume is already at minimum then nothing changes."""
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                if self.__muted:
                    self.__muted = False
                self.__volume -= 1
                # print(self.__volume)
            # else:
            #     return self.__volume

    def __str__(self) -> str:
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
