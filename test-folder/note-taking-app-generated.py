
import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect("notes.db")
cursor = conn.cursor()

# Create tables if they do not exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS folders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        folder_id INTEGER,
        name TEXT,
        FOREIGN KEY (folder_id) REFERENCES folders(id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS subcategories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER,
        name TEXT,
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subcategory_id INTEGER,
        title TEXT,
        content TEXT,
        FOREIGN KEY (subcategory_id) REFERENCES subcategories(id)
    )
""")

conn.commit()

# Function to create a folder
def create_folder():
    folder_name = input("Enter folder name: ").strip()
    try:
        cursor.execute("INSERT INTO folders (name) VALUES (?)", (folder_name,))
        conn.commit()
        print(f"Folder '{folder_name}' created successfully!")
    except sqlite3.IntegrityError:
        print("Folder already exists!")

# Function to create a category inside a folder
def create_category():
    cursor.execute("SELECT * FROM folders")
    folders = cursor.fetchall()
    if not folders:
        print("No folders found. Create a folder first.")
        return
    
    print("Folders:")
    for idx, folder in enumerate(folders, 1):
        print(f"{idx}. {folder[1]}")
    
    folder_choice = int(input("Select a folder (Enter number): ")) - 1
    folder_id = folders[folder_choice][0]

    category_name = input("Enter category name: ").strip()
    cursor.execute("INSERT INTO categories (folder_id, name) VALUES (?, ?)", (folder_id, category_name))
    conn.commit()
    print(f"Category '{category_name}' added!")

# Function to create a subcategory inside a category
def create_subcategory():
    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()
    if not categories:
        print("No categories found. Create a category first.")
        return

    print("Categories:")
    for idx, category in enumerate(categories, 1):
        print(f"{idx}. {category[2]}")
    
    category_choice = int(input("Select a category (Enter number): ")) - 1
    category_id = categories[category_choice][0]

    subcategory_name = input("Enter subcategory name: ").strip()
    cursor.execute("INSERT INTO subcategories (category_id, name) VALUES (?, ?)", (category_id, subcategory_name))
    conn.commit()
    print(f"Subcategory '{subcategory_name}' added!")

# Function to add a note inside a subcategory
def add_note():
    cursor.execute("SELECT * FROM subcategories")
    subcategories = cursor.fetchall()
    if not subcategories:
        print("No subcategories found. Create a subcategory first.")
        return

    print("Subcategories:")
    for idx, subcategory in enumerate(subcategories, 1):
        print(f"{idx}. {subcategory[2]}")
    
    subcategory_choice = int(input("Select a subcategory (Enter number): ")) - 1
    subcategory_id = subcategories[subcategory_choice][0]

    note_title = input("Enter note title: ").strip()
    note_content = input("Enter note content: ").strip()
    cursor.execute("INSERT INTO notes (subcategory_id, title, content) VALUES (?, ?, ?)", 
                   (subcategory_id, note_title, note_content))
    conn.commit()
    print(f"Note '{note_title}' saved!")

# Function to view notes in a subcategory
def view_notes():
    cursor.execute("SELECT * FROM subcategories")
    subcategories = cursor.fetchall()
    if not subcategories:
        print("No subcategories found.")
        return

    print("Subcategories:")
    for idx, subcategory in enumerate(subcategories, 1):
        print(f"{idx}. {subcategory[2]}")

    subcategory_choice = int(input("Select a subcategory (Enter number): ")) - 1
    subcategory_id = subcategories[subcategory_choice][0]

    cursor.execute("SELECT * FROM notes WHERE subcategory_id = ?", (subcategory_id,))
    notes = cursor.fetchall()
    
    if not notes:
        print("No notes found in this subcategory.")
        return

    print("\nNotes:")
    for idx, note in enumerate(notes, 1):
        print(f"{idx}. {note[2]}")  # Display note title

    note_choice = input("\nEnter the note number to view or press Enter to exit: ").strip()
    if note_choice.isdigit():
        note_choice = int(note_choice) - 1
        if 0 <= note_choice < len(notes):
            print(f"\n--- {notes[note_choice][2]} ---")
            print(notes[note_choice][3])
        else:
            print("Invalid choice.")

# Function to delete a note
def delete_note():
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    if not notes:
        print("No notes found.")
        return

    print("Notes:")
    for idx, note in enumerate(notes, 1):
        print(f"{idx}. {note[2]}")  # Show note title
    
    note_choice = int(input("Select a note to delete (Enter number): ")) - 1
    note_id = notes[note_choice][0]

    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    print("Note deleted successfully.")

# Function to display the menu
def menu():
    while True:
        print("\n===== Note-Taking App =====")
        print("1. Create Folder")
        print("2. Create Category")
        print("3. Create Subcategory")
        print("4. Add Note")
        print("5. View Notes")
        print("6. Delete Note")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_folder()
        elif choice == "2":
            create_category()
        elif choice == "3":
            create_subcategory()
        elif choice == "4":
            add_note()
        elif choice == "5":
            view_notes()
        elif choice == "6":
            delete_note()
        elif choice == "7":
            print("Exiting the program.")
            conn.close()
            break
        else:
            print("Invalid option. Try again.")

menu()
