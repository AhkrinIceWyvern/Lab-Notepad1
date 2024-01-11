from tabulate import tabulate
from datetime import datetime

class View(object):

    @staticmethod
    def show_separator_line():
        print('╔════════════════════════════════════════════╗')

    @staticmethod
    def show_line_separator():
        print('║--------------------------------------------------------------║')

    def show_number_point_list(self, notes):
        if not notes:
            self.show_empty_list_message()
        else:
            headers = ["ID", "Дата", "Заголовок"]
            # Відсортовуємо список за ID перед виведенням
            sorted_notes = sorted(notes, key=lambda note: note.note_id)
            data = [[note.note_id, self.format_date(note.date), note.title] for note in sorted_notes]
            print(tabulate(data, headers=headers, tablefmt="pretty"))

    def show_note(self, note):
        headers = ["ID", "Дата", "Заголовок", "Текст"]
        data = [[note.note_id, self.format_date(note.date), note.title, note.text]]
        print(tabulate(data, headers=headers, tablefmt="pretty"))

    def format_date(self, date_str):
        date_object = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
        formatted_date = date_object.strftime("%H:%M %d.%m.%Y")
        return formatted_date

    def show_empty_list_message(self):
        self.show_separator_line()
        print('║ Список нотаток порожній. ')
        self.show_separator_line()

    def display_note_id_not_exist(self, note_id):
        self.show_line_separator()
        print('║ Замітка з id: {} не знайдено.'.format(note_id))
        self.show_line_separator()

    def display_note_id_exist(self, note_id):
        self.show_line_separator()
        print('║ Замітка з id: {} вже є.'.format(note_id))
        self.show_line_separator()

    def display_note_stored(self, note_id):
        self.show_separator_line()
        print(f'║ Замітка успішно додана з ID: {note_id} ')
        self.show_separator_line()

    def display_note_updated(self, note_id):
        self.show_line_separator()
        print('║ Замітка з id:{} успішно оновлена! '.format(note_id))
        self.show_line_separator()

    def display_note_deletion(self, note_id):
        self.show_line_separator()
        print('║ Видалення замітки з id: {} виконано! '.format(note_id))
        self.show_line_separator()

    def display_all_notes_deletion(self):
        self.show_line_separator()
        print('║ Всі замітки видалені! ')
        self.show_line_separator()
