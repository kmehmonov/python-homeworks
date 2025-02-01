import os
import glob
from config import SUPPORTED_TYPES, MAX_FILE_SIZE
from telegram_api import TelegramBot
from file_processor import FileProcessor
from database import DatabaseManager
from gui import BookBotGUI

class BookBot:
    def __init__(self, token, channel_id):
        self.bot = TelegramBot(token, channel_id)
        self.file_processor = FileProcessor()
        self.db = DatabaseManager()

    def process_books(self, params):
        folder_path = params['folder_path']
        file_type = params['file_type']
        size_handling = params['size_handling']

        pattern = os.path.join(folder_path, f"*{file_type}")
        for book_path in glob.glob(pattern):
            book_data = {
                'book_id': os.path.basename(book_path),
                'name': os.path.basename(book_path),
                'original_size': os.path.getsize(book_path)
            }

            try:
                # Handle large files
                if book_data['original_size'] > MAX_FILE_SIZE:
                    if size_handling == 'skip':
                        raise Exception("File too large - skipping")
                    book_path = self.file_processor.compress_file(book_path)
                    book_data['compressed'] = True
                    book_data['final_size'] = os.path.getsize(book_path)

                # Generate and send screenshot
                screenshot_path = self.file_processor.get_first_page_image(book_path)
                photo_response = self.bot.send_photo(screenshot_path)
                
                if not photo_response.get('ok'):
                    raise Exception(f"Photo send failed: {photo_response.get('error')}")

                # Send document
                doc_response = self.bot.send_document(
                    book_path,
                    reply_to_message_id=photo_response['result']['message_id']
                )

                if not doc_response.get('ok'):
                    raise Exception(f"Document send failed: {doc_response.get('error')}")

                # Update database and move file
                book_data['status'] = 'success'
                self.db.move_file(book_path, True)

            except Exception as e:
                book_data['status'] = 'failed'
                book_data['error'] = str(e)
                self.db.move_file(book_path, False)

            finally:
                self.db.add_record(book_data)

if __name__ == "__main__":
    # Get these from environment variables or user input
    TOKEN = "YOUR_BOT_TOKEN"
    CHANNEL_ID = "@YOUR_CHANNEL"

    bot = BookBot(TOKEN, CHANNEL_ID)
    gui = BookBotGUI(bot.process_books)
    gui.run()
