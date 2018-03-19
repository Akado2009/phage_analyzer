import sys

from PyQt4 import QtGui
from PyQt4 import QtCore
import AlignmentWindow


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(150, 150, 700, 400)
        self.setWindowTitle('Phage Analyzer')
        self.move(QtGui.QApplication.desktop().screen().rect().center()- self.rect().center())
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Windows'))
        self.add_main_menu()
        self.main_window_view()

    def add_main_menu(self):
        mainMenu = self.menuBar()

        # file submenu
        fileMenu = mainMenu.addMenu('&File')

        openAction = QtGui.QAction("&Open file", self)
        openAction.setShortcut("Ctrl+O")
        openAction.setStatusTip("Open existing document")
        openAction.triggered.connect(self.open_file)

        quitAction = QtGui.QAction("&Quit", self)
        quitAction.setShortcut("Ctrl+Q")
        quitAction.setStatusTip("Leave the app")
        quitAction.triggered.connect(self.close_application)

        fileMenu.addAction(openAction)
        fileMenu.addAction(quitAction)

        pipelineMenu = mainMenu.addMenu('&Pipeline')

        blastAction = QtGui.QAction("&Start pipeline", self)
        blastAction.setShortcut("Ctrl+B")
        blastAction.setStatusTip("Start pipeline & Generate consensus")
        blastAction.triggered.connect(self.calculate_consensus)

        pipelineMenu.addAction(blastAction)

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Quit', 'Do you sure want to exit?', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def open_file(self):
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File',".","(*.fasta)")
        if self.filename:
            with open(self.filename, "rt") as file:
                self.text.setText(file.read())


    def calculate_consensus(self):
        seqs = ['ATTTTTTTTTTTG', 'ATTTTTTTTTTTG', 'ATTTTTTTTTTTG', 'ATTTTTTTTTTTG', 'ATTTTTTTTTTTG']
        self.alignment_window = AlignmentWindow.AlignmentWindow(seqs)
        self.close()
        self.alignment_window.show()

    def create_text_editor(self):
        self.text = QtGui.QTextEdit(self)
        self.setCentralWidget(self.text)
        self.text.setFontPointSize(20)

    def main_window_view(self):
        self.create_text_editor()
        self.text.setDisabled(True)
        self.statusbar = self.statusBar()
        self.show()


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
