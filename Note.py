import json
import os
from Notes import Note


class NoteManager:
    def __init__(self, storage_file="notes.json"):
        self.storage_file = storage_file
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "r") as f:
                notes_data = json.load(f)
                return [Note(**note_data) for note_data in notes_data]
        else:
            return []

    def save_notes(self):
        with open(self.storage_file, "w") as f:
            json.dump([note.to_dict() for note in self.notes], f, indent=4)

    def add_note(self, title, body):
        id = len(self.notes) + 1
        self.notes.append(Note(id, title, body))
        self.save_notes()

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save_notes()

    def edit_note(self, note_id, title, body):
        for note in self.notes:
            if note.id == note_id:
                note.update(title, body)
                self.save_notes()
                break

    def list_notes(self):
        for note in self.notes:
            print(f"ID: {note.id}, Title: {note.title}, Created At: {note.created_at}")

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None