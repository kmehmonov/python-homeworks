import os

SUPPORTED_TYPES = ['.pdf', '.epub', '.djvu']
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB in bytes
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Folders
SENT_FOLDER = os.path.join(BASE_DIR, 'sent_books')
FAILED_FOLDER = os.path.join(BASE_DIR, 'failed_books')
SCREENSHOTS_FOLDER = os.path.join(BASE_DIR, 'screenshots')

# Database
CSV_NAME = 'books_db.csv'
