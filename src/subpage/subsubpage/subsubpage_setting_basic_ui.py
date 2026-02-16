"""
孙页面：基本（ 首选项 的子页面）
此页面包含了本项目基本的可调整设置选项，包含三个部分：名单、普通抽选、快速抽选
引用时可作 SettBasicUI / subsubpage_settings_basic
"""

from PySide2.QtWidgets import QFrame, QVBoxLayout, QWidget, QStackedWidget
from PySide2.QtCore import Qt
import qfluentwidgets as qfw
from qfluentwidgets import FluentIcon as FI
from app_const_var import *


class NowNamelistSettingCard(qfw.ExpandGroupSettingCard):
    """当前名单设置组 选项卡，从属于 名单 部分，
    继承自 手风琴设置组卡片  ExpandGroupSettingCard，
    引用时可作 NowNamelistSett"""

    def __init__(self, parent=None):
        super().__init__(
            FI.DOCUMENT,
            SettBasicUIString.NOW_NAMELIST_CARD_TITLE,
            SettBasicUIString.NOW_NAMELIST_CARD_CONTENT,
            parent,
        )

        # 选择名单
        self.choose_namelist_combobox = qfw.ComboBox()
        self.choose_namelist_label = qfw.BodyLabel(
            SettBasicUIString.NOW_NAMELIST_CARD_CHOOSE_LABEL
        )

        # 管理名单内容
        self.now_namelist_detail_button = qfw.PushButton(
            SettBasicUIString.NOW_NAMELIST_CARD_DETAIL_BUTTON
        )
        self.now_namelist_detail_label = qfw.BodyLabel(
            SettBasicUIString.NOW_NAMELIST_CARD_DETAIL_LABEL
        )

        # 标记名单
        self.sign_namelist_button = qfw.PushButton(
            SettBasicUIString.NOW_NAMELIST_CRAD_SIGN_BUTTON
        )
        self.sign_namelist_label = qfw.BodyLabel(
            SettBasicUIString.NOW_NAMELIST_CARD_SIGN_LABEL
        )


class NamelistSettingsGroup(QWidget):
    """名单 部分，继承自 QWidget，
    引用时可作 NamelistSettGr"""

    def __init__(self):
        super().__init__()

        # 初始化垂直布局
        self.vBoxLayout = QVBoxLayout(self)

        # 多名单管理
        self.namelists_create_card = qfw.PushSettingCard(
            text=SettBasicUIString.NAMELISTS_CREATE_CARD_TEXT,
            icon=FI.ROBOT,
            title=SettBasicUIString.NAMELISTS_CREATE_CARD_TITLE,
            content=SettBasicUIString.NAMELISTS_CREATE_CARD_CONTENT,
        )

        # 当前名单设置组
        self.now_namelist_groupcard = NowNamelistSettingCard(self)
