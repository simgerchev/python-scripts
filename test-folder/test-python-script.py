
import csv
from prettytable import PrettyTable

def create_table():
    table = PrettyTable()

    # Get column names
    columns = input("Enter column names separated by commas: ").strip().split(",")
    columns = [col.strip() for col in columns]  # Remove extra spaces
    table.field_names = columns  

    # Collect table rows
    rows = []
    while True:
        values = input(f"Enter {len(columns)} values separated by commas (or type 'done' to finish): ").strip()
        
        if values.lower() == "done":
            break
        
        row = values.split(",")
        row = [val.strip() for val in row]  # Remove spaces

        if len(row) == len(columns):  # Ensure correct number of values
            table.add_row(row)
            rows.append(row)
        else:
            print(f"⚠️ Error: Expected {len(columns)} values, but got {len(row)}. Try again.")

    # Show table in terminal
    print("\nGenerated Table:")
    print(table)

    # Save table
    filename = input("Enter filename to save (without extension): ").strip()
    save_as_csv(filename, columns, rows)
    save_as_text(filename, table)

# Save table as CSV
def save_as_csv(filename, columns, rows):
    csv_filename = filename + ".csv"
    with open(csv_filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(rows)
    print(f"✅ Table saved as {csv_filename}!")

# Save table as formatted text file
def save_as_text(filename, table):
    txt_filename = filename + ".txt"
    with open(txt_filename, "w") as file:
        file.write(str(table))
    print(f"✅ Formatted table saved as {txt_filename}!")

if __name__ == "__main__":
    create_table()
