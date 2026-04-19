"""
本文件是储存项目常量与变量标准值的文件
"""

import gettext
import json

# 读取配置文件以获取语言配置
with open("config/app_config.json", "r", encoding="utf-8") as f:
    json_data = json.load(f)
    language_config = json_data["Language"]["language"]

# 初始化gettext翻译
gt = gettext.translation("messages", "locales", [language_config], fallback=True)
gt.install()

_ = gt.gettext


"""字符串常量"""


class BasicString:
    """项目基础信息字符串类"""

    NONE_TEXT = ""

    # 项目本体信息
    APP_NAME = "Sankteco"
    APP_FULL_NAME = "祈福Sankteco"
    APP_VERSION = "Version Dev"
    APP_VERSION_TYPE = "Dev"
    APP_COPYTYPE = "Copyleft, GPL-3.0, ĈTEL, 2023~2026."


class AppConfigString:
    """应用配置类 的字符串，仅包含 app_config.py 相关字符串"""

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


class InfoUIString:
    """信息 界面字符串，仅包含 imformations_ui.py 相关字符串，不包含隶属于主程序多UI交互的字符串"""

    # ShowInfobar 类
    SHOWINFOBAR_OFFLINE_TITLE = _("错误！")
    SHOWINFOBAR_OFFLINE_CONTENT = _("无法找到离线文档！")
    SHOWINFOBAR_ONLINE_TITLE = _("警告！")
    SHOWINFOBAR_ONLINE_CONTENT = _("无法连接到服务器！")

    # 支持 部分
    SUPPTCARD_TITLE = _("支持")
    SUPPTCARD_OFFLINEDOCBUTTON = _("查看")
    SUPPTCARD_ONLINEDOCBUTTON = _("查看")
    SUPPTCARD_OFFLINEDOCGROUPTITLE = _("离线帮助文档")
    SUPPTCARD_OFFLINEDOCGROUPCONTEXT = _("查看保存于本地的帮助文档，如果有的话")
    SUPPTCARD_ONLINEDOCGROUPTITLE = _("在线帮助文档")
    SUPPTCARD_ONLINEDOCGROUPCONTEXT = _("访问项目官网获取在线帮助文档")

    # 更新 部分
    UPDATECARD_TITLE = _("更新")
    UPDATECARD_PIPE_RELEASE = _("正式版")
    UPDATECARD_PIPE_BETA = _("测试版")
    UPDATECARD_UPDATESTATUS = _("检查更新")
    UPDATECARD_PIPEGROUP_TITLE = _("更新通道")
    UPDATECARD_PIPEGROUP_DETAIL = _("选择项目从何通道进行更新")
    UPDATECARD_VERSTATUSGROUP_TITLE = _("当前版本已是最新版本")


class SettUIString:
    """首选项 界面字符串，仅包含 settings_ui.py 相关字符串，不包含隶属于主程序多UI交互的字符串"""

    # 提示文本
    TIP_TITLE = _("在此处调整程序设置")
    TIP_CONTEXT = _("从下面的孙页面中选择其一以更改相关选项")

    # 基本设置
    TO_BASIC_CARD_TEXT = _("跳转")
    TO_BASIC_CARD_TITLE = _("基本")
    TO_BASIC_CARD_CONTEXT = _("更改基本设置")

    # 视听设置
    TO_AUDIOVISUAL_CARD_TEXT = _("跳转")
    TO_AUDIOVISUAL_CARD_TITLE = _("视听")
    TO_AUDIOVISUAL_CARD_CONTEXT = _("更改背景音乐、音效、朗读等设置")

    # 联动设置
    TO_LINKAGE_CARD_TEXT = _("跳转")
    TO_LINKAGE_CARD_TITLE = _("联动")
    TO_LINKAGE_CARD_CONTEXT = _("更改与课表软件的联动设置")

    # 语言设置
    TO_LANGUAGE_CARD_TEXT = _("跳转")
    TO_LANGUAGE_CARD_TITLE = _("语言")
    TO_LANGUAGE_CARD_CONTEXT = _("更改界面显示语言")

    # 更新设置
    TO_UPDATE_CARD_TEXT = _("跳转")
    TO_UPDATE_CARD_TITLE = _("更新")
    TO_UPDATE_CARD_CONTEXT = _("更新程序")

    # 调试设置
    TO_DEBUG_CARD_TEXT = _("跳转")
    TO_DEBUG_CARD_TITLE = _("调试")
    TO_DEBUG_CARD_CONTEXT = _("高级调试选项")


