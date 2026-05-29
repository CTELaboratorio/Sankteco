"""
启动文件, 
此页面是项目的入口, 运行与编译须从此开始
"""

import sys
from PySide2.QtWidgets import QApplication
from ui.main_ui import MainWindow


if __name__ == "__main__":
    """程序入口"""
    # 创建QApplication实例
    app = QApplication(sys.argv)
    # 创建主窗口
    w = MainWindow()
    w.show()
    # 启动应用事件循环
    sys.exit(app.exec_())
