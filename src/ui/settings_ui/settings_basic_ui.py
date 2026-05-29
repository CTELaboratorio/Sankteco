"""
孙页面:基本( 首选项 的子页面), 
此页面包含了本项目基本的可调整设置选项, 包含三个部分:名单, 普通抽选, 快速抽选, 
引用时可作 SettBasicUI / subsubpage_setting_basic
"""

from PySide2.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QWidget
import qfluentwidgets as qfw
from qfluentwidgets import FluentIcon as FI
from app_const_var import AssetsPathTXT
from ui.ui_str import SettBasicUIString
from app_config import AppCommonConfig


# 加载配置文件
sett_basic_ui_cfg = AppCommonConfig()
qfw.qconfig.load(AssetsPathTXT.APP_CONFIG, sett_basic_ui_cfg)


class NowNamelistSettingCard(qfw.ExpandGroupSettingCard):
    """当前名单设置组 选项卡, 从属于 名单 部分,
    继承自 手风琴设置组卡片 ExpandGroupSettingCard,
    引用时可作 NowNamelistSett"""

    def __init__(self, parent=None):
        super().__init__(
            FI.DOCUMENT,
            SettBasicUIString.NOW_NAMELIST_CARD_TITLE,
            SettBasicUIString.NOW_NAMELIST_CARD_CONTENT,
            parent,
        )

        # 初始化控件
        self.init_widgets()

        # 添加控件至组布局
        self.add_widget_to_group(
            self.choose_namelist_label, self.choose_namelist_combobox
        )
        self.add_widget_to_group(
            self.now_namelist_detail_label, self.now_namelist_detail_button
        )
        self.add_widget_to_group(self.sign_namelist_label, self.sign_namelist_button)

    def init_widgets(self):
        """初始化控件"""
        # 选择名单
        self.choose_namelist_combobox = qfw.ComboBox()
        self.choose_namelist_label = qfw.BodyLabel(
            SettBasicUIString.NOW_NAMELIST_CARD_CHOOSE_LABEL
        )

        # 管理名单内容
        self.now_namelist_detail_button = qfw.PushButton(
            SettBasicUIString.NOW_NAMELIST_CARD_DETAIL_BUTTON
        )
        self.now_namelist_detail_label = qfw.BodyLabel(
            SettBasicUIString.NOW_NAMELIST_CARD_DETAIL_LABEL
        )
        self.now_namelist_detail_button.setFixedWidth(100)

        # 标记名单
        self.sign_namelist_button = qfw.PushButton(
            SettBasicUIString.NOW_NAMELIST_CRAD_SIGN_BUTTON
        )
        self.sign_namelist_label = qfw.BodyLabel(
            SettBasicUIString.NOW_NAMELIST_CARD_SIGN_LABEL
        )
        self.sign_namelist_button.setFixedWidth(100)

    def add_widget_to_group(self, added_label, added_widget):
        """添加控件至水平布局并加入设置卡组"""
        widget = QWidget()
        widget.setFixedHeight(60)

        layout = QHBoxLayout(widget)

        layout.addWidget(added_label)
        layout.addWidget(added_widget)

        # 添加组件到设置卡组
        self.addGroupWidget(widget)


class NamelistSettingGroup(QWidget):
    """名单 部分, 继承自 QWidget,
    引用时可作 NamelistSettGr"""

    def __init__(self):
        super().__init__()

        # 初始化垂直布局
        self.vboxlayout = QVBoxLayout(self)

        # 多名单管理
        self.namelists_create_card = qfw.PushSettingCard(
            text=SettBasicUIString.NAMELISTS_CREATE_CARD_TEXT,
            icon=FI.ROBOT,
            title=SettBasicUIString.NAMELISTS_CREATE_CARD_TITLE,
            content=SettBasicUIString.NAMELISTS_CREATE_CARD_CONTENT,
        )

        # 当前名单设置组
        self.now_namelist_groupcard = NowNamelistSettingCard(self)

        # 设置布局
        self.vboxlayout.addWidget(self.namelists_create_card)
        self.vboxlayout.addWidget(self.now_namelist_groupcard)
        self.setLayout(self.vboxlayout)


