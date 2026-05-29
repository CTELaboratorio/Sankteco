"""
孙页面：语言（ 首选项 的子页面），
此页面包含了程序显示语言的可调整设置选项，包含一个部分：语言，
引用时可作 SettLangUI / subsubpage_setting_language
"""

from PySide2.QtWidgets import (
    QFrame,
    QLayout,
)
import qfluentwidgets as qfw
from qfluentwidgets import FluentIcon as FI
from app_const_var import AssetsPathTXT
from ui.ui_str import SettLangUIString
from app_config import AppCommonConfig

# 加载配置文件
sett_lang_ui_cfg = AppCommonConfig()
qfw.qconfig.load(AssetsPathTXT.APP_CONFIG, sett_lang_ui_cfg)


def set_widget_to_layout(wlist: list, layout: QLayout):
    """设置布局的通用函数"""
    for widget in wlist:
        layout.addWidget(widget)


class SettingsLanguageUI(QFrame):
    """孙页面：语言（ 首选项 的子页面）的基础UI类，
    此页面包含了程序显示语言的可调整设置选项，包含一个部分：语言，
    引用时可作 SettLangUI / settings_language"""

    def __init__(self, parent=None):
        super().__init__(parent)

        from PySide2.QtCore import QMargins
        from PySide2.QtWidgets import QVBoxLayout

        # 初始化垂直布局
        self.vboxlayout = QVBoxLayout(self)
        self.vboxlayout.setContentsMargins(QMargins(30, 30, 30, 30))

        # 初始化控件
        self.init_widgets()

        # 控件列表
        self.widget_list = [self.screen_language, self.join_translation]

        # 设置布局
        set_widget_to_layout(self.widget_list, self.vboxlayout)

    def init_widgets(self):
        """初始化控件"""

        # 语言选择
        self.screen_language = qfw.ComboBoxSettingCard(
            sett_lang_ui_cfg.language,
            FI.LANGUAGE,
            SettLangUIString.SCREEN_LANGUAGE_TITLE,
            SettLangUIString.SCREEN_LANGUAGE_CONTEXT,
            [
                SettLangUIString.SCREEN_LANGUAGE_TEXT_ZH_CN,
                SettLangUIString.SCREEN_LANGUAGE_TEXT_EO,
            ],
        )

        # 加入翻译计划
        self.join_translation = qfw.HyperlinkCard(
            AssetsPathTXT.JOIN_TRANSLATION_LINK,
            SettLangUIString.JOIN_TRANSLATION_HYPERLINK_TEXT,
            FI.CLOUD,
            SettLangUIString.JOIN_TRANSLATION_TITLE,
            SettLangUIString.JOIN_TRANSLATION_CONTEXT,
        )
