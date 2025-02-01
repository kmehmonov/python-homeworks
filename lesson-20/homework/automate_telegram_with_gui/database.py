import csv
import os
import shutil
from datetime import datetime
from config import CSV_NAME, SENT_FOLDER, FAILED_FOLDER

class DatabaseManager:
    def __init__(self):
        self._init_folders()
        self._init_csv()
        
    def _init_folders(self):
        """Create necessary folders if they don't exist"""
        os.makedirs(SENT_FOLDER, exist_ok=True)
        os.makedirs(FAILED_FOLDER, exist_ok=True)

    def _init_csv(self):
        """Initialize CSV file with headers if it doesn't exist"""
        if not os.path.exists(CSV_NAME):
            with open(CSV_NAME, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([
                    'book_id', 
                    'name', 
                    'status', 
                    'file_size', 
                    'timestamp', 
                    'error'
                ])

    def is_file_processed(self, filename):
        """Check if file has already been successfully processed"""
        if not os.path.exists(CSV_NAME):
            return False
            
        with open(CSV_NAME, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['book_id'] == filename and row['status'] == 'success':
                    return True
        return False

    def add_record(self, book_data):
        """Add new record to CSV database"""
        with open(CSV_NAME, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                book_data['book_id'],
                book_data['name'],
                book_data['status'],
                book_data.get('file_size', ''),
                datetime.now().isoformat(),
                book_data.get('error', '')
            ])

    def copy_file_to_archive(self, source_path, success):
        """
        Copy file to appropriate archive folder after processing
        Returns new path if successful, None otherwise
        """
        try:
            dest_folder = SENT_FOLDER if success else FAILED_FOLDER
            filename = os.path.basename(source_path)
            dest_path = os.path.join(dest_folder, filename)

            # Handle existing files with same name
            counter = 1
            while os.path.exists(dest_path):
                base, ext = os.path.splitext(filename)
                dest_path = os.path.join(dest_folder, f"{base}_{counter}{ext}")
                counter += 1

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(source_path, dest_path)
            return dest_path
        except Exception as e:
            print(f"Error copying file: {e}")
            return None

    def get_processed_files(self):
        """Get list of all processed files from database"""
        processed = []
        if not os.path.exists(CSV_NAME):
            return processed
            
        with open(CSV_NAME, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                processed.append(row)
        return processed

    def clear_database(self):
        """Clear all database records (for testing purposes)"""
        if os.path.exists(CSV_NAME):
            os.remove(CSV_NAME)
        self._init_csv()