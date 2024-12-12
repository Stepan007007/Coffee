from PyQt6.QtWidgets import QWidget, QApplication, QTableWidgetItem
import sqlite3
from PyQt6 import uic
import sys


class Coffe(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffe.sql')
        self.cur = self.con.cursor()
        self.cur.execute('''SELECT * FROM coffee''')
        res = self.cur.fetchall()
        print(res)
        self.tableWidget.setRowCount(len(res))
        for row_index, row_data in enumerate(res):
            for col_index, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffe()
    ex.show()
    sys.exit(app.exec())