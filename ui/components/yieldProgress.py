from PySide6.QtWidgets import QDialog

from .yieldProgress_ui import Ui_YieldProgress


class YieldProgress(Ui_YieldProgress, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
