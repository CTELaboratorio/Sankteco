"""
主页面，
此页面是本项目的主要GUI界面，包含与各子页面的交互逻辑、控件响应等，
引用时可作 MainUI
"""

import asyncio
from qfluentwidgets import FluentWindow
from qfluentwidgets import FluentIcon as FI
from app_const_var import MainUIString, BasicString, AssetsPathTXT


class MainWindow(FluentWindow):
    """应用程序主窗口，继承自FluentWindow"""

    def __init__(self):
        """初始化主窗口"""
        super().__init__()

        # 运行导入子页面的asyncio程序
        asyncio.run(self.import_subpage_main())

        # 初始化窗口设置
        self.init_window()

        # 初始化导航栏
        self.init_navigation()

        # 连接设置子页面信号
        self.subpage_settings.to_basic_card.clicked.connect(lambda: self.switchTo(self.subsubpage_setting_basic))  # type: ignore
        self.subpage_settings.to_audiovisual_card.clicked.connect(lambda: self.switchTo(self.subsubpage_setting_audiovisual))  # type: ignore
        self.subpage_settings.to_language_card.clicked.connect(lambda:self.switchTo(self.subsubpage_setting_language))  # type: ignore

    async def import_subpage_information(self):
        """导入并重命名 信息 子页面的协程"""
        from subpage.informations_ui import InformationUI

        self.subpage_information = InformationUI(self)
        self.subpage_information.setObjectName(MainUIString.SUBPAGE_INFORMATION_OBJNAME)

    async def import_subpage_settings(self):
        """导入并重命名 设置 子页面其及所有孙页面的协程"""
        from subpage.settings_ui import SettingsUI
        from subpage.subsubpage.setting_basic_ui import SettingBasicUI
        from subpage.subsubpage.setting_audiovisual_ui import SettingAudiovisualUI
        from subpage.subsubpage.setting_language_ui import SettingLanguageUI

        # 设置 子页面
        self.subpage_settings = SettingsUI(self)
        self.subpage_settings.setObjectName(MainUIString.SUBPAGE_SETTINGS_OBJNAME)

        # 基础 孙页面
        self.subsubpage_setting_basic = SettingBasicUI(self)
        self.subsubpage_setting_basic.setObjectName(
            MainUIString.SUBSUBPAGE_SETTIING_BASIC_OBJNAME
        )

        # 视听 孙页面
        self.subsubpage_setting_audiovisual = SettingAudiovisualUI(self)
        self.subsubpage_setting_audiovisual.setObjectName(
            MainUIString.SUBSUBPAGE_SETTIING_AUDIOVISUAL_OBJNAME
        )

        # 语言 孙页面
        self.subsubpage_setting_language = SettingLanguageUI(self)
        self.subsubpage_setting_language.setObjectName(
            MainUIString.SUBSUBPAGE_SETTIING_LANGUAGE_OBJNAME
        )

    async def import_subpage_main(self):
        """导入子页面的基础函数"""

        # 创建并发执行任务
        await asyncio.gather(
            self.import_subpage_information(),
            self.import_subpage_settings(),
        )

    def init_navigation(self):
        """初始化导航栏，添加各个子界面"""
        from qfluentwidgets import NavigationItemPosition

        # 添加子界面及各自的孙页面
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
            self.subsubpage_setting_audiovisual,
            FI.MEDIA,
            MainUIString.SUBSUBPAGE_SETTIING_AUDIOVISUAL_NAVNAME,
            parent=self.subpage_settings,
        )
        self.addSubInterface(
            self.subsubpage_setting_language,
            FI.LANGUAGE,
            MainUIString.SUBSUBPAGE_SETTIING_LANGUAGE_NAVNAME,
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
        from PySide2.QtGui import QIcon

        # 设置窗口大小
        self.resize(1080, 768)
        # 设置窗口图标
        self.setWindowIcon(QIcon(AssetsPathTXT.APP_ICON_PATH))  # type: ignore
        # 设置窗口标题
        self.setWindowTitle(f"{BasicString.APP_FULL_NAME} - {BasicString.APP_VERSION}")
