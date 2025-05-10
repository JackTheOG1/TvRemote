import sys
from PyQt6.QtWidgets import QApplication
from logic import TVFunc

def main():
    app = QApplication(sys.argv)
    window = TVFunc()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
