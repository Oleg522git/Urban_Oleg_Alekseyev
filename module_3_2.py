
def send_email(message, recipient, sender = "university.help@gmail.com"):

    exp_end_of_adress = ['.com','.ru','.net']
    end_of_sender = sender[-sender[::-1].find('.')-1:]
    end_of_recipient = recipient[-recipient[::-1].find('.')-1:]

    if not (end_of_sender in exp_end_of_adress
            and '@' in sender
            and end_of_recipient in exp_end_of_adress
          and '@' in recipient):
      print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


