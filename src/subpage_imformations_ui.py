"""
子页面：信息
此页面包含了本项目的相关信息，包含四部分：信息板、支持、语言、更新
引用时可作 InfoUI 
"""

import qfluentwidgets as qfw
from PySide2.QtWidgets import QFrame, QVBoxLayout, QButtonGroup
from app_config import AppCommonConfig
from app_const_var import *


class InformationBoardCardGroup(qfw.GroupHeaderCardWidget):
    """信息板 部分，继承自 上下分组布局卡片 GroupHeaderCardWidget
    引用时可作 InfoBodCard"""

    def __init__(self, parent=None):
        super().__init__(parent)

        # 选项卡组基本设置
        self.setTitle(InfoUIString.INFOBODCARD_TITLE)
        self.setBorderRadius(8)

        # 图片组
        self.apppic_imagelabel = qfw.ImageLabel(
            "../assets/images/imformations_ui_pic.png"
        )

        # 添加组件到分组中
        self.addGroup(None, None, None, self.apppic_imagelabel)
        group = self.addGroup(
            qfw.FluentIcon.INFO, AppString.APP_FULL_NAME, AppString.APP_COPYTYPE, None
        )
        group.setSeparatorVisible(True)


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
            icon=qfw.FluentIcon.DOCUMENT, text=InfoUIString.SUPPTCARD_OFFLINEDOCBUTTON
        )
        self.online_document_button = qfw.PushButton(
            icon=qfw.FluentIcon.SEARCH, text=InfoUIString.SUPPTCARD_ONLINEDOCBUTTON
        )

        # 添加分组到组件中
        self.addGroup(
            qfw.FluentIcon.DOCUMENT, InfoUIString.SUPPTCARD_OFFLINEDOCGROUP, None, self.offline_document_button
        )
        group = self.addGroup(
            qfw.FluentIcon.GLOBE, InfoUIString.SUPPTCARD_ONLINEDOCGROUP, None, self.online_document_button
        )
        group.setSeparatorVisible(True)


class LanguageCardGroup(qfw.GroupHeaderCardWidget):
    """语言 部分，继承自 上下分组布局卡片 GroupHeaderCardWidget
    引用时可作 LangCard"""

    def __init__(self, parent=None):
        super().__init__(parent)

        # 选项卡组基本设置
        self.setTitle(InfoUIString.LANGCARD_TITLE)
        self.setBorderRadius(8)

        # 创建适用于该类的配置实例
        self.app_config = AppCommonConfig()

        # 加载配置文件
        qfw.qconfig.load("../config/appconfig.json", self.app_config)

        # 语言选项卡
        self.languagecard = qfw.ComboBoxSettingCard(
            self.app_config.language,
            qfw.FluentIcon.LANGUAGE,
            InfoUIString.LANGCARD_LANGCARD_TITLE,
            InfoUIString.LANGCARD_LANGCARD_DETAIL,
            ["简体中文", "Esperanto"],
        )

        # 添加分组到组件中
        group = self.addGroup(None, None, None, self.languagecard)
        group.setSeparatorVisible(True)

        # 响应值更改信号
        # self.app_config.language.valueChanged.connect(print)


class UpdateCardGroup(qfw.GroupHeaderCardWidget):
    """更新 部分，继承自 上下分组布局卡片 GroupHeaderCardWidget
    引用时可作 UpdateCard"""

    def __init__(self, parent=None):
        super().__init__(parent)

        # 选项卡组基本设置
        self.setTitle("更新")
        self.setBorderRadius(8)

        # 更新通道单选按钮
        self.update_pipe_radiobutton_release = qfw.RadioButton(text="正式版")
        self.update_pipe_radiobutton_beta = qfw.RadioButton(text="测试版")
        self.update_pipe_radiobutton_group = QButtonGroup(self)
        self.update_pipe_radiobutton_group.addButton(
            self.update_pipe_radiobutton_release
        )
        self.update_pipe_radiobutton_group.addButton(self.update_pipe_radiobutton_beta)
        # 设置默认项
        self.update_pipe_radiobutton_release.setChecked(True)

        # 更新状态
        self.update_status_check_button = qfw.PushButton(
            icon=qfw.FluentIcon.CHECKBOX, text="检查更新"
        )

        # 当前版本
        self.update_version_now = qfw.BodyLabel("version dev")

        # 添加分组到组件中
        self.addGroup(
            qfw.FluentIcon.SETTING,
            "更新通道",
            "选择项目从何通道进行更新",
            self.update_pipe_radiobutton_group,
        )
        self.addGroup(
            qfw.InfoBarIcon.SUCCESS,
            "当前版本已是最新版本",
            None,
            self.update_status_check_button,
        )
        group = self.addGroup(
            qfw.FluentIcon.INFO, "当前版本", None, self.update_version_now
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
        self.language_card = LanguageCardGroup(self)
        self.update_card = UpdateCardGroup(self)

        # 组件布局
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.information_board_card)
        self.main_layout.addWidget(self.support_card)
        self.main_layout.addWidget(self.language_card)
        self.main_layout.addWidget(self.update_card)
