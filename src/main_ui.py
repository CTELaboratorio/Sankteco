"""
主页面
此页面是本项目的主要GUI界面，包含与各子页面的交互逻辑、控件响应等
引用时可作 MainUI
"""

from PySide2.QtGui import QIcon
from qfluentwidgets import NavigationItemPosition, FluentWindow
from qfluentwidgets import FluentIcon as FIF
from subpage.subpage_informations_ui import SubpageInformationUI
from app_const_var import *


class MainWindow(FluentWindow):
    """应用程序主窗口，继承自FluentWindow"""

    def __init__(self):
        """初始化主窗口"""
        super().__init__()

        # 初始化窗口设置
        self.initWindow()

        # 导入子页面
        self.subpage_information = SubpageInformationUI(self)
        self.subpage_information.setObjectName(MainUIString.SUBPAGE_INFORMATION_OBJNAME)

        # 初始化导航栏
        self.initNavigation()

    def initNavigation(self):
        """初始化导航栏，添加各个子界面"""
        # 添加子界面
        self.addSubInterface(
            self.subpage_information,
            FIF.INFO,
            MainUIString.SUBPAGE_INFORMATION_NAVNAME,
            NavigationItemPosition.BOTTOM,
        )

    def initWindow(self):
        """初始化窗口设置"""
        # 设置窗口大小
        self.resize(1080, 768)
        # 设置窗口图标
        self.setWindowIcon(QIcon(ImagePath.APP_ICON_PATH))  # type: ignore
        # 设置窗口标题
        self.setWindowTitle(f"{BasicString.APP_FULL_NAME} - {BasicString.APP_VERSION}")
