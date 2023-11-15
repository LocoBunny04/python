class Television:
    __MIN_VOLUME = 0
    __MAX_VOLUME = 2
    __MIN_CHANNEL = 0
    __MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.__MIN_VOLUME
        self.__channel = Television.__MIN_CHANNEL

    def power(self):
        if not self.__status:
            self.__status = True
        else:
            self.__status = False
        # print(f'Power is {self.__status}')

    def mute(self):
        if not self.__status:
            return
        elif not self.__muted:
            self.__muted = True

    def channel_up(self):
        if self.__status:
            if self.__channel < Television.__MAX_CHANNEL:
                self.__channel += 1
                # print(self.__channel)
            elif self.__channel == Television.__MAX_CHANNEL:
                self.__channel = Television.__MIN_CHANNEL

    def channel_down(self):

        if self.__status:
            if self.__channel > Television.__MIN_CHANNEL:
                self.__channel -= 1
                # print(self.__channel)
            elif self.__channel == Television.__MIN_CHANNEL:
                self.__channel = self.__MAX_CHANNEL

    def volume_up(self):
        if self.__status:
            if self.__volume < Television.__MAX_VOLUME:
                if self.__muted:
                    self.__muted = False
                self.__volume += 1
                # print(self.__volume)
            else:
                return self.__volume

    def volume_down(self):
        if self.__volume > Television.__MIN_VOLUME:
            if self.__muted:
                self.__muted = False
            self.__volume -= 1
            # print(self.__volume)
        else:
            return self.__volume

    def __str__(self):
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
