"""
孙页面:视听( 首选项 的子页面)的逻辑文件, 
引用时可作 SettAvLogic / subsubpage_setting_audiovisual_logic
"""

from enum import Enum
import qfluentwidgets as qfw
from ui.settings_ui.settings_audiovisual_ui import SettingsAudiovisualUI, sett_av_ui_cfg
from app_config import AppEnums
from app_const_var import AssetsPathTXT


class SettingsAudiovisualLogic(SettingsAudiovisualUI):
    """孙页面:视听( 首选项 的子页面)的基础逻辑类,
    引用时可作 SettAvLogic / setting_audiovisual_logic"""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.cfg = sett_av_ui_cfg

        # 初始化信号连接函数
        self.singal_connection()

    def singal_connection(self):
        """信号连接函数"""

        self.cfg.dark_light.valueChanged.connect(self.change_theme)  # type: ignore

    def change_theme(self, mode: Enum):
        """更改主题函数"""

        if mode == AppEnums.DarkLightEnum.LIGHT:
            qfw.setTheme(qfw.Theme.LIGHT)
        elif mode == AppEnums.DarkLightEnum.DARK:
            qfw.setTheme(qfw.Theme.DARK)
        elif mode == AppEnums.DarkLightEnum.AUTO:
            qfw.setTheme(qfw.Theme.AUTO)

        # 持久化配置
        qfw.qconfig.save()


def apply_theme_from_config():
    """根据配置文件中的 dark_light 设置应用全局主题"""
    mode = sett_av_ui_cfg.dark_light.value
    if mode == AppEnums.DarkLightEnum.LIGHT:
        qfw.setTheme(qfw.Theme.LIGHT)
    elif mode == AppEnums.DarkLightEnum.DARK:
        qfw.setTheme(qfw.Theme.DARK)
    elif mode == AppEnums.DarkLightEnum.AUTO:
        qfw.setTheme(qfw.Theme.AUTO)
    else:
        # 默认深色主题
        qfw.setTheme(qfw.Theme.DARK)
