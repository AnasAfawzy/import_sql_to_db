# SQL Import Tool

This is a Python-based GUI tool for importing SQL files (from a .zip archive or directly) into a MySQL database. Built with Tkinter, this tool simplifies the process of extracting and importing SQL files into a specified database.

## Features

- Extracts `.sql` files from `.zip` archives.
- Imports `.sql` files into MySQL databases.
- Simple GUI for database credentials and file selection.
- Deletes the `.sql` file after successful import to ensure cleanup.

## Prerequisites

### System Requirements

- Python 3.6 or higher
- MySQL installed and added to the system's PATH

### Python Packages

- `tkinter` (comes pre-installed with Python)
- `zipfile` (comes pre-installed with Python)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/sql-import-tool.git
cd sql-import-tool
```

2. Ensure Python and MySQL are properly installed on your system.

## Usage

1. Run the script:

```bash
python sql_import_tool.py
```

2. Use the GUI to:
   - Enter the database name, user, and password.
   - Select a `.zip` file containing a `.sql` file.
   - Start the import process.

## How It Works

1. **Unzipping SQL File:** If a `.zip` file is selected, it will extract the `.sql` file from it.
2. **MySQL Import:** The script runs the `mysql` command with the provided database credentials to import the SQL file.
3. **Cleanup:** Deletes the extracted `.sql` file after the import is complete.

## Example

1. Open the GUI and input the following:
   - **Database Name:** `example_db`
   - **Database User:** `root`
   - **Database Password:** (leave blank for default)
   - **SQL .zip File:** Select the `.zip` file containing your SQL dump.
2. Click **Start Import**. The SQL file will be extracted, imported, and then deleted.

## Error Handling

Alerts are displayed for:

- Missing required fields.
- Missing MySQL installation.
- Errors during the import process.

## Contribution

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature-branch
```

3. Commit your changes:

```bash
git commit -m 'Add feature'
```

4. Push to the branch:

```bash
git push origin feature-branch
```

5. Create a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Python
- Tkinter Documentation
- MySQL

Feel free to contact me at `anas.a.fawzy@gmail.com` for any questions or feedback.
