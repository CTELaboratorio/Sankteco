"""
应用配置类，用于保存项目的所有可调整设置
"""

from enum import Enum
import qfluentwidgets as qfw

class AppCommonConfig(qfw.QConfig):
    """应用配置类"""

    # 语言
    language = qfw.OptionsConfigItem(
        "Language",
        "Language",
        "简体中文",
        qfw.OptionsValidator(["简体中文", "Esperanto"]),
        restart=True
    )