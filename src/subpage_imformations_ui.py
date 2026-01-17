"""
子页面：信息
此页面包含了本项目的相关信息，包含四部分：信息板、支持、语言、更新
"""

import qfluentwidgets as qfw
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout
from PySide2.QtCore import Qt
from app_config import AppCommonConfig


class InformationBoardCardGroup(qfw.GroupHeaderCardWidget):
    """ 信息板 部分，继承自 上下分组布局卡片 GroupHeaderCardWidget """

    def __init__(self, parent=None):
        super().__init__(parent)
        
        # 选项卡组基本设置
        self.setTitle("信息板")
        self.setBorderRadius(8)

        # 图片组
        self.apppic_imagelabel = qfw.ImageLabel("../assets/images/imformations_ui_pic.png")
        
        # 添加组件到分组中
        self.addGroup(None, None, None, self.apppic_imagelabel)
        group = self.addGroup(qfw.FluentIcon.INFO, "祈福Prays", "Copyleft,2023~2026,HXES.As is.", None)
        group.setSeparatorVisible(True)


class SupportCardGroup(qfw.GroupHeaderCardWidget):
    """ 支持 部分，继承自 上下分组布局卡片 GroupHeaderCardWidget """

    def __init__(self, parent=None):
        super().__init__(parent)
        
        # 选项卡组基本设置
        self.setTitle("支持")
        self.setBorderRadius(8)

        # 帮助文档按钮
        self.offline_document_button = qfw.PushButton(icon=qfw.FluentIcon.DOCUMENT, text="查看")
        self.online_document_button = qfw.PushButton(icon=qfw.FluentIcon.SEARCH, text="查看")

        # 添加分组到组件中
        self.addGroup(qfw.FluentIcon.DOCUMENT, "离线帮助文档", None, self.offline_document_button)
        group = self.addGroup(qfw.FluentIcon.GLOBE, "在线帮助文档", None, self.online_document_button)
        group.setSeparatorVisible(True)


class LanguageCardGroup(qfw.GroupHeaderCardWidget):
    """ 语言 部分，继承自 上下分组布局卡片 GroupHeaderCardWidget """
    def __init__(self, parent=None):
        super().__init__(parent)

        # 选项卡组基本设置
        self.setTitle("语言")
        self.setBorderRadius(8)

        # 创建适用于该类的配置实例
        self.app_config = AppCommonConfig()

        # 加载配置文件
        qfw.qconfig.load("../config/appconfig.json", self.app_config)

        # 语言选项卡
        self.languagecard = qfw.ComboBoxSettingCard(
            self.app_config.language,
            qfw.FluentIcon.LANGUAGE,
            "语言选项",
            "从此处更改界面语言",
            ["简体中文", "Esperanto"],
        )

        # 添加分组到组件中
        group = self.addGroup(None, None, None, self.languagecard)
        group.setSeparatorVisible(True)
        