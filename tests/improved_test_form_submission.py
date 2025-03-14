from Homework_5.model.pages.registration_page import RegistrationPage

def test_student_registration():
    registration_page = RegistrationPage()

    (registration_page
     .open()
     .fill_first_name("Анастасия")
     .fill_last_name("Кузнецова")
     .fill_email("kuznetsova@mail.com")
     .select_gender("Female")
     .fill_mobile("1234567890")
     .fill_date_of_birth(9, "May", "1984")
     .fill_subjects("Math")
     .select_hobbies("Reading")
     .upload_picture("resources/download.jpg")
     .fill_address("Ростов-на-Дону, ул.Города Волос")
     .select_state("Haryana")
     .select_city("Karnal")
     .submit()
     .should_have_registered("Анастасия Кузнецова")
     )