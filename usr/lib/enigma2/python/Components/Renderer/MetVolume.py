# 2016.10.24 19:07:23 WIT
#Embedded file name: /usr/lib/enigma2/python/Components/Renderer/MetVolume.py
from Renderer import Renderer
from enigma import eLabel
from enigma import eDVBVolumecontrol, eTimer
from Components.VariableText import VariableText

class MetVolume(VariableText, Renderer):

    def __init__(self):
        Renderer.__init__(self)
        VariableText.__init__(self)
        self.start = False
        self.vTimer = eTimer()
        self.vTimer.callback.append(self.changed)

    GUI_WIDGET = eLabel

    def changed(self, what = ''):
        if self.start:
            self.text = str(eDVBVolumecontrol.getInstance().getVolume()) + '%'

    def onShow(self):
        self.start = True
        self.vTimer.start(200)

    def onHide(self):
        self.start = False
        self.vTimer.stop()