class SettBasicUIString:
    """首选项-基本 界面字符串，仅包含 setting_basic_ui.py 相关字符串，不包含隶属于主程序多UI交互的字符串"""

    # 名单 部分
    # 多名单管理
    NAMELISTS_CREATE_CARD_TEXT = _("管理")
    NAMELISTS_CREATE_CARD_TITLE = _("多名单")
    NAMELISTS_CREATE_CARD_CONTENT = _("创建或管理不同名单以供便携使用")

    # 当前名单设置组
    NOW_NAMELIST_CARD_TITLE = _("设置当前名单")
    NOW_NAMELIST_CARD_CONTENT = _("选择要管理的名单并配置")
    NOW_NAMELIST_CARD_CHOOSE_LABEL = _("选择要管理的名单")
    NOW_NAMELIST_CARD_DETAIL_BUTTON = _("管理")
    NOW_NAMELIST_CARD_DETAIL_LABEL = _("管理当前选择的名单之内容")
    NOW_NAMELIST_CRAD_SIGN_BUTTON = _("添加")
    NOW_NAMELIST_CARD_SIGN_LABEL = _("为所选的名单添加标记")

    # 普通抽选 部分
    # 动画精美度
    CARTON_BEAUTY_LEVEL_CARD_TITLE = _("动画精美度")
    CARTON_BEAUTY_LEVEL_CARD_CONTEXT = _("调节抽选时的动画精美程度")
    CARTON_BEAUTY_LEVEL_CARD_TEXTS_AMAZED = _("华丽")
    CARTON_BEAUTY_LEVEL_CARD_TEXTS_BEAUTY = _("精美")
    CARTON_BEAUTY_LEVEL_CARD_TEXTS_BASIC = _("一般")
    CARTON_BEAUTY_LEVEL_CARD_TEXTS_FAST = _("快速")

    # 快速抽选 部分
    # 结果推送
    SHOW_RESULT_WAY_CARD_TITLE = _("结果推送方式")
    SHOW_RESULT_WAY_CARD_CONTEXT = _("选择快速抽选的结果应怎样显示")
    SHOW_RESULT_WAY_CARD_TEXTS_CI = _("显示在ClassIsland")
    SHOW_RESULT_WAY_CARD_TEXTS_CW = _("显示在ClassWidget")
    SHOW_RESULT_WAY_CARD_TEXTS_DIALOG = _("显示在临时弹窗")

    # 各部分对象名称
    NAMELIST_SETT_GR_OBJNAME = "namelist_sett_gr"
    B_CHOOSE_SETT_GR_OBJNAME = "b_choose_sett_gr"
    F_CHOOSE_SETT_GR_OBJNAME = "f_choose_sett_gr"

    # 各部分显示字段
    NAMELIST_SETT_GR_NAVNAME = _("名单")
    B_CHOOSE_SETT_GR_NAVNAME = _("普通抽选")
    F_CHOOSE_SETT_GR_NAVNAME = _("快速抽选")


class SettAvUIString:
    """首选项-视听 界面字符串，仅包含 setting_audiovisual_ui.py 相关字符串，不包含隶属于主程序多UI交互的字符串"""

    # 音乐 部分
    # 音乐开关
    MUSIC_SWITCH_CARD_TITLE = _("音乐开关")
    MUSIC_SWITCH_CARD_CONTEXT = _("控制是否在普通抽选时播放背景音乐")

    # 音乐文件
    MUSIC_PATH_CARD_TITLE = _("音乐文件")
    MUSIC_PATH_CARD_CONTEXT = _("选择要启用的音乐文件")
    MUSIC_PATH_CARD_BUTTON = _("选择")

    # 音量调节
    MUSIC_VOLUME_CARD_TITLE = _("音乐音量")
    MUSIC_VOLUME_CARD_CONTEXT = _("调节音乐在播放时的音量")

    # 渐入效果
    MUSIC_PLAY_SMOOTHLY_CARD_TITLE = _("音乐渐入效果")
    MUSIC_PLAY_SMOOTHLY_CARD_CONTEXT = _("调整音乐播放时渐入效果持续的秒数(s)")

    # 渐出效果
    MUSIC_PAUSE_SMOOTHLY_CARD_TITLE = _("音乐渐出效果")
    MUSIC_PAUSE_SMOOTHLY_CARD_CONTEXT = _("调整音乐播放时渐出效果持续的秒数(s)")

    # 音效 部分
    # 音效开关
    SOUND_SWITCH_CARD_TITLE = _("音效开关")
    SOUND_SWITCH_CARD_CONTEXT = _("控制是否在点名结束后播放抽选音效")

    # 音效路径
    SOUND_PATH_CRAD_TITLE = _("音效路径")
    SOUND_PATH_CRAD_CONTEXT = _("选择要启用的音效文件")
    SOUND_PATH_CARD_BUTTON = _("选择")

    # 音效在何时播放
    SOUND_PLAY_TIME_CARD_TITLE = _("音效在何时播放")
    SOUND_PLAY_TIME_CARD_TEXT_B_CHOOSE = _("仅普通抽选后")
    SOUND_PLAY_TIME_CARD_TEXT_F_CHOOSE = _("仅快速抽选后")
    SOUND_PLAY_TIME_CARD_TEXT_BOTH = _("两者后")

    # 朗读 部分
    # 朗读开关
    READ_SWITCH_CARD_TITLE = _("朗读开关")
    READ_SWITCH_CARD_CONTEXT = _("控制是否在点名结束后朗读被抽中的名字")

    # 在何时朗读
    READ_TIME_CARD_TITLE = _("在何时朗读")
    READ_TIME_CARD_TEXT_B_CHOOSE = _("仅普通抽选后")
    READ_TIME_CARD_TEXT_F_CHOOSE = _("仅快速抽选后")
    READ_TIME_CARD_TEXT_BOTH = _("两者后")

    # 主题
    # 深浅模式
    THEME_DARK_LIGHT_CARD_TITLE = _("深浅模式")
    THEME_DARK_LIGHT_CARD_CONTEXT = _("选择程序显示时的深浅色模式")
    THEME_DARK_LIGHT_CARD_TEXT_DARK = _("深色")
    THEME_DARK_LIGHT_CARD_TEXT_LIGHT = _("浅色")
    THEME_DARK_LIGHT_CARD_TEXT_AUTO = _("跟随系统")

    # 窗口效果
    THEME_WINDOW_EFFORT_CARD_TITLE = _("窗口效果")
    THEME_WINDOW_EFFORT_CARD_CONTEXT = _("调整程序窗口的显示效果")
    THEME_WINDOW_EFFORT_CARD_TEXT_MICA = _("Mica")
    THEME_WINDOW_EFFORT_CARD_TEXT_AUTO = _("跟随系统")

    # 各部分对象名称
    MUSIC_SETT_GR_OBJNAME = "music_sett_gr"
    SOUND_SETT_GR_OBJNAME = "sound_sett_gr"
    READ_SETT_GR_OBJNAME = "read_sett_gr"
    THEME_SETT_GR_OBJNAME = "theme_sett_gr"

    # 各部分显示字段
    MUSIC_SETT_GR_NAVNAME = _("音乐")
    SOUND_SETT_GR_NAVNAME = _("音效")
    READ_SETT_GR_NAVNAME = _("朗读")
    THEME_SETT_GR_NAVNAME = _("主题")


