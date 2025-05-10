class Television:
    """
    A class for television controls
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL = 2
    def __init__(self) -> None:
        """
        A place to set the defaults
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        This is the power state of the TV
        :return: None
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        This is the muted state of the TV
        :return: None
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Turns the channel up by one
        :return: None
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Turns the channel down by one
        :return: None
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Turns the volume up by one
        :return: None
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Turns the volume down by one
        :return: None
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def set_channel(self, value: int) -> None:
        """Directly set the channel, if valid and TV is on"""
        if self.__status:
            if Television.MIN_CHANNEL <= value <= Television.MAX_CHANNEL:
                self.__channel = value

    def get_channel(self) -> int:
        """Return current channel"""
        return self.__channel

    def get_volume(self) -> int:
        """Return current volume"""
        return self.__volume

    def is_muted(self) -> bool:
        """Return True if TV is muted"""
        return self.__muted

    def is_on(self) -> bool:
        """Return True if TV is powered on"""
        return self.__status

    def __str__(self) -> str:
        """Return a string of the TV's current status"""
        volume = 0 if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}"
