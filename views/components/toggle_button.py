# views/components/toggle_button.py

from PyQt5.QtWidgets import QPushButton


class ToggleButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCheckable(True)
        self.setFixedSize(60, 30)
        self.setStyleSheet("""
            QPushButton {
                background-color: #D3D3D3;
                border: 1px solid #8F8F91;
                border-radius: 4px;
                padding: 4px;
                font-weight: bold;
            }
            QPushButton:checked {
                background-color: #4CAF50;
                color: white;
            }
        """)
        self.setText("OFF")

    def setChecked(self, checked):
        super().setChecked(checked)
        if checked:
            self.setText("ON")
        else:
            self.setText("OFF")