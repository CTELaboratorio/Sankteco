"""
孙页面：基本（ 首选项 的子页面），
此页面包含了本项目基本的可调整设置选项，包含三个部分：名单、普通抽选、快速抽选，
引用时可作 SettBasicUI / subsubpage_settings_basic
"""

from PySide2.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget
from PySide2.QtCore import Qt
import qfluentwidgets as qfw
from qfluentwidgets import FluentIcon as FI
from app_const_var import *
from app_config import *


# 加载配置文件
sett_basic_ui_cfg = AppCommonConfig()
qfw.qconfig.load(r"../../../config/app_config.json", AppCommonConfig)


class NowNamelistSettingCard(qfw.ExpandGroupSettingCard):
    """当前名单设置组 选项卡，从属于 名单 部分，
    继承自 手风琴设置组卡片 ExpandGroupSettingCard，
    引用时可作 NowNamelistSett"""

    def __init__(self, parent=None):
        super().__init__(
            FI.DOCUMENT,
            SettBasicUIString.NOW_NAMELIST_CARD_TITLE,
            SettBasicUIString.NOW_NAMELIST_CARD_CONTENT,
            parent,
        )

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

        # 添加控件至组布局
        self.add_widget_to_group(
            self.choose_namelist_label, self.choose_namelist_combobox
        )
        self.add_widget_to_group(
            self.now_namelist_detail_label, self.now_namelist_detail_button
        )
        self.add_widget_to_group(self.sign_namelist_label, self.sign_namelist_button)

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
    """名单 部分，继承自 QWidget，
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
    """普通抽选 部分，继承自 QWidget，
    引用时可作 BChooseSettGr"""

    def __init__(self):
        super().__init__()

        # 初始化垂直布局
        self.vboxlayout = QVBoxLayout(self)

        # 动画精美度
        self.carton_beauty_level_card = qfw.ComboBoxSettingCard(
            sett_basic_ui_cfg.carton_beauty_level,
            FI.CLOUD,
            "动画精美度",
            "调节抽选时的动画精美程度",
            ["华丽", "精美", "一般", "快速"],
        )

        # 设置布局
        self.vboxlayout.addWidget(self.carton_beauty_level_card)
        self.setLayout(self.vboxlayout)


class FastChooseSettingGroup(QWidget):
    """快速抽选 部分，继承自 QWidget，
    引用时可作 FChooseSettGr"""

    def __init__(self):
        super().__init__()

        # 初始化垂直布局
        self.vboxlayout = QVBoxLayout(self)

        # 结果推送
        self.show_result_way = qfw.OptionsSettingCard(
            sett_basic_ui_cfg.show_result_way,
            FI.INFO,
            "结果推送方式",
            "选择快速抽选的结果应怎样显示",
            ["显示在ClassIsland", "显示在ClassWidget", "显示在临时弹窗"],
        )

        # 设置布局
        self.vboxlayout.addWidget(self.show_result_way)
        self.setLayout(self.vboxlayout)


class SettingBasicUI(QFrame):
    """孙页面：基本（ 首选项 的子页面）的基础UI类，
    此页面包含了本项目基本的可调整设置选项，包含三个部分：名单、普通抽选、快速抽选，
    引用时可作 SettBasicUI / subsubpage_settings_basic"""

    def __init__(self, parent=None):
        super().__init__(parent)

        # 初始化顶部导航栏与多页面，初始化布局
        self.pivot = qfw.Pivot(self)
        self.stackedWidget = QStackedWidget(self)
        self.vboxlayout = QVBoxLayout(self)

        # 添加各项的卡片组
        self.namelist_interface = NamelistSettingGroup()
        self.basic_choose_interface = BasicChooseSettingGroup()
        self.fast_choose_interface = FastChooseSettingGroup()

        # 添加标签页
        self.add_sub_interface(self.namelist_interface, "namelist_sett_gr", "名单")
        self.add_sub_interface(
            self.basic_choose_interface, "b_choose_sett_gr", "普通抽选"
        )
        self.add_sub_interface(
            self.fast_choose_interface, "f_choose_sett_gr", "快速抽选"
        )

        # 连接信号并初始化当前标签页
        self.stackedWidget.currentChanged.connect(self.on_current_index_changed)
        self.stackedWidget.setCurrentWidget(self.namelist_interface)
        self.pivot.setCurrentItem(self.namelist_interface.objectName())

        # 调整布局
        # self.vboxlayout.setContentsMargins(30, 0, 30, 30)
        self.vboxlayout.addWidget(self.pivot)
        self.vboxlayout.setAlignment(self.pivot, Qt.AlignCenter)
        self.vboxlayout.addWidget(self.stackedWidget)

    def add_sub_interface(self, widget: QWidget, objectName: str, text: str):
        widget.setObjectName(objectName)
        self.stackedWidget.addWidget(widget)

        # 使用全局唯一的 objectName 作为路由键
        self.pivot.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stackedWidget.setCurrentWidget(widget),
        )

    def on_current_index_changed(self, index):
        widget = self.stackedWidget.widget(index)
        self.pivot.setCurrentItem(widget.objectName())
