import allure
from selene import browser, have, be, command


def test_fill_form():
    with allure.step("Заполняю личные данные"):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element("#firstName").type("Анастасия")
        browser.element("#lastName").type("Кузнецова")
        browser.element("#userEmail").type("kuznetsova@mail.com")

    with allure.step("Выбираю пол"):
        browser.element('[for="gender-radio-2"]').click()

    with allure.step("Ввожу номер телефона"):
        browser.element("#userNumber").type("1234567890")

    with allure.step("Выбираю дату раждения"):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").type("1984")
        browser.element(".react-datepicker__month-select").type("May")
        browser.element(".react-datepicker__day--009").click()

    with allure.step("Ввожу предметы"):
        browser.element("#subjectsInput").type("Math").press_enter() #тут повозилась - не знала, что это выпадашка, пыталась ввести свой текст

    with allure.step("Выбираю хобби"):
        browser.element('[for="hobbies-checkbox-2"]').click()

    with allure.step("Загружаю изображение"):
        browser.element("#uploadPicture").send_keys("/Users/kuznetsova/Desktop/download.jpg")

    with allure.step("Ввожу адрес"):
        browser.element("#currentAddress").type("Ростов-на-Дону, ул.Города Волос")


    with allure.step("Выбираю штат и город"):
        browser.element("#state").perform(command.js.scroll_into_view).click()
        browser.all("div.css-11unzgr").element_by(have.text("Haryana")).click()
        browser.element("#city").should(be.clickable).click()
        browser.all("div.css-11unzgr").element_by(have.text("Karnal")).click()

    with allure.step("Отправляю форму"):
        browser.element("#submit").press_enter()

    with allure.step("Проверяю, что форма отправлена"):
        browser.element(".modal-title").should(have.text("Thanks for submitting the form"))