class Note(object):

    def __init__(self, note_id, date, title, text):
        self._note_id = note_id
        self._date = date
        self._title = title
        self._text = text

    def __str__(self):
        return (f'\nЗаметка: {self._note_id}\nДата создания(редактирования): {self._date}\n'
                f'Заголовок: {self._title}\nТело: {self._text}\n')

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    @property
    def note_id(self):
        return self._note_id

    @note_id.setter
    def note_id(self, note_id):
        self._note_id = note_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date