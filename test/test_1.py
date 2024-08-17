def test_auth(login_page):
    login_page.open_page()
    login_page.registration_form('Test', 'Testov', 'python1356@yandex.ru', 'privet!!@2222',
                                 'privet!!@2222')
    login_page.check_success_text('Thank you for registering with Main Website Store.')


def test_exist_email(login_page):
    login_page.open_page()
    login_page.registration_form('Test', 'Testov', 'test44@yandex.ru', 'privet!!@2222',
                                 'privet!!@2222')

    login_page.check_text('There is already an account with this email address. If you are sure that it is your email '
                          'address, click here to get your password and access your account.')


def test_incorrect_email(login_page):
    login_page.open_page()
    login_page.registration_form('Test', 'Testov', 'test44', 'privet!!@2222',
                                 'privet!!@2222')

    login_page.check_email('Please enter a valid email address (Ex: johndoe@domain.com).')
