# Кнопки клавиатуры
start_reply_keyboard_markup = {
    "keyboard": [
        ["Запустить тест", "Узнать свою статистику", "Настройка параметров"]
    ],
    "resize_keyboard": True
}

startTest_reply_keyboard_markup = {
    "keyboard": [
        ["Завершить сейчас", "Посмотреть пример"]
    ],
    "resize_keyboard": True
}

setTopic_reply_keyboard = {
    "keyboard": [
        ["Отменить настройку темы"]
    ],
    "resize_keyboard": True
}

setQuestionsNumber_reply_keyboard_markup = {
    "keyboard": [
        ["Отменить настройку количества вопросов"]
    ],
    "resize_keyboard": True,
    "input_field_placeholder": "Введите количество вопросов"
}

setCorrectAnswersNumber_reply_keyboard_markup = {
    "keyboard": [
        ["Отменить настройку количества правильных ответов"]
    ],
    "resize_keyboard": True,
    "input_field_placeholder": "Введите количество правильных ответов"
}

# Inline-кнопки
reminder_inline_keyboard_markup = {
    "inline_keyboard": [
        [{"text": "Пройти тест снова", "callback_data": "Пройти тест снова"}],
        [{"text": "Отложить на 30 мин.", "callback_data": "Отложить на 30 мин."}]
    ]
}

# Команды меню
menu_reply_keyboard_markup = {
    "keyboard": [
        ["Выбрать тему", "Количество вопросов", "Количество правильных ответов"]
    ],
    "resize_keyboard": True
}
