from qfluentwidgets import NavigationItemPosition, FluentWindow, SplashScreen
from qfluentwidgets import FluentIcon as FIF
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize, QTimer, QEventLoop
from PySide2.QtWidgets import QApplication
import sys


class MainWindow(FluentWindow):
    """应用程序主窗口，继承自FluentWindow"""

    def __init__(self):
        """初始化主窗口"""
        super().__init__()

        # 初始化窗口设置
        self.initWindow()

        # 导入子页面
        

        # 初始化导航栏
        self.initNavigation()

    def initNavigation(self):
        """初始化导航栏，添加各个子界面"""
        # 添加子界面
        

    def initWindow(self):
        """初始化窗口设置"""
        # 设置窗口大小
        self.resize(1080, 768)
        # 设置窗口图标
        self.setWindowIcon(QIcon("../assets/icon/appico.png"))
        # 设置窗口标题
        self.setWindowTitle("祈福Prays - dev - new")

        
if __name__ == "__main__":
    """程序入口"""
    # 创建QApplication实例
    app = QApplication(sys.argv)
    # 创建主窗口
    w = MainWindow()
    w.show()
    # 启动应用事件循环
    app.exec_()
