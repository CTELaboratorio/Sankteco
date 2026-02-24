"""
本文件是储存项目常量与变量标准值的文件
"""

import gettext


_ = gettext.gettext


"""字符串常量"""


class BasicString:
    """项目基础信息字符串类"""

    NONE_TEXT = ""

    # 项目本体信息
    APP_NAME = "Sankteco"
    APP_FULL_NAME = "祈福Sankteco"
    APP_VERSION = "Version Dev"
    APP_VERSION_TYPE = "Dev"
    APP_COPYTYPE = "Copyleft, GPL-3.0, 2023~2026, HXES.As is."


class InfoUIString:
    """信息 界面字符串，仅包含 imformations_ui.py 相关字符串，不包含隶属于主程序多UI交互的字符串"""

    # 信息板 部分
    INFOBODCARD_TITLE = _("信息板")

    # 支持 部分
    SUPPTCARD_TITLE = _("支持")
    SUPPTCARD_OFFLINEDOCBUTTON = _("查看")
    SUPPTCARD_ONLINEDOCBUTTON = _("查看")
    SUPPTCARD_OFFLINEDOCGROUPTITLE = _("离线帮助文档")
    SUPPTCARD_OFFLINEDOCGROUPCONTEXT = _("查看保存于本地的帮助文档，如果有的话")
    SUPPTCARD_ONLINEDOCGROUPTITLE = _("在线帮助文档")
    SUPPTCARD_ONLINEDOCGROUPCONTEXT = _("访问项目官网获取在线帮助文档")

    # 语言 部分
    LANGCARD_TITLE = _("语言")
    LANGCARD_LANGCARD_TITLE = _("语言选项")
    LANGCARD_LANGCARD_DETAIL = _("从此处更改界面语言")
    LANGCARD_LANGCARD_COMBO_ZHCN = "简体中文"
    LANGCARD_LANGCARD_COMBO_EO = "Esperanto"

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


class MainUIString:
    """主界面 字符串，包含 main_ui.py 相关字符串，包含隶属于主程序多UI交互的字符串"""

    # 子页面对象名
    SUBPAGE_INFORMATION_OBJNAME = "subpage_information"
    SUBPAGE_SETTINGS_OBJNAME = "subpage_settings"
    SUBSUBPAGE_SETTIING_BASIC_OBJNAME = "subsubpage_setting_basic"

    # 子页面导航窗口显示字段
    SUBPAGE_INFORMATION_NAVNAME = _("信息")
    SUBPAGE_SETTINGS_NAVNAME = _("首选项")
    SUBSUBPAGE_SETTIING_BASIC_NAVNAME = _("基本")


"""相对路径常量"""


class AssetsPath:
    """资源相对路径类"""

    # 图片
    # 图标
    APP_ICON_PATH = "assets/icon/app_icon.png"

    # 项目详细图
    APP_DETAILEDIMAGE_PATH = "assets/images/app_detailed_image.png"

    # 配置文件
    APP_CONFIG = "config/app_config.json"
