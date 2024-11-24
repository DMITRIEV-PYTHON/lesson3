# Задача "Рассылка писем":
# Часто при разработке и работе с рассылками писем(e-mail) они отправляются от одного и того же пользователя
# (администрации или службы поддержки). Тем не менее должна быть возможность сменить его в редких случаях.


def send_email(messange, recipient, *, sender="university.help@gmail.com"):
    variant = (".ru", ".com", ".net")
    if "@" not in recipient or "@" not in sender or not recipient.endswith(variant) or not sender.endswith(variant):
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)


send_email("Это сообщение для проверки связи", "vasyok1337@gmail.com")

send_email("Вы видите это сообщение как лучший студент курса!", "urban.fan@mail.ru", sender="urban.info@gmail.com")

send_email("Пожалуйста, исправьте задание", "urban.student@mail.ru", sender="urban.teacher@mail.uk")

send_email("Напоминаю самому себе о вебинаре", "urban.teacher@mail.ru", sender="urban.teacher@mail.ru")
