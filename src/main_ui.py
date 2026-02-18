"""
主页面，
此页面是本项目的主要GUI界面，包含与各子页面的交互逻辑、控件响应等，
引用时可作 MainUI
"""

from PySide2.QtGui import QIcon
from qfluentwidgets import NavigationItemPosition, FluentWindow
from qfluentwidgets import FluentIcon as FI
from subpage.informations_ui import InformationUI
from subpage.settings_ui import SettingsUI
from subpage.subsubpage.setting_basic_ui import SettingBasicUI
from app_const_var import *


class MainWindow(FluentWindow):
    """应用程序主窗口，继承自FluentWindow"""

    def __init__(self):
        """初始化主窗口"""
        super().__init__()

        # 初始化窗口设置
        self.init_window()

        # 导入子页面
        self.subpage_information = InformationUI(self)
        self.subpage_settings = SettingsUI(self)
        self.subsubpage_setting_basic = SettingBasicUI(self)
        self.subpage_information.setObjectName(MainUIString.SUBPAGE_INFORMATION_OBJNAME)
        self.subpage_settings.setObjectName(MainUIString.SUBPAGE_SETTINGS_OBJNAME)
        self.subsubpage_setting_basic.setObjectName(
            MainUIString.SUBSUBPAGE_SETTIING_BASIC_OBJNAME
        )

        # 初始化导航栏
        self.init_navigation()

        # 连接设置子页面信号
        self.subpage_settings.to_basic_card.clicked.connect(lambda: self.switchTo(self.subsubpage_setting_basic))  # type: ignore

    def init_navigation(self):
        """初始化导航栏，添加各个子界面"""
        # 添加子界面
        self.addSubInterface(
            self.subpage_settings,
            FI.SETTING,
            MainUIString.SUBPAGE_SETTINGS_NAVNAME,
            NavigationItemPosition.BOTTOM,
        )
        self.addSubInterface(
            self.subsubpage_setting_basic,
            FI.BRIGHTNESS,
            MainUIString.SUBSUBPAGE_SETTIING_BASIC_NAVNAME,
            parent=self.subpage_settings,
        )
        self.addSubInterface(
            self.subpage_information,
            FI.INFO,
            MainUIString.SUBPAGE_INFORMATION_NAVNAME,
            NavigationItemPosition.BOTTOM,
        )

    def init_window(self):
        """初始化窗口设置"""
        # 设置窗口大小
        self.resize(1080, 768)
        # 设置窗口图标
        self.setWindowIcon(QIcon(AssetsPath.APP_ICON_PATH))  # type: ignore
        # 设置窗口标题
        self.setWindowTitle(f"{BasicString.APP_FULL_NAME} - {BasicString.APP_VERSION}")
