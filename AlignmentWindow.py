from PyQt4 import QtGui
from PyQt4 import QtCore
from AlignmentTableAbstractModel import TableAbstractModel as alignment_model
from InputDialogWidget import InputDialog as input_dialog
import random
import sys


class AlignmentWindow(QtGui.QMainWindow):


    def __init__(self, sequences):

        super(AlignmentWindow, self).__init__()
        self.setGeometry(50, 50, 700, 400)
        self.setWindowTitle('Alignment Analysis')
        self.move(QtGui.QApplication.desktop().screen().rect().center()- self.rect().center())

        self.alignment = sequences
        self.add_main_menu()
        self.add_toolbar()
        self.alignment_window_view()

    def add_main_menu(self):
        mainMenu = self.menuBar()

        # file submenu
        fileMenu = mainMenu.addMenu('&File')

        quitAction = QtGui.QAction("&Quit", self)
        quitAction.setShortcut("Ctrl+Q")
        quitAction.setStatusTip("Leave the application")
        quitAction.triggered.connect(self.close_application)

        fileMenu.addAction(quitAction)

    def add_toolbar(self):
        changeMultipleAction = QtGui.QAction('Change nucleotides', self)
        changeMultipleAction.triggered.connect(self.change_multiple)
        self.toolBar = self.addToolBar('Alingment correction')
        self.toolBar.addAction(changeMultipleAction)

        addSequence = QtGui.QAction('Add sequence', self)
        addSequence.triggered.connect(self.add_sequence)

        self.toolBar.addAction(addSequence)

        deleteSequence = QtGui.QAction('Delete sequence', self)
        deleteSequence.triggered.connect(self.delete_sequence)

        self.toolBar.addAction(deleteSequence)

        realignSection = QtGui.QAction('Realign selection', self)
        realignSection.triggered.connect(self.realign_selection)

        self.toolBar.addAction(realignSection)

        reverseComplement = QtGui.QAction('Reverse complement', self)
        reverseComplement.triggered.connect(self.reverse_complement)

        self.toolBar.addAction(reverseComplement)
        # testPopup = QtGui.QAction('Popup', self)
        # testPopup.triggered.connect(self.pop_up_editor)
        #
        # self.toolBar.addAction(testPopup)

    def change_multiple(self):
        nucleotide, ok = QtGui.QInputDialog.getText(self, 'Nucleotide substitution', 'Enter nucleotide')
        if ok:
            row = self.alignment_table.selectedIndexes()
            for _row in row:
                self.alignment_table.model().set_item(_row, str(nucleotide))

    def add_sequence(self):
        seq, ok = input_dialog.getDateTime()
        #test case - AGGGGGGGGGGGG
        if ok:
            self.table_data.append(str(seq))
            self.alignment_table.model().layoutChanged.emit()

    def delete_sequence(self):
        row = self.alignment_table.selectedIndexes()
        for _row in row:
            del self.table_data[_row.row()]
        self.alignment_table.model().layoutChanged.emit()

    def realign_selection(self):
        print(1)

    def rev_comp(self, sequence):
        reverse_alphabet = {
                'A': 'T',
                'T': 'A',
                'C': 'G',
                'G': 'C',
                'N': 'N',
                '-': '-'
            }
        rev_comp_sequence = ''
        for sym in sequence[::-1]:
            rev_comp_sequence += reverse_alphabet[sym]
        return rev_comp_sequence

    def reverse_complement(self):

        row = self.alignment_table.selectedIndexes()
        if len(row) != 0:
            for _row in row:
                self.table_data[_row.row()] = list(self.rev_comp(self.table_data[_row.row()]))
        else:
            for i in range(len(self.table_data)):
                self.table_data[i] = list(self.rev_comp(self.table_data[i]))
        self.alignment_table.model().layoutChanged.emit()

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Quit', 'Do you sure want to exit?', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def alignment_window_view(self):
        self.get_table_data(self.alignment)
        self.alignment_table = self.create_table()
        self.setCentralWidget(self.alignment_table)
        self.show()

    def get_table_data(self, data):
        self.table_data = [list(seq) for seq in data]

    def create_table(self):
        tv = QtGui.QTableView()

        hor_header = ['{}'.format(i) for i in range(len(self.table_data[0]))]
        vert_header = ['Sequence number {}'.format(i) for i in range(len(self.table_data))]
        table_model = alignment_model(self.table_data, hor_header, vert_header, self)
        tv.setModel(table_model)

        tv.setShowGrid(False)

        vh = tv.verticalHeader()
        vh.setVisible(True)

        hh = tv.horizontalHeader()
        hh.setStretchLastSection(False)

        tv.resizeColumnsToContents()
        tv.resizeRowsToContents()
        tv.setSortingEnabled(False)

        return tv
