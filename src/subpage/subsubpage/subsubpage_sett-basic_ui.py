"""
孙页面：基本（ 首选项 的子页面）
此页面包含了本项目基本的可调整设置选项，包含三个部分：名单、普通抽选、快速抽选
引用时可作 Sett-BasicUI / subsubpage_sett-basic
"""


from PySide2.QtWidgets import QFrame, QVBoxLayout
from PySide2.QtCore import Qt
import qfluentwidgets as qfw
from qfluentwidgets import FluentIcon as FIF
from app_const_var import *