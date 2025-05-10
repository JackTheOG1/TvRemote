from PyQt6.QtWidgets import QMainWindow, QGraphicsScene
from PyQt6.QtGui import QPixmap
from gui import Ui_MainWindow
from television import Television

class TVFunc(QMainWindow):
    """
    The main class that links buttons
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.tv = Television()
        self.channels = ["Disney", "Nickelodeon", "Cartoon Network"]


        self.ui.powerButton.clicked.connect(self.toggle_power)
        self.ui.muteButton.clicked.connect(self.toggle_mute)
        self.ui.volumeUpButton.clicked.connect(self.volume_up)
        self.ui.volumeDownButton.clicked.connect(self.volume_down)
        self.ui.channelUpButton.clicked.connect(self.channel_up)
        self.ui.channelDownButton.clicked.connect(self.channel_down)
        self.ui.channelSlider.valueChanged.connect(self.slider_channel_change)


        self.ui.channelSlider.setMinimum(0)
        self.ui.channelSlider.setMaximum(len(self.channels) - 1)

        self.update_ui()

    def toggle_power(self):
        """
        The power button
        :return:
        """
        self.tv.power()
        self.update_ui()

    def toggle_mute(self):
        """
        same as power but for the mute function
        :return:
        """
        if self.tv.is_on():
            self.tv.mute()
            self.update_ui()

    def volume_up(self):
        """
        This turns up the volume by one tic
        :return:
        """
        if self.tv.is_on() and not self.tv.is_muted():
            self.tv.volume_up()
        self.update_ui()

    def volume_down(self):
        """
        This turns down the volume by one tic
        :return:
        """
        if self.tv.is_on() and not self.tv.is_muted():
            self.tv.volume_down()
        self.update_ui()

    def channel_up(self):
        """
        This allows you to change the channel up by one
        :return:
        """
        self.tv.channel_up()
        self.ui.channelSlider.setValue(self.tv.get_channel())
        self.update_ui()

    def channel_down(self):
        """
        same as previous, turns down by one
        :return:
        """
        self.tv.channel_down()
        self.ui.channelSlider.setValue(self.tv.get_channel())
        self.update_ui()

    def slider_channel_change(self, value):
        """
        slider is a way to manually put in the channel
        :param value:
        :return:
        """
        if self.tv.is_on():
            self.tv.set_channel(value)
            self.update_ui()

    def update_ui(self):
        """
        allows the ui to be updated by your inputs
        :return:
        """
        try:
            if self.tv.is_on():
                self.ui.powerButton.setChecked(True)

                channel = self.tv.get_channel()
                channel_text = self.channels[channel]

                self.ui.tvChannel.setStyleSheet("background-color: black; color: white; font-size: 20px;")
                scene = self.ui.tvChannel.scene() or self.create_scene()
                scene.clear()
                scene.addText(channel_text)



                image_path = f"images/channel_{channel}.png"

                pixmap = QPixmap(image_path)
                scene.addPixmap(pixmap.scaled(self.ui.tvChannel.width(), self.ui.tvChannel.height()))

                vol = 0 if self.tv.is_muted() else self.tv.get_volume()
                self.ui.volumeBar.setValue(vol * 50)
            else:
                self.ui.tvChannel.setScene(None)
                self.ui.volumeBar.setValue(0)
        except Exception:
            raise
    def create_scene(self):

        scene = QGraphicsScene()
        self.ui.tvChannel.setScene(scene)
        return scene
