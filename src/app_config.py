"""
应用配置类，用于保存项目的所有可调整设置
"""

from enum import Enum
import qfluentwidgets as qfw


class LanguageEnum(Enum):
    """语言枚举类"""

    ZH_CN = "zh_cn"
    EO = "eo"

    @staticmethod
    def values():
        return [q.value for q in LanguageEnum]


class BChoooseCartonBeautyEnum(Enum):
    """动画精美度枚举"""

    FANCY = "100"
    BEAUTY = "75"
    MID = "50"
    FAST = "25"

    @staticmethod
    def values():
        return [q.value for q in BChoooseCartonBeautyEnum]


class FChooseShowResultWayEnum(Enum):
    """结果推送方式枚举"""

    CLASSISLAND = "ClassIsland"
    CLASSWIDGET = "ClassWidget"
    MESSAGEBOX = "MessageBox"

    @staticmethod
    def values():
        return [q.value for q in FChooseShowResultWayEnum]


class AppCommonConfig(qfw.QConfig):
    """应用配置类"""

    # 语言
    language = qfw.OptionsConfigItem(
        "Language",
        "Language",
        LanguageEnum.ZH_CN,
        qfw.OptionsValidator([LanguageEnum.ZH_CN, LanguageEnum.EO]),
        restart=True,
    )

    # 动画精美度
    carton_beauty_level = qfw.OptionsConfigItem(
        "Basic",
        "carton_beauty_level",
        BChoooseCartonBeautyEnum.FANCY,
        qfw.OptionsValidator(
            [
                BChoooseCartonBeautyEnum.FANCY,
                BChoooseCartonBeautyEnum.BEAUTY,
                BChoooseCartonBeautyEnum.MID,
                BChoooseCartonBeautyEnum.FAST,
            ]
        ),
        restart=True,
    )

    # 结果推送方式
    show_result_way = qfw.OptionsConfigItem(
        "Basic",
        "show_result_way",
        FChooseShowResultWayEnum.MESSAGEBOX,
        qfw.OptionsValidator(
            [
                FChooseShowResultWayEnum.CLASSISLAND,
                FChooseShowResultWayEnum.CLASSWIDGET,
                FChooseShowResultWayEnum.MESSAGEBOX,
            ]
        ),
        restart=True,
    )

    # 音乐开关
    music_switch = qfw.ConfigItem("Av", "music_switch", False, qfw.BoolValidator())

    # 音乐音量调节
    music_volume = qfw.RangeConfigItem(
        "Av", "music_volume", 80, qfw.RangeValidator(0, 100)
    )

    # 音乐渐入效果
    music_play_smoothly = qfw.RangeConfigItem(
        "Av", "music_play_smoothly", 0, qfw.RangeValidator(0, 5)
    )

    # 音乐渐出效果
    music_pause_smoothly = qfw.RangeConfigItem(
        "Av", "music_pause_smoothly", 0, qfw.RangeValidator(0, 5)
    )
