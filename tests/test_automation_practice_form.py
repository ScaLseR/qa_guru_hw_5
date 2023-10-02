"""автотест на заполнение и отправку формы
https://demoqa.com/automation-practice-form """
from selene import have
from os import path
from selene.support.shared import browser


def test_filling_and_send_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Бобр')
    browser.element('#lastName').type('Добр')
    browser.element('#userEmail').type('bobrdobr@test.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('May')
    browser.element('.react-datepicker__year-select').type('2022')
    browser.element('.react-datepicker__day--012').click()
    browser.element('#subjectsInput').type('English').press_enter().type('Computer Science').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element("#uploadPicture").send_keys(path.abspath('bobr.jpg'))
    browser.element('#currentAddress').type('Бобриное Болото')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#submit').click()

    browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
    browser.element('.table').all('tr td:nth-child(2)').should(have.texts('Бобр Добр',
                                                                      'bobrdobr@test.ru',
                                                                      'Male',
                                                                      '1234567890',
                                                                      '12 May,2022',
                                                                      'English, Computer Science',
                                                                      'Reading',
                                                                      'bobr.jpg',
                                                                      'Бобриное Болото',
                                                                      'Haryana Karnal'))
