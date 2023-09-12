from PySide6.QtWidgets import QListWidget


class SamplesListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
