import csv
import os
from config import CSV_NAME, SENT_FOLDER, FAILED_FOLDER
from datetime import datetime

class DatabaseManager:
    def __init__(self):
        self._init_folders()
        self._init_csv()

    def _init_folders(self):
        os.makedirs(SENT_FOLDER, exist_ok=True)
        os.makedirs(FAILED_FOLDER, exist_ok=True)

    def _init_csv(self):
        if not os.path.exists(CSV_NAME):
            with open(CSV_NAME, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    'book_id', 'name', 'status', 'compressed', 
                    'original_size', 'final_size', 'timestamp', 'error'
                ])

    def add_record(self, book_data):
        with open(CSV_NAME, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                book_data['book_id'],
                book_data['name'],
                book_data['status'],
                book_data.get('compressed', False),
                book_data.get('original_size'),
                book_data.get('final_size'),
                datetime.now().isoformat(),
                book_data.get('error', '')
            ])

    def move_file(self, source_path, success):
        dest_folder = SENT_FOLDER if success else FAILED_FOLDER
        os.makedirs(dest_folder, exist_ok=True)
        dest_path = os.path.join(dest_folder, os.path.basename(source_path))
        os.rename(source_path, dest_path)
        return dest_path
