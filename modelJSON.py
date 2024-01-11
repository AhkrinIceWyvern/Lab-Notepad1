import json

from view import View
from note import Note

class ModelJSON(object):

    def __init__(self, filename):
        self.filename = filename
        self.notes = list()

    def create_note_with_id(self, note):
        self.notes = self.read_notes()
        max_id = max((item.note_id for item in self.notes), default=0)
        note.note_id = max_id + 1
        self.notes.append(note)
        self.write_json(self.notes)

    def create_note(self, note):
        self.notes = self.read_notes()
        max_id = max((item.note_id for item in self.notes), default=0)
        note.note_id = max_id + 1
        self.notes.append(note)
        self.write_json(self.notes)

    def read_note(self, search_id):
        self.notes = self.read_notes()
        for note in self.notes:
            if note.note_id == search_id:
                return note
        else:
            self.view.display_note_id_not_exist(search_id)

    def read_notes(self):
        return self.read_json()

    def update_note(self, search_id, note):
        self.notes = self.read_notes()
        for item in self.notes:
            if item.note_id == search_id:
                item.date = note.date
                item.title = note.title
                item.text = note.text

        self.write_json(self.notes)

    def delete_note(self, search_id):
        self.notes = self.read_notes()
        for index, note in enumerate(self.notes):
            if note.note_id == search_id:
                del self.notes[index]

        self.write_json(self.notes)

    def delete_all_notes(self):
        self.notes = self.read_notes()
        self.notes.clear()
        self.write_json(self.notes)

    def write_json(self, notes):
        json_strings_list = [{'id': note.note_id, 'date': note.date, 'title': note.title, 'text': note.text} for note in notes]
        notes_json = json.dumps(json_strings_list, indent=4, ensure_ascii=False, sort_keys=False, default=str)

        with open(self.filename, "w", encoding='utf-8') as my_file:
            my_file.write(notes_json)

    def read_json(self):
        notes_list = list()
        try:
            with open(self.filename, "r", encoding='utf-8') as my_file:
                notes_json = my_file.read()
            data = json.loads(notes_json)
            data.sort(key=lambda x: x['date'])
            notes_list = [Note(item['id'], item['date'], item['title'], item['text']) for item in data]
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass

        return notes_list
