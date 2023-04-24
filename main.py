import json
import os.path
import datetime

# Функция для сохранения заметок в файл
def save_notes(notes):
    with open('notes.json', 'w') as f:
        json.dump(notes, f)

# Функция для загрузки заметок из файла
def load_notes():
    if os.path.isfile('notes.json'):
        with open('notes.json', 'r') as f:
            return json.load(f)
    else:
        return []

# Функция для добавления новой заметки
def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "created_at": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена.")

# Функция для вывода списка всех заметок
def list_notes():
    if len(notes) == 0:
        print("Список заметок пуст.")
    else:
        for note in notes:
            print(f"{note['id']}. {note['title']} ({note['created_at']})")

# Функция для вывода деталей заметки по ее номеру
def view_note():
    id = int(input("Введите номер заметки: "))
    note = next((note for note in notes if note['id'] == id), None)
    if note:
        print(f"Заголовок: {note['title']}\nТекст: {note['body']}\nСоздано: {note['created_at']}\nИзменено: {note['updated_at']}")
    else:
        print("Заметка не найдена.")

# Функция для редактирования заметки по ее номеру
def edit_note():
    id = int(input("Введите номер заметки: "))
    note = next((note for note in notes if note['id'] == id), None)
    if note:
        title = input(f"Введите новый заголовок заметки ({note['title']}): ")
        body = input(f"Введите новый текст заметки ({note['body']}): ")
        note['title'] = title if title else note['title']
        note['body'] = body if body else note['body']
        note['updated_at'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        save_notes(notes)
        print("Заметка успешно изменена.")
    else:
        print("Заметка не найдена.")

# Функция для удаления заметки по ее номеру
def delete_note():
    id = int(input("Введите номер заметки: "))
    note = next((note for note in notes if note['id'] == id), None)
    if note:
        notes.remove(note)
        save_notes(notes)
        print("Заметка успешно удалена.")
    else:
        print("Заметка не найдена.")

# Загрузка заметок из файла при запуске программы
notes = load_notes()

# Основной цикл программы
while True:
    print("\nВыберите действие:")
    print("1. Добавить заметку")
    print("2. Просмотреть список заметок")
    print("3. Просмотреть детали заметки")
    print("4. Изменить заметку")
    print("5. Удалить заметку")
    print("6. Выйти из программы")
    choice = input("> ")
    if choice == "1":
        add_note()
    elif choice == "2":
        list_notes()
    elif choice == "3":
        view_note()
    elif choice == "4":
        edit_note()
    elif choice == "5":
        delete_note()
    elif choice == "6":
        break
    else:
        print("Неверный выбор.")

# Сохранение заметок в файл при завершении программы
save_notes(notes)
