"""
子页面：首选项
此页面包含了本项目的可调整设置选项，包含六个孙页面：基本、视听、联动、语言、更新、调试
引用时可作 SettUI / subpage_settings
"""


from PySide2.QtWidgets import QFrame, QVBoxLayout
from PySide2.QtCore import Qt
import qfluentwidgets as qfw
from qfluentwidgets import FluentIcon as FIF
from app_const_var import *