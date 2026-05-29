"""
主页面, 
此页面是本项目的主要GUI界面, 包含与各子页面的交互逻辑, 控件响应等, 
引用时可作 MainUI
"""

import asyncio
from qfluentwidgets import FluentWindow
from qfluentwidgets import FluentIcon as FI
from app_const_var import AssetsPathTXT
from .ui_str import MainUIString, BasicString


class MainWindow(FluentWindow):
    """应用程序主窗口, 继承自FluentWindow"""

    def __init__(self):
        """初始化主窗口"""
        super().__init__()

        # 运行导入子页面的asyncio程序
        asyncio.run(self.import_ui())

        # 初始化窗口设置
        self.init_window()

        # 初始化导航栏
        self.init_navigation()

        # 连接设置子页面信号
        self.settings_ui.to_basic_card.clicked.connect(lambda: self.switchTo(self.settings_basic_ui))  # type: ignore
        self.settings_ui.to_audiovisual_card.clicked.connect(lambda: self.switchTo(self.settings_audiovisual_ui))  # type: ignore
        self.settings_ui.to_language_card.clicked.connect(lambda: self.switchTo(self.settings_language_ui))  # type: ignore

    async def import_information_ui(self):
        """导入并重命名 信息 子页面的协程"""
        from ui.informations_ui.informations_ui import InformationUI

        self.information_ui = InformationUI(self)
        self.information_ui.setObjectName(MainUIString.SUBPAGE_INFORMATION_OBJNAME)

    async def import_settings_ui(self):
        """导入并重命名 设置 子页面其及所有孙页面的协程"""
        from ui.settings_ui.settings_ui import SettingsUI
        from ui.settings_ui.settings_basic_ui import SettingsBasicUI
        from ui.settings_ui.settings_audiovisual_ui import SettingsAudiovisualUI
        from ui.settings_ui.settings_language_ui import SettingsLanguageUI

        # 设置 子页面
        self.settings_ui = SettingsUI(self)
        self.settings_ui.setObjectName(MainUIString.SUBPAGE_SETTINGS_OBJNAME)

        # 基础 孙页面
        self.settings_basic_ui = SettingsBasicUI(self)
        self.settings_basic_ui.setObjectName(
            MainUIString.SUBSUBPAGE_SETTIING_BASIC_OBJNAME
        )

        # 视听 孙页面
        self.settings_audiovisual_ui = SettingsAudiovisualUI(self)
        self.settings_audiovisual_ui.setObjectName(
            MainUIString.SUBSUBPAGE_SETTIING_AUDIOVISUAL_OBJNAME
        )

        # 语言 孙页面
        self.settings_language_ui = SettingsLanguageUI(self)
        self.settings_language_ui.setObjectName(
            MainUIString.SUBSUBPAGE_SETTIING_LANGUAGE_OBJNAME
        )

    async def import_pray_ui(self):
        """导入并重命名 祈福 子页面的协程"""
        from ui.pray_ui.pray_ui import PrayUI

        # 祈福 子页面
        self.pray_ui = PrayUI(self)
        self.pray_ui.setObjectName(MainUIString.SUBPAGE_PRAY_OBJNAME)

    async def import_ui(self):
        """导入子页面的基础函数"""

        # 创建并发执行任务
        await asyncio.gather(
            self.import_pray_ui(),
            self.import_information_ui(),
            self.import_settings_ui(),
        )

    def init_navigation(self):
        """初始化导航栏, 添加各个子界面"""
        from qfluentwidgets import NavigationItemPosition

        # 添加子界面及各自的孙页面
        self.addSubInterface(
            self.pray_ui,
            FI.QUESTION,
            MainUIString.SUBPAGE_PRAY_NAVNAME,
            NavigationItemPosition.TOP,
        )
        self.addSubInterface(
            self.settings_ui,
            FI.SETTING,
            MainUIString.SUBPAGE_SETTINGS_NAVNAME,
            NavigationItemPosition.BOTTOM,
        )
        self.addSubInterface(
            self.settings_basic_ui,
            FI.BRIGHTNESS,
            MainUIString.SUBSUBPAGE_SETTIING_BASIC_NAVNAME,
            parent=self.settings_ui,
        )
        self.addSubInterface(
            self.settings_audiovisual_ui,
            FI.MEDIA,
            MainUIString.SUBSUBPAGE_SETTIING_AUDIOVISUAL_NAVNAME,
            parent=self.settings_ui,
        )
        self.addSubInterface(
            self.settings_language_ui,
            FI.LANGUAGE,
            MainUIString.SUBSUBPAGE_SETTIING_LANGUAGE_NAVNAME,
            parent=self.settings_ui,
        )
        self.addSubInterface(
            self.information_ui,
            FI.INFO,
            MainUIString.SUBPAGE_INFORMATION_NAVNAME,
            NavigationItemPosition.BOTTOM,
        )

    def init_window(self):
        """初始化窗口设置"""
        from PySide2.QtGui import QIcon

        # 设置窗口大小
        self.resize(1080, 768)
        # 设置窗口图标
        self.setWindowIcon(QIcon(AssetsPathTXT.APP_ICON_PATH))  # type: ignore
        # 设置窗口标题
        self.setWindowTitle(f"{BasicString.APP_FULL_NAME} - {BasicString.APP_VERSION}")
