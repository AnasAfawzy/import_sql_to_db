import zipfile
import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox


def import_sql_file(db_name, db_user, db_password, sql_zip_path):
    sql_file = None

    # Step 1: Unzip the .zip file if needed
    if sql_zip_path.endswith(".zip"):
        with zipfile.ZipFile(sql_zip_path, "r") as zip_ref:
            # Extract all contents of the zip file to the current directory
            zip_ref.extractall()
            # Find the .sql file in the extracted contents
            extracted_files = zip_ref.namelist()
            sql_file = next(
                (file for file in extracted_files if file.endswith(".sql")), None
            )
            if sql_file is None:
                raise ValueError("No .sql file found in the ZIP archive.")
    else:
        sql_file = sql_zip_path

    # Step 2: Construct the MySQL command to import the SQL file
    mysql_command = ["mysql", "--user=" + db_user, "--password=" + db_password, db_name]

    # Step 3: Use subprocess to run the MySQL import command
    try:
        with open(sql_file, "r") as sql_file_handle:
            subprocess.run(mysql_command, stdin=sql_file_handle, check=True)
        messagebox.showinfo(
            "Success", f"Successfully imported {sql_file} into the database {db_name}"
        )

    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error occurred while importing SQL file: {e}")
    except FileNotFoundError:
        messagebox.showerror(
            "Error",
            "MySQL command not found. Ensure MySQL is installed and added to PATH.",
        )
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

    finally:
        # Step 4: Delete the SQL file after successful import, or cleanup on failure
        if sql_file and os.path.exists(sql_file):
            os.remove(sql_file)
            print(f"Deleted {sql_file} after import.")


# Function to open a file dialog and let the user select a .zip file
def select_file():
    file_path = filedialog.askopenfilename(
        title="Select SQL .zip file", filetypes=[("ZIP files", "*.zip")]
    )
    if file_path:
        entry_sql_file.delete(0, tk.END)
        entry_sql_file.insert(0, file_path)


# Function to start the import process
def start_import():
    db_name = entry_db_name.get()
    db_user = entry_db_user.get()
    db_password = entry_db_password.get()
    sql_zip_path = entry_sql_file.get()

    if not (db_name and sql_zip_path):
        messagebox.showerror("Error", "Please fill in all required fields!")
    else:
        import_sql_file(db_name, db_user, db_password, sql_zip_path)


# Tkinter GUI setup
root = tk.Tk()
root.title("SQL Import Tool")

# Labels and entries for database credentials
tk.Label(root, text="Database Name:").grid(
    row=0, column=0, padx=10, pady=5, sticky=tk.W
)
entry_db_name = tk.Entry(root, width=40)
entry_db_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Database User:").grid(
    row=1, column=0, padx=10, pady=5, sticky=tk.W
)
entry_db_user = tk.Entry(root, width=40)
entry_db_user.grid(row=1, column=1, padx=10, pady=5)
entry_db_user.insert(0, "root")  # Default user is root

tk.Label(root, text="Database Password:").grid(
    row=2, column=0, padx=10, pady=5, sticky=tk.W
)
entry_db_password = tk.Entry(root, width=40, show="*")
entry_db_password.grid(row=2, column=1, padx=10, pady=5)
entry_db_password.insert(0, "")  # Default password is empty

# Label and entry for SQL zip file selection
tk.Label(root, text="SQL .zip File:").grid(
    row=3, column=0, padx=10, pady=5, sticky=tk.W
)
entry_sql_file = tk.Entry(root, width=40)
entry_sql_file.grid(row=3, column=1, padx=10, pady=5)

# Browse button for file selection
btn_browse = tk.Button(root, text="Browse", command=select_file)
btn_browse.grid(row=3, column=2, padx=10, pady=5)

# Start import button
btn_import = tk.Button(root, text="Start Import", command=start_import)
btn_import.grid(row=4, column=1, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
