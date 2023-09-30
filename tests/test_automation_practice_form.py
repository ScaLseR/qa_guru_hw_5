"""автотест на заполнение и отправку формы
https://demoqa.com/automation-practice-form """
from selene import have
from os import path


def test_filling_and_send_form(open_url):
    open_url.element('#firstName').type('Бобр')
    open_url.element('#lastName').type('Добр')
    open_url.element('#userEmail').type('bobrdobr@test.ru')
    open_url.element('[for="gender-radio-1"]').click()
    open_url.element('#userNumber').type('1234567890')
    open_url.element('#dateOfBirthInput').click()
    open_url.element('.react-datepicker__month-select').type('May')
    open_url.element('.react-datepicker__year-select').type('2022')
    open_url.element('.react-datepicker__day--012').click()
    open_url.element('#subjectsInput').type('English').press_enter().type('Computer Science').press_enter()
    open_url.element('[for="hobbies-checkbox-2"]').click()
    open_url.element("#uploadPicture").send_keys(path.abspath('bobr.jpg'))
    open_url.element('#currentAddress').type('Бобриное Болото')
    open_url.element('#react-select-3-input').type('Haryana').press_enter()
    open_url.element('#react-select-4-input').type('Karnal').press_enter()
    open_url.element('#submit').click()

    open_url.element('.table').all('tr td:nth-child(2)').should(have.texts('Бобр Добр',
                                                                           'bobrdobr@test.ru',
                                                                           'Male',
                                                                           '1234567890',
                                                                           '12 May,2022',
                                                                           'English, Computer Science',
                                                                           'Reading',
                                                                           'bobr.jpg',
                                                                           'Бобриное Болото',
                                                                           'Haryana Karnal'))
