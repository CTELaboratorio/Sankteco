"""
子页面：信息，
此页面包含了本项目的相关信息，包含三部分：信息板、支持、更新，
引用时可作 InfoUI / information_ui
"""

from PySide2.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QGraphicsView,
)
from PySide2.QtCore import Qt
import qfluentwidgets as qfw
from qfluentwidgets import FluentIcon as FI
from app_const_var import InfoUIString, BasicString, AssetsPathTXT


class ImageViewer(QGraphicsView):
    """图片显示控件，继承自 QGraphicsView"""

    from typing import Optional
    from PySide2.QtWidgets import QWidget

    def __init__(self, parent: Optional[QWidget] = None):
        from PySide2.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
        from PySide2.QtGui import QPainter

        super(ImageViewer, self).__init__(parent)

        # 创建一个 QGraphicsScene 对象并设置其父对象为当前的 ImageViewer
        self.scene = QGraphicsScene(self)  # type: ignore

        # 创建一个 QGraphicsPixmapItem 对象，用于显示图片
        self.imageItem = QGraphicsPixmapItem()  # type: ignore

        self.scene.addItem(self.imageItem)
        self.setScene(self.scene)

        # 启用平滑变换
        self.setRenderHint(QPainter.SmoothPixmapTransform)

    def setPixmap(self, pic: str):
        from PySide2.QtGui import QPixmap

        pixmap = QPixmap(pic)
        self.imageItem.setPixmap(pixmap)

    def resizeEvent(self, event):

        super(ImageViewer, self).resizeEvent(event)

        # 根据窗口大小自动调整图片大小
        self.fitInView(self.imageItem, Qt.KeepAspectRatio)  # type: ignore


class ShowInfobar:
    """初始化并显示消息条的类"""

    def offline_button_infobar(self, parent=None):
        """离线帮助文档被点击消息条"""

        self.infobar_offline = qfw.InfoBar.error(
            InfoUIString.SHOWINFOBAR_OFFLINE_TITLE,
            InfoUIString.SHOWINFOBAR_OFFLINE_CONTENT,
            Qt.Horizontal,
            True,
            -1,
            qfw.InfoBarPosition.TOP,
            parent,
        )

    def online_button_infobar(self, parent=None):
        """在线帮助文档被点击消息条"""

        self.infobar_online = qfw.InfoBar.warning(
            InfoUIString.SHOWINFOBAR_ONLINE_TITLE,
            InfoUIString.SHOWINFOBAR_ONLINE_CONTENT,
            Qt.Horizontal,
            True,
            -1,
            qfw.InfoBarPosition.TOP,
            parent,
        )


class InformationBoardCardGroup(qfw.ElevatedCardWidget):
    """信息板 部分，继承自 卡片组件 ElevatedCardWidget
    引用时可作 InfoBodCard"""

    def __init__(self, parent=None):
        super().__init__(parent)

        # 项目详细图
        self.app_detailed_image = ImageViewer()
        self.app_detailed_image.setPixmap(AssetsPathTXT.APP_DETAILEDIMAGE_PATH)

        # 项目信息
        self.infotext_bodylabel = qfw.StrongBodyLabel(BasicString.APP_FULL_NAME, self)
        self.infotext_captionlabel = qfw.CaptionLabel(BasicString.APP_COPYTYPE, self)

        # 组件布局
        self.vboxlayout = QVBoxLayout(self)
        self.vboxlayout.addWidget(self.app_detailed_image)
        self.vboxlayout.setAlignment(self.app_detailed_image, Qt.AlignCenter)
        self.vboxlayout.addWidget(self.infotext_bodylabel)
        self.vboxlayout.addWidget(self.infotext_captionlabel)


class SupportCardGroup(qfw.GroupHeaderCardWidget):
    """支持 部分，继承自 上下分组布局卡片 GroupHeaderCardWidget
    引用时可作 SupptCard"""

    def __init__(self, parent=None):
        super().__init__(parent)

        # 选项卡组基本设置
        self.setTitle(InfoUIString.SUPPTCARD_TITLE)
        self.setBorderRadius(8)

        # 帮助文档按钮
        self.offline_document_button = qfw.PushButton(
            icon=FI.DOCUMENT, text=InfoUIString.SUPPTCARD_OFFLINEDOCBUTTON
        )
        self.online_document_button = qfw.PushButton(
            icon=FI.SEARCH, text=InfoUIString.SUPPTCARD_ONLINEDOCBUTTON
        )

        # 添加分组到组件中
        self.addGroup(
            FI.DOCUMENT,
            InfoUIString.SUPPTCARD_OFFLINEDOCGROUPTITLE,
            InfoUIString.SUPPTCARD_OFFLINEDOCGROUPCONTEXT,
            self.offline_document_button,
        )
        group = self.addGroup(
            FI.GLOBE,
            InfoUIString.SUPPTCARD_ONLINEDOCGROUPTITLE,
            InfoUIString.SUPPTCARD_ONLINEDOCGROUPCONTEXT,
            self.online_document_button,
        )
        group.setSeparatorVisible(True)


class UpdateCardGroup(qfw.GroupHeaderCardWidget):
    """更新 部分，继承自 上下分组布局卡片 GroupHeaderCardWidget
    引用时可作 UpdateCard"""

    def __init__(self, parent=None):
        super().__init__(parent)

        # 选项卡组基本设置
        self.setTitle(InfoUIString.UPDATECARD_TITLE)
        self.setBorderRadius(8)

        # 更新通道下拉框
        self.update_pipe_combobox = qfw.ComboBox()
        self.update_pipe_combobox_item = [
            InfoUIString.UPDATECARD_PIPE_RELEASE,
            InfoUIString.UPDATECARD_PIPE_BETA,
        ]
        self.update_pipe_combobox.addItems(self.update_pipe_combobox_item)

        # 更新状态
        self.update_status_check_button = qfw.PushButton(
            icon=FI.CHECKBOX, text=InfoUIString.UPDATECARD_UPDATESTATUS
        )

        # 添加分组到组件中
        self.addGroup(
            FI.SETTING,
            InfoUIString.UPDATECARD_PIPEGROUP_TITLE,
            InfoUIString.UPDATECARD_PIPEGROUP_DETAIL,
            self.update_pipe_combobox,
        )
        group = self.addGroup(
            qfw.InfoBarIcon.SUCCESS,
            InfoUIString.UPDATECARD_VERSTATUSGROUP_TITLE,
            BasicString.APP_VERSION,
            self.update_status_check_button,
        )
        group.setSeparatorVisible(True)


class InformationUI(QFrame):
    """子页面基础ui类"""

    def __init__(self, parent=None):
        """初始化子页面"""
        super().__init__(parent)

        # 初始化卡片组件
        self.information_board_card = InformationBoardCardGroup(self)
        self.support_card = SupportCardGroup(self)
        self.update_card = UpdateCardGroup(self)

        # 组件布局
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.information_board_card)
        self.main_layout.addWidget(self.support_card)
        self.main_layout.addWidget(self.update_card)

        # 连接 支持 部分帮助文档按钮点击信号
        self.support_card.offline_document_button.clicked.connect(
            lambda: ShowInfobar.offline_button_infobar(self, self)
        )
        self.support_card.online_document_button.clicked.connect(
            lambda: ShowInfobar.online_button_infobar(self, self)
        )
