# views/components/step_button.py

from PyQt5.QtWidgets import QPushButton

class StepButton(QPushButton):
    def __init__(self, step_index, parent=None):
        super().__init__(parent)
        self.step_index = step_index
        self.setFixedSize(80, 40)
        self.setText(f"Step {step_index + 1}")

    def connect_step(self, callback):
        self.clicked.connect(lambda: callback(self.step_index))