class SettLangUIString:
    """首选项-语言 界面字符串，仅包含 setting_language_ui.py 相关字符串，不包含隶属于主程序多UI交互的字符串"""

    # 语言选择
    SCREEN_LANGUAGE_TITLE = _("显示语言")
    SCREEN_LANGUAGE_CONTEXT = _("选择将在屏幕上显示的语言")
    SCREEN_LANGUAGE_TEXT_ZH_CN = _("简体中文")
    SCREEN_LANGUAGE_TEXT_EO = _("世界语")

    # 加入翻译计划
    JOIN_TRANSLATION_TITLE = _("加入翻译计划")
    JOIN_TRANSLATION_CONTEXT = _("加入项目的在线翻译工程，为本地化做出贡献")
    JOIN_TRANSLATION_HYPERLINK_TEXT = _("跳转")


class MainUIString:
    """主界面 字符串，包含 main_ui.py 相关字符串，包含隶属于主程序多UI交互的字符串"""

    # 子页面对象名
    SUBPAGE_INFORMATION_OBJNAME = "subpage_information"
    SUBPAGE_SETTINGS_OBJNAME = "subpage_settings"

    # 设置 孙页面对象名
    SUBSUBPAGE_SETTIING_BASIC_OBJNAME = "subsubpage_setting_basic"
    SUBSUBPAGE_SETTIING_AUDIOVISUAL_OBJNAME = "subsubpage_setting_audiovisual"
    SUBSUBPAGE_SETTIING_LANGUAGE_OBJNAME = "subsubpage_setting_language"

    # 子页面导航窗口显示字段
    SUBPAGE_INFORMATION_NAVNAME = _("信息")
    SUBPAGE_SETTINGS_NAVNAME = _("首选项")

    # 设置 孙页面导航窗口显示字段
    SUBSUBPAGE_SETTIING_BASIC_NAVNAME = _("基本")
    SUBSUBPAGE_SETTIING_AUDIOVISUAL_NAVNAME = _("视听")
    SUBSUBPAGE_SETTIING_LANGUAGE_NAVNAME = _("语言")


"""相对路径常量"""


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
    # 加入翻译计划（ 语言 孙页面）
    JOIN_TRANSLATION_LINK = ""


class AssetsPath:
    """资源相对路径类"""

    from pathlib import Path

    # 音频
    # 默认音乐
    APP_DEFAULT_MUSIC_PATH = Path(AssetsPathTXT.APP_DEFAULT_MUSIC_PATH)

    # 默认音效
    APP_DEFAULT_SOUND_PATH = Path(AssetsPathTXT.APP_DEFAULT_SOUND_PATH)
