# ============================================================================
# SCRIPT 1: Move All .jpg Files to a New Folder
# ============================================================================

import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    """
    Move all .jpg files from source folder to destination folder
    """
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created destination folder: {destination_folder}")
    
    # Check if source folder exists
    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist!")
        return
    
    # Counter for moved files
    moved_count = 0
    
    # Loop through all files in source folder
    for filename in os.listdir(source_folder):
        # Check if file has .jpg extension (case-insensitive)
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
            # Full path of source and destination
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)
            
            # Move the file
            try:
                shutil.move(source_path, destination_path)
                print(f"Moved: {filename}")
                moved_count += 1
            except Exception as e:
                print(f"Error moving {filename}: {e}")
    
    # Summary
    print(f"\n✓ Successfully moved {moved_count} .jpg file(s)")


# ============================================================================
# SCRIPT 2: Extract Email Addresses from Text File
# ============================================================================

import re

def extract_emails(input_file, output_file):
    """
    Extract all email addresses from a text file and save to another file
    """
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist!")
        return
    
    # Regular expression pattern for email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Read the input file
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Find all email addresses
        emails = re.findall(email_pattern, content)
        
        # Remove duplicates and sort
        unique_emails = sorted(set(emails))
        
        # Write emails to output file
        with open(output_file, 'w', encoding='utf-8') as file:
            for email in unique_emails:
                file.write(email + '\n')
        
        # Summary
        print(f"✓ Found {len(emails)} email(s) ({len(unique_emails)} unique)")
        print(f"✓ Saved to: {output_file}")
        
        # Display found emails
        if unique_emails:
            print("\nExtracted emails:")
            for email in unique_emails:
                print(f"  - {email}")
        
    except Exception as e:
        print(f"Error: {e}")


# ============================================================================
# SCRIPT 3: Scrape Webpage Title and Save to File
# ============================================================================

import requests
from datetime import datetime

def scrape_webpage_title(url, output_file):
    """
    Scrape the title of a webpage and save it to a file
    """
    try:
        # Send GET request to the webpage
        print(f"Fetching: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad status codes
        
        # Extract title using regex
        title_pattern = r'<title>(.*?)</title>'
        match = re.search(title_pattern, response.text, re.IGNORECASE)
        
        if match:
            title = match.group(1).strip()
            
            # Get current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Save to file
            with open(output_file, 'a', encoding='utf-8') as file:
                file.write(f"[{timestamp}] {url}\n")
                file.write(f"Title: {title}\n")
                file.write("-" * 70 + "\n\n")
            
            print(f"✓ Title: {title}")
            print(f"✓ Saved to: {output_file}")
        else:
            print("⚠ No title found on the webpage")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
    except Exception as e:
        print(f"Error: {e}")


# ============================================================================
# MAIN MENU - Run Any Script
# ============================================================================

def main():
    """
    Main menu to choose which automation script to run
    """
    print("=" * 70)
    print("TASK AUTOMATION SCRIPTS")
    print("=" * 70)
    print("\nChoose a script to run:")
    print("1. Move all .jpg files to a new folder")
    print("2. Extract email addresses from a text file")
    print("3. Scrape webpage title and save to file")
    print("4. Exit")
    print()
    
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == "1":
        print("\n--- MOVE JPG FILES ---")
        source = input("Enter source folder path: ").strip()
        destination = input("Enter destination folder path: ").strip()
        move_jpg_files(source, destination)
    
    elif choice == "2":
        print("\n--- EXTRACT EMAIL ADDRESSES ---")
        input_file = input("Enter input text file path: ").strip()
        output_file = input("Enter output file path (default: emails.txt): ").strip()
        if not output_file:
            output_file = "emails.txt"
        extract_emails(input_file, output_file)
    
    elif choice == "3":
        print("\n--- SCRAPE WEBPAGE TITLE ---")
        url = input("Enter webpage URL: ").strip()
        output_file = input("Enter output file path (default: webpage_titles.txt): ").strip()
        if not output_file:
            output_file = "webpage_titles.txt"
        scrape_webpage_title(url, output_file)
    
    elif choice == "4":
        print("Goodbye!")
        return
    
    else:
        print("Invalid choice! Please select 1-4.")


# Run the program
if __name__ == "__main__":
    main()


# ============================================================================
# EXAMPLE USAGE (Uncomment to test individual functions)
# ============================================================================

# Example 1: Move JPG files
# move_jpg_files("./images", "./jpg_images")

# Example 2: Extract emails
# extract_emails("sample_text.txt", "extracted_emails.txt")

# Example 3: Scrape webpage title
# scrape_webpage_title("https://www.python.org", "webpage_titles.txt")