
import sqlite3
import tkinter as tk
import tkinter.ttk as ttk  # Import ttk for themed widgets
from tkinter import messagebox

# Connect to SQLite database (creates the database if it doesn't exist)
conn = sqlite3.connect("notes_flashcards.db")
cursor = conn.cursor()

# Create tables for notes and flashcards if they don't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS flashcards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        answer TEXT
    )
""")
conn.commit()

# Function to add a note
def add_note():
    note = note_entry.get("1.0", tk.END).strip()
    if note:
        cursor.execute("INSERT INTO notes (content) VALUES (?)", (note,))
        conn.commit()
        note_entry.delete("1.0", tk.END)
        load_notes()
    else:
        messagebox.showwarning("Warning", "Note cannot be empty")

# Function to load and display notes
def load_notes():
    notes_listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM notes")
    for row in cursor.fetchall():
        notes_listbox.insert(tk.END, row[1])

# Function to view a specific note
def view_note():
    selected_note_index = notes_listbox.curselection()
    if selected_note_index:
        note_content = notes_listbox.get(selected_note_index)
        messagebox.showinfo("Note", note_content)

# Function to add a flashcard
def add_flashcard():
    question = flashcard_question_entry.get().strip()
    answer = flashcard_answer_entry.get().strip()
    if question and answer:
        cursor.execute("INSERT INTO flashcards (question, answer) VALUES (?, ?)", (question, answer))
        conn.commit()
        flashcard_question_entry.delete(0, tk.END)
        flashcard_answer_entry.delete(0, tk.END)
        load_flashcards()
    else:
        messagebox.showwarning("Warning", "Question and answer cannot be empty")

# Function to load and display flashcards
def load_flashcards():
    flashcards_listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM flashcards")
    for row in cursor.fetchall():
        flashcards_listbox.insert(tk.END, row[1])

# Function to view a specific flashcard
def view_flashcard():
    selected_flashcard_index = flashcards_listbox.curselection()
    if selected_flashcard_index:
        flashcard_content = flashcards_listbox.get(selected_flashcard_index)
        cursor.execute("SELECT * FROM flashcards WHERE question=?", (flashcard_content,))
        flashcard = cursor.fetchone()
        messagebox.showinfo("Flashcard", f"Question: {flashcard[1]}\nAnswer: {flashcard[2]}")

# GUI setup
root = tk.Tk()
root.title("Notes & Flashcards App")

# Tabs Setup
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Frame for Notes
notes_frame = tk.Frame(notebook)
notebook.add(notes_frame, text="Notes")

# Notes section
note_label = tk.Label(notes_frame, text="Write a note:")
note_label.pack(pady=5)

note_entry = tk.Text(notes_frame, height=5, width=40)
note_entry.pack(pady=5)

add_note_button = tk.Button(notes_frame, text="Add Note", command=add_note)
add_note_button.pack(pady=5)

notes_listbox = tk.Listbox(notes_frame, width=50, height=10)
notes_listbox.pack(pady=5)

view_note_button = tk.Button(notes_frame, text="View Note", command=view_note)
view_note_button.pack(pady=5)

# Frame for Flashcards
flashcards_frame = tk.Frame(notebook)
notebook.add(flashcards_frame, text="Flashcards")

# Flashcards section
flashcard_question_label = tk.Label(flashcards_frame, text="Question:")
flashcard_question_label.pack(pady=5)

flashcard_question_entry = tk.Entry(flashcards_frame, width=40)
flashcard_question_entry.pack(pady=5)

flashcard_answer_label = tk.Label(flashcards_frame, text="Answer:")
flashcard_answer_label.pack(pady=5)

flashcard_answer_entry = tk.Entry(flashcards_frame, width=40)
flashcard_answer_entry.pack(pady=5)

add_flashcard_button = tk.Button(flashcards_frame, text="Add Flashcard", command=add_flashcard)
add_flashcard_button.pack(pady=5)

flashcards_listbox = tk.Listbox(flashcards_frame, width=50, height=10)
flashcards_listbox.pack(pady=5)

view_flashcard_button = tk.Button(flashcards_frame, text="View Flashcard", command=view_flashcard)
view_flashcard_button.pack(pady=5)

# Load data when app starts
load_notes()
load_flashcards()

# Start the Tkinter main loop
root.mainloop()

# Close the DB connection when done
conn.close()
