"""
孙页面：视听（ 首选项 的子页面），
此页面包含了背景音乐、音效、朗读等可调整设置选项，包含三个部分：音乐、音效、朗读，
引用时可作 SettAvUI / subsubpage_setting_audiovisual
"""

from PySide2.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget
from PySide2.QtCore import Qt
import qfluentwidgets as qfw
from qfluentwidgets import FluentIcon as FI
from app_const_var import *
from app_config import *


# 加载配置文件
sett_av_ui_cfg = AppCommonConfig()
qfw.qconfig.load(AssetsPath.APP_CONFIG, AppCommonConfig)


class MusicSettingGroup(QWidget):
    """音乐 部分，继承自 QWidget，
    引用时可作 MusicSettGr"""

    def __init__(self):
        super().__init__()

        # 初始化垂直布局
        self.vboxlayout = QVBoxLayout(self)

        # 音乐开关
        self.music_switch_card = qfw.SwitchSettingCard(
            FI.MUSIC,
            "音乐开关",
            "控制是否在普通抽选时播放背景音乐",
            sett_av_ui_cfg.music_switch,
        )

        # 音乐文件
        self.music_path_card = qfw.PushSettingCard(
            "选择", FI.DOCUMENT, "音乐文件", "选择要启用的音乐文件"
        )

        # 音量调节
        self.music_volume_card = qfw.RangeSettingCard(
            sett_av_ui_cfg.music_volume, FI.VOLUME, "音乐音量", "调节音乐在播放时的音量"
        )

        # 渐入效果
        self.music_play_smoothly_card = qfw.RangeSettingCard(
            sett_av_ui_cfg.music_play_smoothly,
            FI.ZOOM_IN,
            "音乐渐入效果",
            "调整音乐播放时渐入效果持续的秒数(s)",
        )

        # 渐出效果
        self.music_pause_smoothly_card = qfw.RangeSettingCard(
            sett_av_ui_cfg.music_pause_smoothly,
            FI.ZOOM_OUT,
            "音乐渐出效果",
            "调整音乐播放时渐出效果持续的秒数(s)",
        )

        # 控件列表
        self.widget_list = [
            self.music_switch_card,
            self.music_path_card,
            self.music_volume_card,
            self.music_play_smoothly_card,
            self.music_pause_smoothly_card,
        ]

        # 设置布局
        for widget in self.widget_list:
            self.vboxlayout.addWidget(widget)
        self.setLayout(self.vboxlayout)
