"""
应用配置类，用于保存项目的所有可调整设置
引用时可作 AppConfig 
"""

from enum import Enum
from typing import Type
from app_const_var import *
import qfluentwidgets as qfw


class ValuesMixin:
    """返回Enum类成员value的基类"""

    @classmethod
    def values(cls: Type[Enum]) -> list:  # type: ignore[reportGeneralTypeIssues]
        return [q.value for q in cls.__members__.values()]


class AppEnums:
    """应用枚举类"""

    class LanguageEnum(ValuesMixin, Enum):
        """语言枚举类"""

        ZH_CN = "zh_CN"
        EO = "eo"

    class BChoooseCartonBeautyEnum(ValuesMixin, Enum):
        """动画精美度枚举"""

        FANCY = "100"
        BEAUTY = "75"
        MID = "50"
        FAST = "25"

    class FChooseShowResultWayEnum(ValuesMixin, Enum):
        """结果推送方式枚举"""

        CLASSISLAND = "ClassIsland"
        CLASSWIDGET = "ClassWidget"
        MESSAGEBOX = "MessageBox"

    class SoundPlayTimeEnum(ValuesMixin, Enum):
        """音效在何时播放枚举"""

        BCHOOSE = "OnlyBChoose"
        FCHOOSE = "OnlyFChoose"
        ALL = "BChoose&FChoose"

    class ReadTimeEnum(ValuesMixin, Enum):
        """在何时朗读枚举"""

        BCHOOSE = "OnlyBChoose"
        FCHOOSE = "OnlyFChoose"
        ALL = "BChoose&FChoose"

    class DarkLightEnum(ValuesMixin, Enum):
        """深浅模式枚举"""

        DARK = "Dark"
        LIGHT = "Light"
        AUTO = "Auto"

    class WindowEffortEnum(ValuesMixin, Enum):
        """窗口效果枚举"""

        MICA = "Mica"
        AUTO = "Auto"

    class HitokotoAPIEnum(ValuesMixin, Enum):
        """一言API枚举"""

        HITOKOTO = "https://v1.hitokoto.cn/"


class AppCommonConfig(qfw.QConfig):
    """应用配置类"""

    # 语言
    language = qfw.OptionsConfigItem(
        AppConfigString.LANGUAGE_GROUP,
        AppConfigString.LANGUAGE_NAME,
        AppEnums.LanguageEnum.ZH_CN,
        qfw.OptionsValidator([AppEnums.LanguageEnum.ZH_CN, AppEnums.LanguageEnum.EO]),
        qfw.EnumSerializer(AppEnums.LanguageEnum),
        restart=True,
    )

    # 动画精美度
    carton_beauty_level = qfw.OptionsConfigItem(
        AppConfigString.BASIC_GROUP,
        AppConfigString.BASIC_CARTON_BEAUTY_LEVEL_NAME,
        AppEnums.BChoooseCartonBeautyEnum.FANCY,
        qfw.OptionsValidator(
            [
                AppEnums.BChoooseCartonBeautyEnum.FANCY,
                AppEnums.BChoooseCartonBeautyEnum.BEAUTY,
                AppEnums.BChoooseCartonBeautyEnum.MID,
                AppEnums.BChoooseCartonBeautyEnum.FAST,
            ]
        ),
        qfw.EnumSerializer(AppEnums.BChoooseCartonBeautyEnum),
        restart=True,
    )

    # 结果推送方式
    show_result_way = qfw.OptionsConfigItem(
        AppConfigString.BASIC_GROUP,
        AppConfigString.BASIC_SHOW_RESULT_WAY_NAME,
        AppEnums.FChooseShowResultWayEnum.MESSAGEBOX,
        qfw.OptionsValidator(
            [
                AppEnums.FChooseShowResultWayEnum.CLASSISLAND,
                AppEnums.FChooseShowResultWayEnum.CLASSWIDGET,
                AppEnums.FChooseShowResultWayEnum.MESSAGEBOX,
            ]
        ),
        qfw.EnumSerializer(AppEnums.FChooseShowResultWayEnum),
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
        AppEnums.SoundPlayTimeEnum.ALL,
        qfw.OptionsValidator(
            [
                AppEnums.SoundPlayTimeEnum.BCHOOSE,
                AppEnums.SoundPlayTimeEnum.FCHOOSE,
                AppEnums.SoundPlayTimeEnum.ALL,
            ]
        ),
        qfw.EnumSerializer(AppEnums.SoundPlayTimeEnum),
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
        AppEnums.ReadTimeEnum.ALL,
        qfw.OptionsValidator(
            [
                AppEnums.ReadTimeEnum.BCHOOSE,
                AppEnums.ReadTimeEnum.FCHOOSE,
                AppEnums.ReadTimeEnum.ALL,
            ]
        ),
        qfw.EnumSerializer(AppEnums.ReadTimeEnum),
    )

    # 深浅模式
    dark_light = qfw.OptionsConfigItem(
        AppConfigString.AV_GROUP,
        AppConfigString.AV_DARK_LIGHT_NAME,
        AppEnums.DarkLightEnum.AUTO,
        qfw.OptionsValidator(
            [
                AppEnums.DarkLightEnum.DARK,
                AppEnums.DarkLightEnum.LIGHT,
                AppEnums.DarkLightEnum.AUTO,
            ]
        ),
        qfw.EnumSerializer(AppEnums.DarkLightEnum),
    )

    # 窗口效果
    window_effort = qfw.OptionsConfigItem(
        AppConfigString.AV_GROUP,
        AppConfigString.AV_WINDOW_EFFORT_NAME,
        AppEnums.WindowEffortEnum.AUTO,
        qfw.OptionsValidator(
            [AppEnums.WindowEffortEnum.MICA, AppEnums.WindowEffortEnum.AUTO]
        ),
        qfw.EnumSerializer(AppEnums.WindowEffortEnum),
    )

    #  API接口
    hitokoto_api = qfw.OptionsConfigItem(
        AppConfigString.AV_GROUP,
        AppConfigString.AV_HITOKOTO_API_NAME,
        AppEnums.HitokotoAPIEnum.HITOKOTO,
        qfw.OptionsValidator([AppEnums.HitokotoAPIEnum.HITOKOTO]),
        qfw.EnumSerializer(AppEnums.HitokotoAPIEnum),
    )

    # 刷新时间
    hitokoto_renew_time = qfw.RangeConfigItem(
        AppConfigString.AV_GROUP,
        AppConfigString.AV_HITOKOTO_RENEW_NAME,
        300,
        qfw.RangeValidator(0, 900),
    )
