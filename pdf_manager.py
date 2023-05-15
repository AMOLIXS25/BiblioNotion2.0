from fpdf import FPDF

from models.setting import SettingStorage


class NotePDF(FPDF):
    """Classe NotePDF"""
    def __init__(self, note_model):
        super().__init__()
        self.setting_storage = SettingStorage()
        self.note_model = note_model
        self.create_cover()
        self.create_content_page()

    def create_cover(self):
        """Méthode qui permet de créer la couverture de ma note"""
        self.add_page()
        self.set_fill_color(50, 50, 50)
        self.rect(0, 0, 10000, 10000, style="DF")
        if self.setting_storage.get_theme("default") == "Purple Drop":
            self.image("./res/images/icon_splash_screen_purple.png", 60, 80)
        else:
            self.image("./res/images/icon_splash_screen.png", 60, 80)
        self.set_text_color(255, 255, 255)
        self.set_font('Arial', 'B',  size=25)
        self.set_y(143)
        self.cell(h=50, w=0, txt=f"{self.note_model.title.title()}", align='C')
        self.set_y(260)
        self.set_font('Arial', 'B', size=16)
        self.cell(h=10, w=0, txt=f"Par Amaury", align='L')
        self.image("./res/images/unicorn.png", 14, 270)

    def create_content_page(self):
        """Méthode qui permet de créer la page contenu de la note"""
        self.add_page()
        self.set_text_color(50, 50, 50)
        self.set_font('Arial', 'BU', size=25)
        self.set_y(0)
        self.cell(h=50, w=0, txt=f"{self.note_model.title.title()}", align='L')
        self.set_y(40)
        self.set_font('Arial', '', size=14)
        self.multi_cell(190, 7, self.note_model.content, 0, 'L', False)


class BookNotesPDF(FPDF):
    """Classe BookNotesPdf"""
    def __init__(self, book_model, all_notes_of_the_book):
        super().__init__()
        self.setting_storage = SettingStorage()
        self.book_model = book_model
        self.all_notes_of_the_book = all_notes_of_the_book
        self.create_cover()
        self.create_content_page()

    def create_cover(self):
        """Méthode qui permet de créer la couverture du livre de note"""
        self.add_page()
        self.set_fill_color(50, 50, 50)
        self.rect(0, 0, 10000, 10000, style="DF")
        if self.setting_storage.get_theme("default") == "Purple Drop":
            self.image("./res/images/icon_splash_screen_purple.png", 60, 80)
        else:
            self.image("./res/images/icon_splash_screen.png", 60, 80)
        self.set_text_color(255, 255, 255)
        self.set_font('Arial', 'B',  size=25)
        self.set_y(143)
        self.cell(h=50, w=0, txt=f"Notes {self.book_model.title.title()}", align='C')
        self.set_y(260)
        self.set_font('Arial', 'B', size=16)
        self.cell(h=10, w=0, txt=f"Par Amaury", align='L')
        self.image("./res/images/unicorn.png", 14, 270)

    def create_content_page(self):
        """Méthode qui permet de créer la page de contenu pour les notes du livre"""
        for note in self.all_notes_of_the_book:
            self.add_page()
            self.set_text_color(50, 50, 50)
            self.set_font('Arial', 'BU', size=25)
            self.set_y(0)
            self.cell(h=50, w=0, txt=f"{note.title.title()}", align='L')
            self.set_y(40)
            self.set_font('Arial', '', size=14)
            self.multi_cell(190, 7, note.content, 0, 'L', False)