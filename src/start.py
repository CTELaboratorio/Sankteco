"""
启动文件, 
此页面是项目的入口, 运行与编译须从此开始
"""

import sys
from PySide2.QtWidgets import QApplication
from ui.main_ui import MainWindow
from ui.settings_ui.settings_audiovisual_logic import apply_theme_from_config


if __name__ == "__main__":
    """程序入口"""

    # 创建QApplication实例
    app = QApplication(sys.argv)

    # 应用保存的主题配置（必须在窗口创建前执行）
    apply_theme_from_config()

    # 创建主窗口
    w = MainWindow()
    w.show()

    # 启动应用事件循环
    sys.exit(app.exec_())
