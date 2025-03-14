# здесь описан класс модального окно подтверждения отправки формы, которое появляется после успешной регистрации.

from selene import browser, have, be

class Modal:
    def __init__(self):
        self.modal = browser.element(".modal-content")  # Окно подтверждения
        self.table = self.modal.element(".table")  # Таблица с результатами

    def should_have_text(self, text):
        self.modal.should(be.visible).should(have.text(text))
        return self

    def should_have_registered_data(self, *values):
        self.table.all("td:nth-child(2)").should(have.texts(*values))
        return self