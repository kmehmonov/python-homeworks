import os
import glob
from config import MAX_FILE_SIZE, BOT_TOKEN, CHANNEL_ID
from telegram_api import TelegramBot
from file_processor import FileProcessor
from database import DatabaseManager
from gui import BookBotGUI

class BookBot:
    def __init__(self, token, channel_id):
        self.bot = TelegramBot(token, channel_id)
        self.file_processor = FileProcessor()
        self.db = DatabaseManager()
        self.current_file = ""
        self.progress_value = 0
        self.total_files = 0

    def process_books(self, params, gui_update_callback):
        folder_path = params['folder_path']
        file_type = params['file_type']

        pattern = os.path.join(folder_path, f"*{file_type}")
        all_files = glob.glob(pattern)
        new_files = [f for f in all_files if not self.db.is_file_processed(os.path.basename(f))]
        
        self.total_files = len(new_files)
        self.progress_value = 0
        
        for idx, book_path in enumerate(new_files):
            self.current_file = os.path.basename(book_path)
            self.progress_value = idx + 1
            gui_update_callback(self._get_progress_info())
            
            book_data = {
                'book_id': self.current_file,
                'name': self.current_file,
                'file_size': os.path.getsize(book_path)
            }

            try:
                # Check file size
                if book_data['file_size'] > MAX_FILE_SIZE:
                    raise Exception("File too large - skipping")

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

                # Update database and copy file to archive
                book_data['status'] = 'success'
                self.db.copy_file_to_archive(book_path, success=True)

            except Exception as e:
                book_data['status'] = 'failed'
                book_data['error'] = str(e)
                self.db.copy_file_to_archive(book_path, success=False)

            finally:
                self.db.add_record(book_data)

        gui_update_callback({'current_file': "Process completed!", 'progress': 100})

    def _get_progress_info(self):
        return {
            'current_file': f"Processing: {self.current_file}",
            'progress': (self.progress_value / self.total_files) * 100 if self.total_files > 0 else 0
        }

if __name__ == "__main__":
    # Get these from environment variables or user input
    TOKEN = BOT_TOKEN
    CHANNEL_ID = CHANNEL_ID

    bot = BookBot(TOKEN, CHANNEL_ID)
    gui = BookBotGUI(bot.process_books)
    gui.run()