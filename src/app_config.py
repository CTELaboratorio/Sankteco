"""
应用配置类，用于保存项目的所有可调整设置
引用时可作 AppConfig 
"""

from enum import Enum
from app_const_var import *
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


class SoundPlayTimeEnum(Enum):
    """音效在何时播放枚举"""

    BCHOOSE = "OnlyBChoose"
    FCHOOSE = "OnlyFChoose"
    ALL = "BChoose&FChoose"

    @staticmethod
    def values():
        return [q.value for q in SoundPlayTimeEnum]


class ReadTimeEnum(Enum):
    """在何时朗读枚举"""

    BCHOOSE = "OnlyBChoose"
    FCHOOSE = "OnlyFChoose"
    ALL = "BChoose&FChoose"

    @staticmethod
    def values():
        return [q.value for q in ReadTimeEnum]


class DarkLightEnum(Enum):
    """深浅模式枚举"""

    DARK = "Dark"
    LIGHT = "Light"
    AUTO = "Auto"

    @staticmethod
    def values():
        return [q.value for q in DarkLightEnum]


class AppCommonConfig(qfw.QConfig):
    """应用配置类"""

    # 语言
    language = qfw.OptionsConfigItem(
        AppConfigString.LANGUAGE_GROUP,
        AppConfigString.LANGUAGE_NAME,
        LanguageEnum.ZH_CN,
        qfw.OptionsValidator([LanguageEnum.ZH_CN, LanguageEnum.EO]),
        qfw.EnumSerializer(LanguageEnum),
        restart=True,
    )

    # 动画精美度
    carton_beauty_level = qfw.OptionsConfigItem(
        AppConfigString.BASIC_GROUP,
        AppConfigString.BASIC_CARTON_BEAUTY_LEVEL_NAME,
        BChoooseCartonBeautyEnum.FANCY,
        qfw.OptionsValidator(
            [
                BChoooseCartonBeautyEnum.FANCY,
                BChoooseCartonBeautyEnum.BEAUTY,
                BChoooseCartonBeautyEnum.MID,
                BChoooseCartonBeautyEnum.FAST,
            ]
        ),
        qfw.EnumSerializer(BChoooseCartonBeautyEnum),
        restart=True,
    )

    # 结果推送方式
    show_result_way = qfw.OptionsConfigItem(
        AppConfigString.BASIC_GROUP,
        AppConfigString.BASIC_SHOW_RESULT_WAY_NAME,
        FChooseShowResultWayEnum.MESSAGEBOX,
        qfw.OptionsValidator(
            [
                FChooseShowResultWayEnum.CLASSISLAND,
                FChooseShowResultWayEnum.CLASSWIDGET,
                FChooseShowResultWayEnum.MESSAGEBOX,
            ]
        ),
        qfw.EnumSerializer(FChooseShowResultWayEnum),
        restart=True,
    )

    # 音乐开关
    music_switch = qfw.ConfigItem(
        AppConfigString.AV_GROUP,
        AppConfigString.AV_MUSIC_SWITCH_NAME,
        False,
        qfw.BoolValidator(),
    )

    # 音乐路径
    music_path = qfw.ConfigItem(
        AppConfigString.AV_GROUP,
        AppConfigString.AV_MUSIC_PATH_NAME,
        AssetsPathTXT.APP_DEFAULT_MUSIC_PATH,
        qfw.FolderValidator(),
    )

    # 音乐音量调节
    music_volume = qfw.RangeConfigItem(
        AppConfigString.AV_GROUP,
        AppConfigString.AV_MUSIC_VOLUME_NAME,
        80,
        qfw.RangeValidator(0, 100),
    )

    # 音乐渐入效果
    music_play_smoothly = qfw.RangeConfigItem(
        AppConfigString.AV_GROUP,
        AppConfigString.AV_MUSIC_PLAY_SMOOTHLY_NAME,
        0,
        qfw.RangeValidator(0, 5),
    )

    # 音乐渐出效果
    music_pause_smoothly = qfw.RangeConfigItem(
        AppConfigString.AV_GROUP,
        AppConfigString.AV_MUSIC_PAUSE_SMOOTHLY_NAME,
        0,
        qfw.RangeValidator(0, 5),
    )

    # 音效开关
    sound_switch = qfw.ConfigItem(
        AppConfigString.AV_GROUP,
        AppConfigString.AV_SOUND_SWITCH_NAME,
        True,
        qfw.BoolValidator(),
    )

    # 音效路径
    sound_path = qfw.ConfigItem(
        AppConfigString.AV_GROUP,
        AppConfigString.AV_SOUND_PATH_NAME,
        AssetsPath.APP_DEFAULT_SOUND_PATH,
        qfw.FolderValidator(),
    )

    # 音效在何时播放
    sound_play_time = qfw.OptionsConfigItem(
        AppConfigString.AV_GROUP,
        AppConfigString.AV_SOUND_PLAY_TIME_NAME,
        SoundPlayTimeEnum.ALL,
        qfw.OptionsValidator(
            [
                SoundPlayTimeEnum.BCHOOSE,
                SoundPlayTimeEnum.FCHOOSE,
                SoundPlayTimeEnum.ALL,
            ]
        ),
        qfw.EnumSerializer(SoundPlayTimeEnum),
    )

    # 朗读开关
    read_switch = qfw.ConfigItem(
        AppConfigString.AV_GROUP,
        AppConfigString.AV_READ_SWITCH_NAME,
        True,
        qfw.BoolValidator(),
    )

    # 在何时朗读
    read_time = qfw.OptionsConfigItem(
        AppConfigString.AV_GROUP,
        AppConfigString.AV_READ_TIME_NAME,
        ReadTimeEnum.ALL,
        qfw.OptionsValidator(
            [
                ReadTimeEnum.BCHOOSE,
                ReadTimeEnum.FCHOOSE,
                ReadTimeEnum.ALL,
            ]
        ),
        qfw.EnumSerializer(ReadTimeEnum),
    )

    # 深浅模式
    dark_light = qfw.OptionsConfigItem(
        AppConfigString.AV_GROUP,
        AppConfigString.AV_DARK_LIGHT_NAME,
        DarkLightEnum.AUTO,
        qfw.OptionsValidator(
            [DarkLightEnum.DARK, DarkLightEnum.LIGHT, DarkLightEnum.AUTO]
        ),
        qfw.EnumSerializer(DarkLightEnum),
        restart=True,
    )
