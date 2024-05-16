input_name = './/label[text()="Имя"]/following-sibling::input'  # поле ввода имени
input_email = './/label[text()="Email"]/following-sibling::input'  # поле ввода почты
input_password = './/label[text()="Пароль"]/following-sibling::input'  # поле ввода пароля

button_registration = './/button[text()="Зарегистрироваться"]'  # конпка "Зарегистрироваться"
button_login_main_page = './/button[text()="Войти в аккаунт"]'  # кнопка "Войти в аккаунт" на главной странице
button_login = './/button[text()="Войти"]'  # кнопка "Войти" на странице авторизации
button_logout = './/li/button[text()="Выход"]'  # кнопка "Выход" в личном кабинете
button_checkout_main_page = './/button[text()="Оформить заказ"]'  # кнопка "Оформить заказ" на главной странице

link_login = './/a[starts-with(@class, "Auth_link")]'  # ссылка "Войти"

header_stellar_burger = './/div[starts-with(@class, "AppHeader_header__logo")]/a'  # ссылка на главную страницу в шапке
header_constructor = './/p[text()="Конструктор"]//parent::a'  # ссылка на конструктор в шапке
header_profile = './/p[text()="Личный Кабинет"]/parent::a'  # ссылка на "Личный Кабинет" в шапке

constructor_navigation_buns = './/div/span[text()="Булки"]'  # раздел навигации к "Булки" в конструкторе
constructor_navigation_sauces = './/div/span[text()="Соусы"]'  # раздел навигации к "Соусы" в конструкторе
constructor_navigation_fillings = './/div/span[text()="Начинки"]'  # раздел навигации к "Начинки" в конструкторе

constructor_header_buns = './/h2[text()="Булки"]'  # заголовок "Булки" в конструкторе
constructor_header_sauces = './/h2[text()="Соусы"]'  # заголовок "Соусы" в конструкторе
constructor_header_fillings = './/h2[text()="Начинки"]'  # заголовок "Начинки" в конструкторе

constructor_div_buns = './/span[text()="Булки"]/parent::div'  # div раздела "Булки" в конструкторе
constructor_div_sauces = './/span[text()="Соусы"]/parent::div'  # div раздела "Соусы" в конструкторе
constructor_div_fillings = './/span[text()="Начинки"]/parent::div'  # div раздела "Начинки" в конструкторе

first_ingredient = './/ul[1]/a[1]' # первый ингредиент в конструкторе
last_ingredient = './/ul[last()]/a[last()]'  # последний ингредиент в конструкторе
