# CodeAlpha_TaskAutomationWithPythonScript
Three Python automation scripts for common repetitive tasks: organizing JPG files by moving them to dedicated folders, extracting email addresses from text files using regex patterns, and scraping webpage titles with timestamps. Features an interactive menu, error handling, and progress feedback for efficient task automation.
# Task Automation Scripts

## Description (300 characters)

Three Python automation scripts for common repetitive tasks: organizing JPG files by moving them to dedicated folders, extracting email addresses from text files using regex patterns, and scraping webpage titles with timestamps. Features an interactive menu, error handling, and progress feedback for efficient task automation.

---

## Overview

This project contains three practical automation scripts designed to handle repetitive tasks efficiently. Each script demonstrates essential Python libraries and techniques for file handling, text processing, and web scraping.

## Scripts Included

### 1. **JPG File Organizer**
Automatically moves all `.jpg` and `.jpeg` files from a source folder to a destination folder.

**Use Case**: Organizing photos, cleaning up downloads folder, sorting image files.

### 2. **Email Extractor**
Extracts all email addresses from text files using regex patterns and saves unique emails to an output file.

**Use Case**: Processing contact lists, extracting emails from documents, data collection.

### 3. **Webpage Title Scraper**
Fetches webpage titles via HTTP requests and saves them with timestamps to a log file.

**Use Case**: Monitoring webpage changes, collecting research data, tracking website titles.

---

## Features

- **Interactive Menu**: Easy-to-use interface for selecting and running scripts
- **Error Handling**: Graceful handling of missing files, network errors, and invalid inputs
- **Progress Feedback**: Real-time updates on operations being performed
- **Duplicate Removal**: Email extractor removes duplicate entries automatically
- **Timestamp Logging**: Webpage scraper includes date/time stamps
- **Case-Insensitive**: JPG organizer handles both `.jpg` and `.jpeg` extensions

---

## Requirements

### Python Version
- Python 3.x

### Built-in Libraries (No installation needed)
- `os` - File and directory operations
- `shutil` - High-level file operations
- `re` - Regular expressions for pattern matching

### External Libraries (Requires installation)
- `requests` - HTTP library for web scraping

---

## Installation

1. **Clone or download this repository**
```bash
git clone <repository-url>
cd task-automation-scripts
```

2. **Install required packages**
```bash
pip install requests
```

---

## Usage

### Running the Interactive Menu

```bash
python automation_scripts.py
```

Follow the on-screen prompts to select and run any script.

### Script 1: Move JPG Files

**Interactive Mode:**
```
1. Select option 1 from menu
2. Enter source folder path (e.g., ./downloads)
3. Enter destination folder path (e.g., ./images)
```

**Direct Function Call:**
```python
move_jpg_files("./source_folder", "./destination_folder")
```

**Example:**
```python
move_jpg_files("C:/Users/YourName/Downloads", "C:/Users/YourName/Pictures/JPG_Files")
```

### Script 2: Extract Email Addresses

**Interactive Mode:**
```
1. Select option 2 from menu
2. Enter input file path (e.g., contacts.txt)
3. Enter output file path (default: emails.txt)
```

**Direct Function Call:**
```python
extract_emails("input.txt", "output.txt")
```

**Sample Input File (sample.txt):**
```
Contact John at john.doe@example.com for details.
You can also reach support@company.org or 
admin@website.net for assistance.
Call us at 123-456-7890 or email info@business.com
```

**Output File (emails.txt):**
```
admin@website.net
info@business.com
john.doe@example.com
support@company.org
```

### Script 3: Scrape Webpage Title

**Interactive Mode:**
```
1. Select option 3 from menu
2. Enter webpage URL (e.g., https://www.python.org)
3. Enter output file path (default: webpage_titles.txt)
```

**Direct Function Call:**
```python
scrape_webpage_title("https://www.example.com", "titles.txt")
```

**Sample Output (webpage_titles.txt):**
```
[2024-12-30 14:23:45] https://www.python.org
Title: Welcome to Python.org
----------------------------------------------------------------------

[2024-12-30 14:25:12] https://github.com
Title: GitHub: Let's build from here
----------------------------------------------------------------------
```

---

## Key Concepts Demonstrated

### File Operations
- Creating directories with `os.makedirs()`
- Checking file/folder existence with `os.path.exists()`
- Listing directory contents with `os.listdir()`
- Moving files with `shutil.move()`

### Regular Expressions
- Email pattern matching with `re.findall()`
- HTML title extraction with `re.search()`
- Case-insensitive matching

### Web Scraping
- HTTP GET requests with `requests.get()`
- Handling timeouts and exceptions
- Extracting data from HTML

### File Handling
- Reading files with `open()` and context managers
- Writing to files with proper encoding
- Appending data to existing files

### Error Handling
- Try-except blocks for robust error management
- User-friendly error messages
- Input validation

---

## Example Workflows

### Workflow 1: Organizing Photos
```
1. Download photos to a folder
2. Run Script 1 to move all JPGs to organized folder
3. Clean folder structure automatically
```

### Workflow 2: Building Email List
```
1. Collect text documents with contact information
2. Run Script 2 on each file
3. Consolidate all extracted emails into one file
```

### Workflow 3: Website Monitoring
```
1. Create list of URLs to monitor
2. Run Script 3 periodically (daily/weekly)
3. Track title changes over time
```

---

## Customization Ideas

### JPG File Organizer
- Extend to handle other image formats (`.png`, `.gif`, `.bmp`)
- Add date-based folder organization (year/month/day)
- Implement file size filtering
- Add option to copy instead of move

### Email Extractor
- Extract phone numbers and URLs
- Add validation for email formats
- Generate CSV output with additional metadata
- Process multiple files at once

### Webpage Title Scraper
- Scrape multiple URLs from a list
- Extract additional metadata (description, keywords)
- Add scheduling for automated monitoring
- Export to CSV or JSON format

---

## Troubleshooting

### Common Issues

**Issue**: Script 1 - "Source folder does not exist"
- **Solution**: Verify the folder path is correct and uses prope
