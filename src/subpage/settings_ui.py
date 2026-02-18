"""
子页面：首选项，
此页面包含了本项目的可调整设置选项，包含六个孙页面：基本、视听、联动、语言、更新、调试，
引用时可作 SettUI / subpage_settings
"""

from PySide2.QtWidgets import QFrame, QVBoxLayout
from PySide2.QtCore import Qt
import qfluentwidgets as qfw
from qfluentwidgets import FluentIcon as FI
from app_const_var import *


class SettingsUI(QFrame):
    """子页面：首选项的基础UI类，
    此页面包含了本项目的可调整设置选项，包含六个孙页面：基本、视听、联动、语言、更新、调试，
    引用时可作 SettUI / subpage_settings"""

    def __init__(self, parent=None):
        super().__init__(parent)

        # 提示文本
        self.tip_titlelabel = qfw.TitleLabel("在此处调整程序设置")
        self.tip_strongbodylabel = qfw.StrongBodyLabel(
            "从下面的孙页面中选择其一以更改相关选项"
        )

        # 孙页面指向卡片
        self.to_basic_card = qfw.PrimaryPushSettingCard(
            "跳转",
            FI.BRIGHTNESS,
            "基本",
            "更改基本设置",
        )
        self.to_audiovisual_card = qfw.PrimaryPushSettingCard(
            "跳转",
            FI.MEDIA,
            "视听",
            "更改背景音乐、音效、朗读等设置",
        )
        self.to_linkage_card = qfw.PrimaryPushSettingCard(
            "跳转",
            FI.CONNECT,
            "联动",
            "更改与课表软件的联动设置",
        )
        self.to_language_card = qfw.PrimaryPushSettingCard(
            "跳转",
            FI.LANGUAGE,
            "语言",
            "更改界面显示语言",
        )
        self.to_update_card = qfw.PrimaryPushSettingCard(
            "跳转",
            FI.UPDATE,
            "更新",
            "更新程序",
        )
        self.to_debug_card = qfw.PrimaryPushSettingCard(
            "跳转",
            FI.IOT,
            "调试",
            "高级调试选项",
        )

        # 页面布局
        self.vboxlayout = QVBoxLayout(self)
        self.label_list = [self.tip_titlelabel, self.tip_strongbodylabel]
        self.widget_list = [
            self.to_basic_card,
            self.to_audiovisual_card,
            self.to_linkage_card,
            self.to_language_card,
            self.to_update_card,
            self.to_debug_card,
        ]
        
        # 批量导入组件
        for label in self.label_list:
            self.vboxlayout.addWidget(label)
            self.vboxlayout.setAlignment(label, Qt.AlignCenter)
        for widget in self.widget_list:
            self.vboxlayout.addWidget(widget)
