class MailBox:
    def __init__(self):
        self.inbox_list = []

    def receive(self):
        return self.inbox_list


class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        if fl_read:
            self.is_read = True

    def __bool__(self):
        return self.is_read

mail = MailBox()
mail.inbox_list = []

lst_in = ['sc_lib@list.ru; От Балакирева; Успехов в IT!',
          'mail@list.ru; Выгодное предложение; Вам одобрен кредит.',
          'Python ООП; Балакирев С.М.; 2022',
          'mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.']

for item in lst_in:
    item = item.split(";")
    mail_from = item[0]
    title = item[1]
    content = item[2]
    mail.inbox_list.append(MailItem(mail_from, title, content))

mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)

mail.receive()

inbox_list_filtered = list(filter(lambda x: bool(x), mail.inbox_list))

# для проверки
print(len(mail.inbox_list))
print(len(inbox_list_filtered))
