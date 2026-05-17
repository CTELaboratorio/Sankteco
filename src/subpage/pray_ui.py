"""
子页面:祈福, 
此页面包含了基本点名功能的GUI, 是程序启动时的默认页面, 
包含四大部分:一言显示, 点名结果显示, 点名快捷设置, 实时资源显示, 
引用时可作 PrayUI / subpage_pray
"""

from PySide2.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLayout,
    QListWidgetItem,
)
from PySide2.QtGui import QColor
import qfluentwidgets as qfw
from qfluentwidgets import FluentIcon as FI
from app_const_var import PrayUIString, AssetsPathTXT
from app_config import AppCommonConfig


# 加载配置文件
pray_ui_cfg = AppCommonConfig()
qfw.qconfig.load(AssetsPathTXT.APP_CONFIG, pray_ui_cfg)


def set_widget_to_layout(wlist: list, layout: QLayout):
    """设置布局的通用函数(控件到布局)"""
    for widget in wlist:
        layout.addWidget(widget)


def set_layouts_to_layout(llist: list, to_layout: QLayout):
    """设置布局的通用函数(布局到布局)"""
    for layout in llist:
        to_layout.addChildLayout(layout)


class HitokotoShowGroup(QWidget):
    """一言显示 部分, 继承自 QWidget,
    引用时可作 HitokotoShowGr"""

    def __init__(self):
        super().__init__()

        # 初始化垂直布局
        self.vboxlayout = QVBoxLayout(self)

        # 初始化控件
        self.init_widgets()

        # 控件列表
        self.widget_list = [self.hitokoto_show]

        # 设置布局
        set_widget_to_layout(self.widget_list, self.vboxlayout)

    def init_widgets(self):
        """初始化控件"""

        # 一言显示
        self.hitokoto_show = qfw.StrongBodyLabel("旗开得胜，一举夺魁！")
        self.hitokoto_show.setTextColor(QColor(0, 255, 0), QColor(255, 0, 0))  # type: ignore


class PrayResultShowGroup(QWidget):
    """点名结果显示 部分, 继承自 QWidget,
    引用时可作 PrayResShowGr"""

    def __init__(self):
        super().__init__()

        # 初始化垂直布局
        self.vboxlayout = QVBoxLayout(self)

        # 初始化控件
        self.init_widgets()

        # 控件列表
        self.widget_list = [self.pray_result_show]

        # 设置布局
        set_widget_to_layout(self.widget_list, self.vboxlayout)

    def init_widgets(self):
        """初始化控件"""

        # 点名结果显示
        self.pray_result_show = qfw.ListWidget()
        self.pray_result_list = ["别紧张"]
        if not (self.pray_result_list == []):
            self.bind_list_to_widget()

    def add_pray_result(self, result_list: list):
        """清除并添加点名结果"""

        # 清除原有点名结果
        self.pray_result_list = []

        # 添加新点名结果
        for result in result_list:
            self.pray_result_list.append(result)

    def bind_list_to_widget(self):
        """将点名结果列表与控件绑定"""

        for i in self.pray_result_list:
            item = QListWidgetItem(i)
            self.pray_result_show.addItem(item)


class PrayQuickSettingGroup(QWidget):
    """点名快捷设置 部分, 继承自 QWidget,
    引用时可作 PraySettGr"""

    def __init__(self):
        super().__init__()

        # 初始化垂直布局
        self.vboxlayout = QVBoxLayout(self)

        # 初始化各部分布局
        self.start_pray_button_layout()
        self.set_pray_algorithm_combobox()

        # 布局列表
        self.layout_list = [self.spbtn_vboxlayout, self.spacombo_vboxlayout]

        # 设置布局
        set_layouts_to_layout(self.layout_list, self.vboxlayout)

    def line_1_layout(self):
        """第一行布局"""

        # 初始化水平布局
        self.line_1_hboxlayout = QHBoxLayout(self)

        # 初始化布局
        self.start_pray_button_layout()
        self.set_pray_algorithm_combobox()

        # 布局列表
        self.line_1_widget_list = [self.spbtn_vboxlayout, self.spacombo_vboxlayout]

        # 设置布局
        set_layouts_to_layout(self.line_1_widget_list, self.line_1_hboxlayout)

    def start_pray_button_layout(self):
        """开始祈福按钮布局, 引用时简写为 spbtn"""

        # 初始化垂直布局
        self.spbtn_vboxlayout = QVBoxLayout(self)

        # 初始化开始祈福按钮
        self.start_pray_button = qfw.PushButton("祈福")

        # 设置布局
        self.spbtn_vboxlayout.addWidget(self.start_pray_button)

    def set_pray_algorithm_combobox(self):
        """设置祈福算法下拉框, 引用时简写为 spacombo"""

        # 初始化垂直布局
        self.spacombo_vboxlayout = QVBoxLayout(self)

        # 初始化祈福算法下拉框
        self.pray_algorithm_combobox = qfw.ComboBox()

        # 初始化祈福算法选项
        self.pray_algorithm_list = ["Python原生随机算法", "SecRandom算法"]

        # 绑定列表到下拉框
        self.pray_algorithm_combobox.addItems(self.pray_algorithm_list)

        # 设置布局
        self.spacombo_vboxlayout.addWidget(self.pray_algorithm_combobox)

    # TODO: 祈福数量调整布局