class BasicChooseSettingGroup(QWidget):
    """普通抽选 部分, 继承自 QWidget,
    引用时可作 BChooseSettGr"""

    def __init__(self):
        super().__init__()

        # 初始化垂直布局
        self.vboxlayout = QVBoxLayout(self)

        # 动画精美度
        self.carton_beauty_level_card = qfw.ComboBoxSettingCard(
            sett_basic_ui_cfg.carton_beauty_level,
            FI.CLOUD,
            SettBasicUIString.CARTON_BEAUTY_LEVEL_CARD_TITLE,
            SettBasicUIString.CARTON_BEAUTY_LEVEL_CARD_CONTEXT,
            [
                SettBasicUIString.CARTON_BEAUTY_LEVEL_CARD_TEXTS_AMAZED,
                SettBasicUIString.CARTON_BEAUTY_LEVEL_CARD_TEXTS_BEAUTY,
                SettBasicUIString.CARTON_BEAUTY_LEVEL_CARD_TEXTS_BASIC,
                SettBasicUIString.CARTON_BEAUTY_LEVEL_CARD_TEXTS_FAST,
            ],
        )

        # 设置布局
        self.vboxlayout.addWidget(self.carton_beauty_level_card)
        self.setLayout(self.vboxlayout)


class FastChooseSettingGroup(QWidget):
    """快速抽选 部分, 继承自 QWidget,
    引用时可作 FChooseSettGr"""

    def __init__(self):
        super().__init__()

        # 初始化垂直布局
        self.vboxlayout = QVBoxLayout(self)

        # 结果推送
        self.show_result_way = qfw.OptionsSettingCard(
            sett_basic_ui_cfg.show_result_way,
            FI.INFO,
            SettBasicUIString.SHOW_RESULT_WAY_CARD_TITLE,
            SettBasicUIString.SHOW_RESULT_WAY_CARD_CONTEXT,
            [
                SettBasicUIString.SHOW_RESULT_WAY_CARD_TEXTS_CI,
                SettBasicUIString.SHOW_RESULT_WAY_CARD_TEXTS_CW,
                SettBasicUIString.SHOW_RESULT_WAY_CARD_TEXTS_DIALOG,
            ],
        )

        # 设置布局
        self.vboxlayout.addWidget(self.show_result_way)
        self.setLayout(self.vboxlayout)


class SettingsBasicUI(QFrame):
    """孙页面:基本( 首选项 的子页面)的基础UI类,
    此页面包含了本项目基本的可调整设置选项, 包含三个部分:名单, 普通抽选, 快速抽选,
    引用时可作 SettBasicUI / settings_basic"""

    def __init__(self, parent=None):
        super().__init__(parent)

        from PySide2.QtCore import Qt, QMargins
        from PySide2.QtWidgets import QStackedWidget

        # 初始化顶部导航栏与多页面, 初始化布局
        self.pivot = qfw.Pivot(self)
        self.stackedWidget = QStackedWidget(self)
        self.vboxlayout = QVBoxLayout(self)

        # 添加各项的卡片组
        self.namelist_interface = NamelistSettingGroup()
        self.basic_choose_interface = BasicChooseSettingGroup()
        self.fast_choose_interface = FastChooseSettingGroup()

        # 添加标签页
        self.add_sub_interface(
            self.namelist_interface,
            SettBasicUIString.NAMELIST_SETT_GR_OBJNAME,
            SettBasicUIString.NAMELIST_SETT_GR_NAVNAME,
        )
        self.add_sub_interface(
            self.basic_choose_interface,
            SettBasicUIString.B_CHOOSE_SETT_GR_OBJNAME,
            SettBasicUIString.B_CHOOSE_SETT_GR_NAVNAME,
        )
        self.add_sub_interface(
            self.fast_choose_interface,
            SettBasicUIString.F_CHOOSE_SETT_GR_OBJNAME,
            SettBasicUIString.F_CHOOSE_SETT_GR_NAVNAME,
        )

        # 连接信号并初始化当前标签页
        self.stackedWidget.currentChanged.connect(self.on_current_index_changed)
        self.stackedWidget.setCurrentWidget(self.namelist_interface)
        self.pivot.setCurrentItem(self.namelist_interface.objectName())

        # 调整布局
        self.vboxlayout.setContentsMargins(QMargins(30, 30, 30, 30))
        self.vboxlayout.addWidget(self.pivot)
        self.vboxlayout.setAlignment(self.pivot, Qt.AlignCenter)
        self.vboxlayout.addWidget(self.stackedWidget)

    def add_sub_interface(self, widget: QWidget, objectName: str, text: str):
        """添加子页面"""

        widget.setObjectName(objectName)
        self.stackedWidget.addWidget(widget)

        # 使用全局唯一的 objectName 作为路由键
        self.pivot.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stackedWidget.setCurrentWidget(widget),
        )

    def on_current_index_changed(self, index):
        """将多页面的切换信号连接到顶部导航栏显示"""

        widget = self.stackedWidget.widget(index)
        self.pivot.setCurrentItem(widget.objectName())
