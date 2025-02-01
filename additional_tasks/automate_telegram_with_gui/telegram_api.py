import requests
import os
from config import MAX_FILE_SIZE

class TelegramBot:
    def __init__(self, token, channel_id):
        self.base_url = f"https://api.telegram.org/bot{token}"
        self.channel_id = channel_id

    def _send_request(self, method, files=None, data=None):
        try:
            response = requests.post(f"{self.base_url}/{method}", files=files, data=data)
            return response.json()
        except Exception as e:
            return {'ok': False, 'error': str(e)}

    def send_photo(self, image_path):
        with open(image_path, 'rb') as photo:
            files = {'photo': photo}
            data = {'chat_id': self.channel_id}
            return self._send_request('sendPhoto', files=files, data=data)

    def send_document(self, doc_path, reply_to_message_id=None):
        file_size = os.path.getsize(doc_path)
        if file_size > MAX_FILE_SIZE:
            return {'ok': False, 'error': 'File too large'}

        with open(doc_path, 'rb') as document:
            files = {'document': document}
            data = {'chat_id': self.channel_id, 'reply_to_message_id': reply_to_message_id}
            return self._send_request('sendDocument', files=files, data=data)
