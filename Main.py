from Note import NoteManager


def main():
    note_manager = NoteManager()

    while True:
        print("\nNote App")
        print("1. Add Note")
        print("2. Edit Note")
        print("3. Delete Note")
        print("4. List Notes")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter note title: ")
            body = input("Enter note body: ")
            note_manager.add_note(title, body)
            print("Note added successfully!")

        elif choice == "2":
            note_id = int(input("Enter note ID to edit: "))
            note = note_manager.get_note_by_id(note_id)
            if note:
                title = input("Enter new title: ")
                body = input("Enter new body: ")
                note_manager.edit_note(note_id, title, body)
                print("Note edited successfully!")
            else:
                print("Note not found!")

        elif choice == "3":
            note_id = int(input("Enter note ID to delete: "))
            note = note_manager.get_note_by_id(note_id)
            if note:
                note_manager.delete_note(note_id)
                print("Note deleted successfully!")
            else:
                print("Note not found!")

        elif choice == "4":
            note_manager.list_notes()

        elif choice == "5":
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()