from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel


class BlockLabelDialog(QLabel):
    def __init__(
        self,
        parent=None,
        modality: Qt.WindowModality = Qt.WindowModality.ApplicationModal,
        *,
        autoShow: bool = False
    ):
        super().__init__(parent)

        self.setWindowFlag(Qt.WindowType.Dialog, True)
        self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
        self.setWindowModality(modality)
        self.setWindowTitle("Please Wait")
        self.setMinimumWidth(200)
        self.setMargin(20)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.autoShow = autoShow

    def show(self):
        super().show()
        QApplication.processEvents()

    def __enter__(self):
        if self.autoShow:
            self.show()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        self.deleteLater()
