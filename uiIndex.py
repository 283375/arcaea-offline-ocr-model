import logging
import sys
import time

from PySide6.QtWidgets import QApplication

from ui.mainWindow import MainWindow

# logging.basicConfig(
#     filename=f"ui-{int(time.time() * 1000)}.log",
#     filemode="w",
#     level=logging.DEBUG,
# )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyle("fusion")

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
