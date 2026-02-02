"""
子页面：信息
此页面包含了本项目的相关信息，包含四部分：信息板、支持、语言、更新
引用时可作 InfoUI 
"""

from PySide2.QtWidgets import QFrame, QVBoxLayout, QWidget
from PySide2.QtCore import Qt
import qfluentwidgets as qfw
from qfluentwidgets import FluentIcon as FIF
from app_config import AppCommonConfig
from app_const_var import *


class InformationBoardCardGroup(qfw.ElevatedCardWidget):
    """信息板 部分，继承自 卡片组件 ElevatedCardWidget
    引用时可作 InfoBodCard"""

    def __init__(self, parent=None):
        super().__init__(parent)
        
        # 图片文本
        self.apppic_imagelabel = qfw.ImageLabel(
            "../assets/images/imformations_ui_pic.png", 
            self
        )
        self.apppic_imagelabel.scaledToHeight(320)
        self.apppic_imagelabel.scaledToWidth(640)

        # 项目信息
        self.infotext_bodylabel = qfw.BodyLabel(BasicString.APP_FULL_NAME, self)
        self.infotext_captionlabel = qfw.CaptionLabel(BasicString.APP_COPYTYPE, self)

        # 组件布局
        self.vlayout = QVBoxLayout(self)
        self.vlayout.setAlignment(self.vlayout, Qt.AlignLeft)
        self.vlayout.addStretch(1)
        self.vlayout.addWidget(self.apppic_imagelabel, 0, Qt.AlignCenter)
        self.vlayout.addStretch(1)
        self.vlayout.addWidget(self.infotext_bodylabel, 0, Qt.AlignLeft)
        self.vlayout.addStretch(1)
        self.vlayout.addWidget(self.infotext_captionlabel, 0, Qt.AlignLeft)


class SupportCardGroup(qfw.GroupHeaderCardWidget):
    """支持 部分，继承自 上下分组布局卡片 GroupHeaderCardWidget
    引用时可作 SupptCard"""

    def __init__(self, parent=None):
        super().__init__(parent)

        # 选项卡组基本设置
        self.setTitle(InfoUIString.SUPPTCARD_TITLE)
        self.setBorderRadius(8)

        # 帮助文档按钮
        self.offline_document_button = qfw.PushButton(
            icon=FIF.DOCUMENT, text=InfoUIString.SUPPTCARD_OFFLINEDOCBUTTON
        )
        self.online_document_button = qfw.PushButton(
            icon=FIF.SEARCH, text=InfoUIString.SUPPTCARD_ONLINEDOCBUTTON
        )

        # 添加分组到组件中
        self.addGroup(
            FIF.DOCUMENT,
            InfoUIString.SUPPTCARD_OFFLINEDOCGROUPTITLE,
            InfoUIString.SUPPTCARD_OFFLINEDOCGROUPCONTEXT,
            self.offline_document_button,
        )
        group = self.addGroup(
            FIF.GLOBE,
            InfoUIString.SUPPTCARD_ONLINEDOCGROUPTITLE,
            InfoUIString.SUPPTCARD_ONLINEDOCGROUPCONTEXT,
            self.online_document_button,
        )
        group.setSeparatorVisible(True)


"""
class LanguageCardGroup(QVBoxLayout):
    ""语言 部分，继承自 QWidget
    引用时可作 LangCard""

    def __init__(self, parent=None):
        super().__init__(parent)

        # 创建适用于该类的配置实例
        self.app_config = AppCommonConfig()

        # 加载配置文件
        qfw.qconfig.load("../config/appconfig.json", self.app_config)

        # 语言选项卡
        self.languagecard = qfw.ComboBoxSettingCard(
            self.app_config.language,
            FIF.LANGUAGE,
            InfoUIString.LANGCARD_LANGCARD_TITLE,
            InfoUIString.LANGCARD_LANGCARD_DETAIL,
            ["简体中文", "Esperanto"],
        )

        # 响应值更改信号
        # self.app_config.language.valueChanged.connect(print)
"""


class UpdateCardGroup(qfw.GroupHeaderCardWidget):
    """更新 部分，继承自 上下分组布局卡片 GroupHeaderCardWidget
    引用时可作 UpdateCard"""

    def __init__(self, parent=None):
        super().__init__(parent)

        # 选项卡组基本设置
        self.setTitle(InfoUIString.UPDATECARD_TITLE)
        self.setBorderRadius(8)

        # 更新通道下拉框
        self.update_pipe_combobox = qfw.ComboBox()
        self.update_pipe_combobox_item = [
            InfoUIString.UPDATECARD_PIPE_RELEASE,
            InfoUIString.UPDATECARD_PIPE_BETA,
        ]
        self.update_pipe_combobox.addItems(self.update_pipe_combobox_item)

        # 更新状态
        self.update_status_check_button = qfw.PushButton(
            icon=FIF.CHECKBOX, text=InfoUIString.UPDATECARD_UPDATESTATUS
        )

        # 添加分组到组件中
        self.addGroup(
            FIF.SETTING,
            InfoUIString.UPDATECARD_PIPEGROUP_TITLE,
            InfoUIString.UPDATECARD_PIPEGROUP_DETAIL,
            self.update_pipe_combobox,
        )
        group = self.addGroup(
            qfw.InfoBarIcon.SUCCESS,
            InfoUIString.UPDATECARD_VERSTATUSGROUP_TITLE,
            BasicString.APP_VERSION,
            self.update_status_check_button,
        )
        group.setSeparatorVisible(True)

        # 响应值更改信号
        """
        self.update_pipe_radiobutton_group.buttonToggled.connect(
            lambda button: print(button.text())
        )"""


class SubpageInformationUI(QFrame):
    """子页面基础ui类"""

    def __init__(self, parent=None):
        """初始化子页面"""
        super().__init__(parent)

        # 依次显示卡片组件
        self.information_board_card = InformationBoardCardGroup(self)
        self.support_card = SupportCardGroup(self)
        # self.language_card = LanguageCardGroup(self)
        self.update_card = UpdateCardGroup(self)

        # 组件布局
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.information_board_card)
        self.main_layout.addWidget(self.support_card)
        # self.main_layout.addWidget(self.language_card)
        self.main_layout.addWidget(self.update_card)
