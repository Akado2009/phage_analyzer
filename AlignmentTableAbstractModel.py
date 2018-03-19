from PyQt4 import QtGui
from PyQt4 import QtCore

class TableAbstractModel(QtCore.QAbstractTableModel):

    def __init__(self, data, hor_header, vert_header, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.array_data = data
        self.horizontal_header = hor_header
        self.vertical_header = vert_header

    def rowCount(self, parent):
        return len(self.array_data)

    def columnCount(self, parent):
        if len(self.array_data) > 0:
            return len(self.array_data[0])
        return 0

    def set_item(self, index, value):
        self.array_data[index.row()][index.column()] = value

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != QtCore.Qt.DisplayRole and role != QtCore.Qt.EditRole:
            return None
        value = ''
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            value = self.array_data[row][col]
        elif role == QtCore.Qt.EditRole:
            row = index.row()
            col = index.column()
            value = self.array_data[row][col]
        return value

    def setData(self, index, value, role=QtCore.Qt.EditRole):
            row = index.row()
            col = index.column()
            self.array_data[row][col] = value
            return True

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.horizontal_header[col]
        elif orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            return self.vertical_header[col]
        return None

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

    def update(self, dataIn):
        print(dataIn)

    def sort(self, Ncol, order):

        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.array_data = sorted(self.arraydata, key=operator.itemgetter(Ncol))
        if order == Qt.DescendingOrder:
            self.arraydata.reverse()
        self.emit(SIGNAL("layoutChanged()"))
