"""
孙页面：视听（ 首选项 的子页面），
此页面包含了视觉效果与音频效果等可调整设置选项，包含三个部分：音乐、音效、朗读、主题、字体、一言，
引用时可作 SettAvUI / subsubpage_setting_audiovisual
"""

from PySide2.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QStackedWidget,
    QLayout,
)
from PySide2.QtCore import Qt
import qfluentwidgets as qfw
from qfluentwidgets import FluentIcon as FI
from app_const_var import *
from app_config import *


# 加载配置文件
sett_av_ui_cfg = AppCommonConfig()
qfw.qconfig.load(AssetsPath.APP_CONFIG, AppCommonConfig)


def set_widget_to_layout(wlist: list, layout: QLayout):
    """设置布局的通用函数"""
    for widget in wlist:
        layout.addWidget(widget)


class MusicSettingGroup(QWidget):
    """音乐 部分，继承自 QWidget，
    引用时可作 MusicSettGr"""

    def __init__(self):
        super().__init__()

        # 初始化垂直布局
        self.vboxlayout = QVBoxLayout(self)

        # 初始化控件
        self.init_widgets()

        # 控件列表
        self.widget_list = [
            self.music_switch_card,
            self.music_path_card,
            self.music_volume_card,
            self.music_play_smoothly_card,
            self.music_pause_smoothly_card,
        ]

        # 设置布局
        set_widget_to_layout(self.widget_list, self.vboxlayout)
        self.setLayout(self.vboxlayout)

    def init_widgets(self):
        """初始化控件"""
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


class SoundSettingGroup(QWidget):
    """音效 部分，继承自 QWidget，
    引用时可作 SoundSettGr"""

    def __init__(self):
        super().__init__(self)

        # 初始化垂直布局
        self.vboxlayout = QVBoxLayout(self)

        # 初始化控件
        self.init_widgets()

        # 控件列表
        self.widget_list = [
            self.sound_switch_card,
            self.sound_path,
            self.sound_play_time,
        ]

        # 设置布局
        set_widget_to_layout(self.widget_list, self.vboxlayout)
        self.setLayout(self.vboxlayout)

    def init_widgets(self):
        """初始化控件"""
        # 音效开关
        self.sound_switch_card = qfw.SwitchSettingCard(
            FI.RINGER,
            "音效开关",
            "控制是否在点名结束后播放抽选音效",
            sett_av_ui_cfg.sound_switch,
        )

        # 音效路径
        self.sound_path = qfw.PushSettingCard(
            "选择",
            FI.DOCUMENT,
            "音效路径",
            "选择要启用的音效文件",
            sett_av_ui_cfg.sound_path,
        )

        # 音效在何时播放
        self.sound_play_time = qfw.OptionsSettingCard(
            sett_av_ui_cfg.sound_play_time,
            FI.RINGER,
            "音效在何时播放",
            texts=["仅普通抽选后", "仅快速抽选后", "两者后"],
        )


class ReadSettingGroup(QWidget):
    """朗读 部分，继承自 QWidget，
    引用时可作 ReadSettGr"""

    def __init__(self):
        super().__init__(self)

        # 初始化垂直布局
        self.vboxlayout = QVBoxLayout(self)

        # 初始化控件
        self.init_widgets()

    def init_widgets(self):
        """初始化控件"""
        # 朗读开关
        self.read_switch_card = qfw.SwitchSettingCard(
            FI.SPEAKERS,
            "朗读开关",
            "控制是否在点名结束后朗读被抽中的名字",
            sett_av_ui_cfg.read_switch,
        )

        # 在何时朗读
        self.read_time = qfw.OptionsSettingCard(
            sett_av_ui_cfg.read_time,
            FI.RINGER,
            "在何时朗读",
            texts=["仅普通抽选后", "仅快速抽选后", "两者后"],
        )
