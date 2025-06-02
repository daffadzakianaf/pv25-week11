import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidgetItem, QStatusBar
)
from PyQt6.QtGui import QClipboard
from PyQt6 import uic


class BukuApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("form_buku.ui", self)  
        self.setWindowTitle("Manajemen Data Buku - Fitur Clipboard & Dock Pencarian")

        self.data = []
        self.load_data()

        self.pasteClipboard.clicked.connect(self.paste_from_clipboard)

        self.pencarian.textChanged.connect(self.filter_data)

        self.simpan.clicked.connect(self.simpan_data)

        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        self.statusbar.showMessage("Nama: Muhammad Daffa Dzaki Ahnaf | NIM: F1D022142")

    def paste_from_clipboard(self):
        clipboard: QClipboard = QApplication.clipboard()
        self.judul.setText(clipboard.text())

    def load_data(self):
        self.tabel.setRowCount(0)
        self.tabel.setColumnCount(4)
        self.tabel.setHorizontalHeaderLabels(["ID", "Judul", "Pengarang", "Tahun"])

        for row_data in self.data:
            row_pos = self.tabel.rowCount()
            self.tabel.insertRow(row_pos)
            for col_index, item in enumerate(row_data):
                self.tabel.setItem(row_pos, col_index, QTableWidgetItem(item))

    def filter_data(self):
        keyword = self.pencarian.text().lower()
        filtered_data = [row for row in self.data if keyword in " ".join(row).lower()]
        self.tabel.setRowCount(0)

        for row_data in filtered_data:
            row_pos = self.tabel.rowCount()
            self.tabel.insertRow(row_pos)
            for col_index, item in enumerate(row_data):
                self.tabel.setItem(row_pos, col_index, QTableWidgetItem(item))

    def simpan_data(self):
        judul = self.judul.text().strip()
        pengarang = self.pengarang.text().strip()
        tahun = self.tahun.text().strip()

        if not judul or not pengarang or not tahun:
            self.statusbar.showMessage(" Harap isi semua kolom sebelum menyimpan!")
            return

        id_baru = str(len(self.data) + 1)
        self.data.append([id_baru, judul, pengarang, tahun])

        self.load_data()
        self.judul.clear()
        self.pengarang.clear()
        self.tahun.clear()
        self.statusbar.showMessage(" Data berhasil disimpan.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BukuApp()
    window.show()
    sys.exit(app.exec())
