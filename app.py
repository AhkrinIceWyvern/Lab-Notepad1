import datetime
from controller import Controller
from modelJSON import ModelJSON
from note import Note
from view import View


def run():
    controller = Controller(ModelJSON("notes.json"), View())

    while True:
        print_menu()
        command = input('Зробіть вибір: ')

        if command == '7':
            break
        elif command == '1':
            create_note(controller)
        elif command == '2':
            read_note(controller)
        elif command == '3':
            update_note(controller)
        elif command == '4':
            delete_note(controller)
        elif command == '5':
            delete_all_notes(controller)
        elif command == '6':
            read_all_notes(controller)
        else:
            print('Команда не знайдена')


def print_menu():
    print('\n╔════════════════════════════════════════════╗')
    print('║                  Меню                      ║')
    print('╠════════════════════════════════════════════╣')
    print('║ 1 - Створити нотатку                       ║')
    print('║ 2 - Прочитати нотатку                      ║')
    print('║ 3 - Оновити нотатку                        ║')
    print('║ 4 - Видалити нотатку                       ║')
    print('║ 5 - Видалити всі нотатки                   ║')
    print('║ 6 - Вивести список заміток                 ║')
    print('║ 7 - Вийти                                  ║')
    print('╚════════════════════════════════════════════╝')


def create_note(controller):
    print('\n╔════════════════════════════════════════════╗')
    print('║          Створення нотатки                 ║')
    print('╠════════════════════════════════════════════╣')
    
    note_data = get_note_data()
    controller.create_note_with_id(note_data)

    print('╚════════════════════════════════════════════╝')


def read_note(controller):
    print('\n╔════════════════════════════════════════════╗')
    print('║          Прочитати нотатку                 ║')
    print('╠════════════════════════════════════════════╣')
    
    if controller.notes_exist():
        note_id = get_valid_note_id(controller)
        controller.show_note(note_id)

    print('╚════════════════════════════════════════════╝')


def update_note(controller):
    if controller.notes_exist():
        print('\n╔════════════════════════════════════════════╗')
        print('║          Оновити нотатку                   ║')
        print('╠════════════════════════════════════════════╣')

        note_id = get_valid_note_id(controller)
        if controller.note_id_exist(note_id):
            controller.update_note(note_id, get_note_data())

        print('╚════════════════════════════════════════════╝')


def delete_note(controller):
    if controller.notes_exist():
        print('\n╔════════════════════════════════════════════╗')
        print('║          Видалити нотатку                  ║')
        print('╠════════════════════════════════════════════╣')

        note_id = get_valid_note_id(controller)
        if controller.note_id_exist(note_id):
            controller.delete_note(note_id)

        print('╚════════════════════════════════════════════╝')



def delete_all_notes(controller):
    if controller.notes_exist():
        print('\n╔════════════════════════════════════════════╗')
        print('║         Видалити всі нотатки               ║')
        print('╠════════════════════════════════════════════╣')

        if input('Ви впевнені, що хочете видалити всі нотатки? (Y/N): ').capitalize() == 'Y':
            controller.delete_all_notes()

        print('╚════════════════════════════════════════════╝')



def read_all_notes(controller):
    if controller.notes_exist():
        print('\n╔════════════════════════════════════════════╗')
        print('║         Вивести список заміток              ║')
        print('╠════════════════════════════════════════════╣')

        controller.show_notes()

        print('╚════════════════════════════════════════════╝')



def get_note_data():
    note_id = 0
    date = datetime.datetime.now()
    print('╔════════════════════════════════════════════╗')
    title = input('║ Введіть заголовок нотатки: ')
    text = input('║ Введіть тіло нотатки: ')
    print('╚════════════════════════════════════════════╝')
    return Note(note_id, date, title, text)



def get_valid_note_id(controller):
    while True:
        print('╔════════════════════════════════════════════╗')
        note_id = input('║ Введіть id нотатки: ')
        if note_id.isdigit() and int(note_id) > 0 and controller.note_id_exist(int(note_id)):
            return int(note_id)
        else:
            print('║ Введіть існуючий позитивний id нотатки! ')
            print('╚════════════════════════════════════════════╝')



if __name__ == "__main__":
    run()
