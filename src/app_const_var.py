"""
常变量文件
本文件是储存项目常量与变量标准值的文件, 不包括ui的字符串
"""

"""
====================
相对路径常量
====================
"""


class AssetsPathTXT:
    """资源相对路径纯文本类"""

    # 图片
    # 图标
    APP_ICON_PATH = "assets/icon/app_icon.png"

    # 项目详细图
    APP_DETAILEDIMAGE_PATH = "assets/images/app_detailed_image.png"

    # 配置文件
    APP_CONFIG = "config/app_config.json"

    # 音频
    # 默认音乐
    APP_DEFAULT_MUSIC_PATH = ""

    # 默认音效
    APP_DEFAULT_SOUND_PATH = "assets/sounds/notice.wav"

    # 链接
    # 加入翻译计划( 语言 孙页面)
    JOIN_TRANSLATION_LINK = ""


class AssetsPath:
    """资源相对路径类"""

    from pathlib import Path

    # 音频
    # 默认音乐
    APP_DEFAULT_MUSIC_PATH = Path(AssetsPathTXT.APP_DEFAULT_MUSIC_PATH)

    # 默认音效
    APP_DEFAULT_SOUND_PATH = Path(AssetsPathTXT.APP_DEFAULT_SOUND_PATH)


"""
====================
Web地址常量
====================
"""


class WebUrl:
    """网址类"""

    # 一言API接口
    HITOKOTO_API_URL = "https://v1.hitokoto.cn/"
    HITOKOTO_API_URL_WITH_FORMAT = "https://v1.hitokoto.cn/?c=i&encode=text"


"""
====================
字符串常量
====================
"""


class AppConfigString:
    """应用配置类 的字符串, 仅包含 app_config.py 相关字符串"""

    # 语言 类字符串
    LANGUAGE_GROUP = "Language"
    LANGUAGE_NAME = "language"

    # 基本 类字符串
    BASIC_GROUP = "Basic"
    BASIC_CARTON_BEAUTY_LEVEL_NAME = "carton_beauty_level"
    BASIC_SHOW_RESULT_WAY_NAME = "show_result_way"

    # 视听 类字符串
    AV_GROUP = "Av"
    AV_MUSIC_SWITCH_NAME = "music_switch"
    AV_MUSIC_PATH_NAME = "music_path"
    AV_MUSIC_VOLUME_NAME = "music_volume"
    AV_MUSIC_PLAY_SMOOTHLY_NAME = "music_play_smoothly"
    AV_MUSIC_PAUSE_SMOOTHLY_NAME = "music_pause_smoothly"
    AV_SOUND_SWITCH_NAME = "sound_switch"
    AV_SOUND_PATH_NAME = "sound_path"
    AV_SOUND_PLAY_TIME_NAME = "sound_play_time"
    AV_READ_SWITCH_NAME = "read_switch"
    AV_READ_TIME_NAME = "read_time"
    AV_DARK_LIGHT_NAME = "dark_light"
    AV_WINDOW_EFFORT_NAME = "window_effort"
    AV_HITOKOTO_API_NAME = "hitokoto_api"
    AV_HITOKOTO_RENEW_NAME = "hitokoto_renew_time"
