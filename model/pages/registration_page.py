from selene import browser, have, be, command
import os


class RegistrationPage:

# Открытие страницы формы регистрации https://demoqa.com/automation-practice-form.
    def open(self):
        browser.open("https://demoqa.com/automation-practice-form")
        return self

# Ввод value в поле “Имя” (#firstName).
    def fill_first_name(self, value):
        browser.element("#firstName").type(value)
        return self

# Ввод value в поле “Фамилия” (  # lastName)
    def fill_last_name(self, value):
        browser.element("#lastName").type(value)
        return self


# Ввод email
    def fill_email(self, value):
        browser.element("#userEmail").type(value)
        return self

# Выбор пола
    def select_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
        return self

# Ввод телефона
    def fill_mobile(self, value):
        browser.element("#userNumber").type(value)
        return self


# Выбор даты рождения
    def fill_date_of_birth(self, day, month, year):
        # Открытие календаря для выбора даты
        browser.element("#dateOfBirthInput").click()  # Нажимаем на поле выбора даты рождения

        # Выбор года
        browser.element(".react-datepicker__year-select").type(year)  # Вводим год (например, 1984)

        # Выбор месяца
        browser.element(".react-datepicker__month-select").type(month)  # Вводим месяц (например, May)

        # Выбор дня
        browser.element(f".react-datepicker__day--0{day:02d}").click()  # Вводим день, добавляем ведущий ноль, если необходимо

        return self

# Ввод предметов. Позволяет вводить несколько предметов через *subjects, например: registration_page.fill_subjects("Math", "Physics")
    def fill_subjects(self, *subjects):
        for subject in subjects:
            browser.element("#subjectsInput").type(subject).press_enter()
        return self

# Выбор хобби
    def select_hobbies(self, *hobbies):
        for hobby in hobbies:
            browser.all('.custom-checkbox').element_by(have.exact_text(hobby)).click()
        return self

# Загрузка картинк
    def upload_picture(self, file_name):
        file_path = os.path.abspath(file_name)
        browser.element("#uploadPicture").send_keys(file_path)
        return self

# Ввод адреса
    def fill_address(self, value):
        browser.element("#currentAddress").type(value)
        return self

# Выбор штата и города
    def select_state(self, state):
        browser.element("#state").perform(command.js.scroll_into_view).click()
        browser.all("div.css-11unzgr").element_by(have.text(state)).click()
        return self

    def select_city(self, city):
        browser.element("#city").click()
        browser.all("div.css-11unzgr").element_by(have.text(city)).click()
        return self

# Отправка формы
    def submit(self):
        browser.element("#submit").press_enter()
        return self

# Проверка успешной регистрации.
# Проверяет, что появилось модальное окно с заголовком “Thanks for submitting the form”.
# Проверяет, что в таблице есть имя студента.
    def should_have_registered(self, student_name):
        browser.element(".modal-title").should(have.text("Thanks for submitting the form"))
        browser.element(".table").should(have.text(student_name))
        return self