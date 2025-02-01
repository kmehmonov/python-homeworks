import os

SUPPORTED_TYPES = ['.pdf', '.epub']
MAX_FILE_SIZE = 50 * 1024 * 1024
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SENT_FOLDER = os.path.join(BASE_DIR, 'sent_books')
FAILED_FOLDER = os.path.join(BASE_DIR, 'failed_books')
SCREENSHOTS_FOLDER = os.path.join(BASE_DIR, 'screenshots')

CSV_NAME = 'books_db.csv'

BOT_TOKEN = os.getenv("MY_BOT_TOKEN")
CHANNEL_ID = "-1001821144204"