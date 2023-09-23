import json
from pathlib import Path

from PySide6.QtCore import QByteArray, QMimeData, Qt
from PySide6.QtGui import QDrag, QPixmap
from PySide6.QtWidgets import QListWidget, QListWidgetItem, QMessageBox, QProgressDialog


class SamplesListWidget(QListWidget):
    PathlibPathRole = Qt.ItemDataRole.UserRole

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setViewMode(QListWidget.ViewMode.IconMode)
        self.setEditTriggers(QListWidget.EditTrigger.NoEditTriggers)
        self.setMovement(QListWidget.Movement.Static)
        self.setDragDropMode(QListWidget.DragDropMode.DragOnly)
        self.setDragEnabled(True)
        self.setSelectionMode(QListWidget.SelectionMode.MultiSelection)

    def setSamples(self, samples: list[Path]):
        self.clear()

        samplesNum = len(samples)
        progressDialog = QProgressDialog("", "Abort", 0, samplesNum, self)
        progressDialog.setWindowModality(Qt.WindowModality.ApplicationModal)

        for i, sample in enumerate(samples):
            item = QListWidgetItem(QPixmap(str(sample)), f"{sample.stem[:3]}...", self)
            item.setData(self.PathlibPathRole, sample)
            self.addItem(item)

            if samplesNum >= 1000:
                updateInterval = 100
            elif samplesNum >= 100:
                updateInterval = 10
            else:
                updateInterval = 1
            if i % updateInterval == 0:
                progressDialog.setValue(i)
                progressDialog.setLabelText(f"{i + 1}/{samplesNum}")

            if progressDialog.wasCanceled():
                break

        progressDialog.setValue(samplesNum)
        QMessageBox.information(
            self, None, f"Loaded {self.model().rowCount()} samples."
        )

    def startDrag(self, supportedActions: Qt.DropAction):
        drag = QDrag(self)
        items = self.selectedItems()
        paths = [str(item.data(self.PathlibPathRole).resolve()) for item in items]
        mimeDataString = json.dumps(paths, ensure_ascii=False)

        mimeData = QMimeData()
        mimeData.setData(
            "application/ao-ocr-model_sample",
            QByteArray(mimeDataString.encode("utf-8")),
        )

        drag.setPixmap(items[0].icon().pixmap(items[0].icon().availableSizes()[0]))
        drag.setMimeData(mimeData)
        if drag.exec(Qt.DropAction.MoveAction) == Qt.DropAction.MoveAction:
            for item in items:
                index = self.indexFromItem(item)
                self.model().removeRow(index.row())
