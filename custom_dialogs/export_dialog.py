from PySide6.QtWidgets import QDialog
from PySide6 import QtCore

from generate_uis.export_view_ui import Ui_ExportWindow


class ExportDialog(QDialog, Ui_ExportWindow):
    """ConvertNoteDialog classe"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pdf = False
        self.txt = False
        self.pdf_frame.setCursor(QtCore.Qt.PointingHandCursor)
        self.txt_frame.setCursor(QtCore.Qt.PointingHandCursor)
        self.connect_signals_to_slots()

    @property
    def is_txt(self):
        return self.txt
    
    @property
    def is_pdf(self):
        return self.pdf
    
    def connect_signals_to_slots(self):
        """Méthode qui permet de connecter les signaux à leurs slots"""
        self.quit_button.clicked.connect(self.on_quit_button_clicked)
        self.pdf_frame.mousePressEvent = self.on_pdf_frame_mouse_pressed
        self.txt_frame.mousePressEvent = self.on_txt_frame_mouse_pressed

    def on_pdf_frame_mouse_pressed(self, event):
        self.pdf = True
        self.close()

    def on_txt_frame_mouse_pressed(self, event):
        self.txt = True
        self.close()

    def on_quit_button_clicked(self):
        self.close()