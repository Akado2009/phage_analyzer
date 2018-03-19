from PyQt4 import QtGui
from PyQt4 import QtCore

class InputDialog(QtGui.QDialog):
    def __init__(self, parent = None):
        super(InputDialog, self).__init__(parent)

        layout = QtGui.QVBoxLayout(self)

        self.text = QtGui.QTextEdit(self)
        layout.addWidget(self.text)

        buttons = QtGui.QDialogButtonBox(
            QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def getSequence(self):
        return self.text.toPlainText()

    @staticmethod
    def getDateTime(parent = None):
        dialog = InputDialog(parent)
        result = dialog.exec_()
        sequence = dialog.getSequence()
        return (sequence, result == QtGui.QDialog.Accepted)
