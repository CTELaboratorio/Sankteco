"""
孙页面:视听( 首选项 的子页面), 
此页面包含了视觉效果与音频效果等可调整设置选项, 包含五个部分:音乐, 音效, 朗读, 主题, 一言, 
引用时可作 SettAvUI / subsubpage_setting_audiovisual
"""

from PySide2.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QWidget,
    QLayout,
)
import qfluentwidgets as qfw
from qfluentwidgets import FluentIcon as FI
from app_const_var import SettAvUIString, AssetsPathTXT
from app_config import AppCommonConfig


# 加载配置文件
sett_av_ui_cfg = AppCommonConfig()
qfw.qconfig.load(AssetsPathTXT.APP_CONFIG, sett_av_ui_cfg)


def set_widget_to_layout(wlist: list, layout: QLayout):
    """设置布局的通用函数"""
    for widget in wlist:
        layout.addWidget(widget)


class MusicSettingGroup(QWidget):
    """音乐 部分, 继承自 QWidget,
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

    def init_widgets(self):
        """初始化控件"""

        # 音乐开关
        self.music_switch_card = qfw.SwitchSettingCard(
            FI.MUSIC,
            SettAvUIString.MUSIC_SWITCH_CARD_TITLE,
            SettAvUIString.MUSIC_SWITCH_CARD_CONTEXT,
            sett_av_ui_cfg.music_switch,
        )

        # 音乐文件
        self.music_path_card = qfw.PushSettingCard(
            SettAvUIString.MUSIC_PATH_CARD_BUTTON,
            FI.DOCUMENT,
            SettAvUIString.MUSIC_PATH_CARD_TITLE,
            SettAvUIString.MUSIC_PATH_CARD_CONTEXT,
        )

        # 音量调节
        self.music_volume_card = qfw.RangeSettingCard(
            sett_av_ui_cfg.music_volume,
            FI.VOLUME,
            SettAvUIString.MUSIC_VOLUME_CARD_TITLE,
            SettAvUIString.MUSIC_VOLUME_CARD_CONTEXT,
        )

        # 渐入效果
        self.music_play_smoothly_card = qfw.RangeSettingCard(
            sett_av_ui_cfg.music_play_smoothly,
            FI.ZOOM_IN,
            SettAvUIString.MUSIC_PLAY_SMOOTHLY_CARD_TITLE,
            SettAvUIString.MUSIC_PLAY_SMOOTHLY_CARD_CONTEXT,
        )

        # 渐出效果
        self.music_pause_smoothly_card = qfw.RangeSettingCard(
            sett_av_ui_cfg.music_pause_smoothly,
            FI.ZOOM_OUT,
            SettAvUIString.MUSIC_PAUSE_SMOOTHLY_CARD_TITLE,
            SettAvUIString.MUSIC_PAUSE_SMOOTHLY_CARD_CONTEXT,
        )


class SoundSettingGroup(QWidget):
    """音效 部分, 继承自 QWidget,
    引用时可作 SoundSettGr"""

    def __init__(self):
        super().__init__()

        # 初始化垂直布局
        self.vboxlayout = QVBoxLayout(self)

        # 初始化控件
        self.init_widgets()

        # 控件列表
        self.widget_list = [
            self.sound_switch_card,
            self.sound_path_card,
            self.sound_play_time_card,
        ]

        # 设置布局
        set_widget_to_layout(self.widget_list, self.vboxlayout)
        self.setLayout(self.vboxlayout)

    def init_widgets(self):
        """初始化控件"""

        # 音效开关
        self.sound_switch_card = qfw.SwitchSettingCard(
            FI.RINGER,
            SettAvUIString.SOUND_SWITCH_CARD_TITLE,
            SettAvUIString.SOUND_SWITCH_CARD_CONTEXT,
            sett_av_ui_cfg.sound_switch,
        )

        # 音效路径
        self.sound_path_card = qfw.PushSettingCard(
            SettAvUIString.SOUND_PATH_CARD_BUTTON,
            FI.DOCUMENT,
            SettAvUIString.SOUND_PATH_CRAD_TITLE,
            SettAvUIString.SOUND_PATH_CRAD_CONTEXT,
        )

        # 音效在何时播放
        self.sound_play_time_card = qfw.OptionsSettingCard(
            sett_av_ui_cfg.sound_play_time,
            FI.RINGER,
            SettAvUIString.SOUND_PLAY_TIME_CARD_TITLE,
            texts=[
                SettAvUIString.SOUND_PLAY_TIME_CARD_TEXT_B_CHOOSE,
                SettAvUIString.SOUND_PLAY_TIME_CARD_TEXT_F_CHOOSE,
                SettAvUIString.SOUND_PLAY_TIME_CARD_TEXT_BOTH,
            ],
        )


class ReadSettingGroup(QWidget):
    """朗读 部分, 继承自 QWidget,
    引用时可作 ReadSettGr"""

    def __init__(self):
        super().__init__()

        # 初始化垂直布局
        self.vboxlayout = QVBoxLayout(self)

        # 初始化控件
        self.init_widgets()

        # 控件列表
        self.widget_list = [
            self.read_switch_card,
            self.read_time_card,
        ]

        # 设置布局
        set_widget_to_layout(self.widget_list, self.vboxlayout)
        self.setLayout(self.vboxlayout)

    def init_widgets(self):
        """初始化控件"""

        # 朗读开关
        self.read_switch_card = qfw.SwitchSettingCard(
            FI.SPEAKERS,
            SettAvUIString.READ_SWITCH_CARD_TITLE,
            SettAvUIString.READ_SWITCH_CARD_CONTEXT,
            sett_av_ui_cfg.read_switch,
        )

        # 在何时朗读
        self.read_time_card = qfw.OptionsSettingCard(
            sett_av_ui_cfg.read_time,
            FI.RINGER,
            SettAvUIString.READ_TIME_CARD_TITLE,
            texts=[
                SettAvUIString.READ_TIME_CARD_TEXT_B_CHOOSE,
                SettAvUIString.READ_TIME_CARD_TEXT_F_CHOOSE,
                SettAvUIString.READ_TIME_CARD_TEXT_BOTH,
            ],
        )


class ThemeSettingGroup(QWidget):
    """主题 部分, 继承自 QWidget,
    引用时可作 ThemeSettGr"""

    def __init__(self):
        super().__init__()

        # 初始化垂直布局
        self.vboxlayout = QVBoxLayout(self)

        # 初始化控件
        self.init_widgets()

        # 控件列表
        self.widget_list = [self.dark_light_card, self.window_effort_card]

        # 设置布局
        set_widget_to_layout(self.widget_list, self.vboxlayout)
        self.setLayout(self.vboxlayout)

    def init_widgets(self):
        """初始化控件"""

        # 深浅模式
        self.dark_light_card = qfw.ComboBoxSettingCard(
            sett_av_ui_cfg.dark_light,
            FI.RINGER,
            SettAvUIString.THEME_DARK_LIGHT_CARD_TITLE,
            SettAvUIString.THEME_DARK_LIGHT_CARD_CONTEXT,
            [
                SettAvUIString.THEME_DARK_LIGHT_CARD_TEXT_DARK,
                SettAvUIString.THEME_DARK_LIGHT_CARD_TEXT_LIGHT,
                SettAvUIString.THEME_DARK_LIGHT_CARD_TEXT_AUTO,
            ],
        )

        # 窗口效果
        self.window_effort_card = qfw.ComboBoxSettingCard(
            sett_av_ui_cfg.window_effort,
            FI.RINGER,
            SettAvUIString.THEME_WINDOW_EFFORT_CARD_TITLE,
            SettAvUIString.THEME_WINDOW_EFFORT_CARD_CONTEXT,
            [
                SettAvUIString.THEME_WINDOW_EFFORT_CARD_TEXT_MICA,
                SettAvUIString.THEME_WINDOW_EFFORT_CARD_TEXT_AUTO,
            ],
        )


class HitokotoSettingGroup(QWidget):
    """一言 部分, 继承自 QWidget,
    引用时可作 HitokotoSettGr"""

    def __init__(self):
        super().__init__()

        # 初始化垂直布局
        self.vboxlayout = QVBoxLayout(self)

        # 初始化控件
        self.init_widgets()

        # 控件列表
        self.widget_list = [self.api_web_card, self.renew_time]

        # 设置布局
        set_widget_to_layout(self.widget_list, self.vboxlayout)
        self.setLayout(self.vboxlayout)

    def init_widgets(self):
        """初始化控件"""

        # API接口
        self.api_web_card = qfw.ComboBoxSettingCard(
            sett_av_ui_cfg.hitokoto_api,
            FI.RINGER,
            SettAvUIString.HITOKOTO_API_CARD_TITLE,
            SettAvUIString.HITOKOTO_API_CARD_CONTEXT,
            [SettAvUIString.HITOKOTO_API_CARD_TEXT_HITOKOTO],
        )

        # 刷新时间
        self.renew_time = qfw.RangeSettingCard(
            sett_av_ui_cfg.hitokoto_renew_time,
            FI.DATE_TIME,
            SettAvUIString.HITOKOTO_RENEW_TIME_CARD_TITLE,
            SettAvUIString.HITOKOTO_RENEW_TIME_CARD_CONTEXT,
        )


class SettingAudiovisualUI(QFrame):
    """孙页面:视听( 首选项 的子页面)的基础UI类,
    此页面包含了视觉效果与音频效果等可调整设置选项, 包含五个部分:音乐, 音效, 朗读, 主题, 一言,
    引用时可作 SettAvUI / subsubpage_setting_audiovisual"""

    def __init__(self, parent=None):
        super().__init__(parent)

        from PySide2.QtCore import Qt, QMargins
        from PySide2.QtWidgets import QStackedWidget

        # 初始化顶部导航栏与多页面, 初始化布局
        self.pivot = qfw.Pivot(self)
        self.stackedWidget = QStackedWidget(self)
        self.vboxlayout = QVBoxLayout(self)

        # 添加各项的卡片组
        self.music_interface = MusicSettingGroup()
        self.sound_interface = SoundSettingGroup()
        self.read_interface = ReadSettingGroup()
        self.theme_interface = ThemeSettingGroup()
        self.hitokoto_interface = HitokotoSettingGroup()

        # 添加标签页
        self.add_sub_interface(
            self.music_interface,
            SettAvUIString.MUSIC_SETT_GR_OBJNAME,
            SettAvUIString.MUSIC_SETT_GR_NAVNAME,
        )
        self.add_sub_interface(
            self.sound_interface,
            SettAvUIString.SOUND_SETT_GR_OBJNAME,
            SettAvUIString.SOUND_SETT_GR_NAVNAME,
        )
        self.add_sub_interface(
            self.read_interface,
            SettAvUIString.READ_SETT_GR_OBJNAME,
            SettAvUIString.READ_SETT_GR_NAVNAME,
        )
        self.add_sub_interface(
            self.theme_interface,
            SettAvUIString.THEME_SETT_GR_OBJNAME,
            SettAvUIString.THEME_SETT_GR_NAVNAME,
        )
        self.add_sub_interface(
            self.hitokoto_interface,
            SettAvUIString.HITOKOTO_SETT_GR_OBJNAME,
            SettAvUIString.HITOKOTO_SETT_GR_NAVNAME,
        )

        # 连接信号并初始化当前标签页
        self.stackedWidget.currentChanged.connect(self.on_current_index_changed)
        self.stackedWidget.setCurrentWidget(self.music_interface)
        self.pivot.setCurrentItem(self.music_interface.objectName())

        # 调整布局
        self.vboxlayout.setContentsMargins(QMargins(30, 30, 30, 30))
        self.vboxlayout.addWidget(self.pivot)
        self.vboxlayout.setAlignment(self.pivot, Qt.AlignCenter)
        self.vboxlayout.addWidget(self.stackedWidget)

    def add_sub_interface(self, widget: QWidget, objectName: str, text: str):
        """添加子页面"""

        widget.setObjectName(objectName)
        self.stackedWidget.addWidget(widget)

        # 使用全局唯一的 objectName 作为路由键
        self.pivot.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stackedWidget.setCurrentWidget(widget),
        )

    def on_current_index_changed(self, index):
        """将多页面的切换信号连接到顶部导航栏显示"""

        widget = self.stackedWidget.widget(index)
        self.pivot.setCurrentItem(widget.objectName())
