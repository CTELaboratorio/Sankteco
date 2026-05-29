"""
子页面:首选项, 
此页面包含了本项目的可调整设置选项, 包含六个孙页面:基本, 视听, 联动, 语言, 更新, 调试, 
引用时可作 SettUI / subpage_settings
"""

from PySide2.QtWidgets import QFrame
import qfluentwidgets as qfw
from qfluentwidgets import FluentIcon as FI
from ui.ui_str import SettUIString


class SettingsUI(QFrame):
    """子页面:首选项的基础UI类,
    此页面包含了本项目的可调整设置选项, 包含六个孙页面:基本, 视听, 联动, 语言, 更新, 调试,
    引用时可作 SettUI / subpage_settings"""

    def __init__(self, parent=None):
        super().__init__(parent)
        from PySide2.QtCore import Qt, QMargins
        from PySide2.QtWidgets import QVBoxLayout

        # 页面布局
        self.vboxlayout = QVBoxLayout(self)

        # 初始化控件
        self.init_widgets()

        # 控件列表
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

        # 调整布局
        self.vboxlayout.setContentsMargins(QMargins(30, 30, 30, 30))

    def init_widgets(self):
        """初始化控件"""

        # 提示文本
        self.tip_titlelabel = qfw.TitleLabel(SettUIString.TIP_TITLE)
        self.tip_strongbodylabel = qfw.StrongBodyLabel(SettUIString.TIP_CONTEXT)

        # 孙页面指向卡片
        self.to_basic_card = qfw.PrimaryPushSettingCard(
            SettUIString.TO_BASIC_CARD_TEXT,
            FI.BRIGHTNESS,
            SettUIString.TO_BASIC_CARD_TITLE,
            SettUIString.TO_BASIC_CARD_CONTEXT,
        )
        self.to_audiovisual_card = qfw.PrimaryPushSettingCard(
            SettUIString.TO_AUDIOVISUAL_CARD_TEXT,
            FI.MEDIA,
            SettUIString.TO_AUDIOVISUAL_CARD_TITLE,
            SettUIString.TO_AUDIOVISUAL_CARD_CONTEXT,
        )
        self.to_linkage_card = qfw.PrimaryPushSettingCard(
            SettUIString.TO_LINKAGE_CARD_TEXT,
            FI.CONNECT,
            SettUIString.TO_LINKAGE_CARD_TITLE,
            SettUIString.TO_LINKAGE_CARD_CONTEXT,
        )
        self.to_language_card = qfw.PrimaryPushSettingCard(
            SettUIString.TO_LANGUAGE_CARD_TEXT,
            FI.LANGUAGE,
            SettUIString.TO_LANGUAGE_CARD_TITLE,
            SettUIString.TO_LANGUAGE_CARD_CONTEXT,
        )
        self.to_update_card = qfw.PrimaryPushSettingCard(
            SettUIString.TO_UPDATE_CARD_TEXT,
            FI.UPDATE,
            SettUIString.TO_UPDATE_CARD_TITLE,
            SettUIString.TO_UPDATE_CARD_CONTEXT,
        )
        self.to_debug_card = qfw.PrimaryPushSettingCard(
            SettUIString.TO_DEBUG_CARD_TEXT,
            FI.IOT,
            SettUIString.TO_DEBUG_CARD_TITLE,
            SettUIString.TO_DEBUG_CARD_CONTEXT,
        )
