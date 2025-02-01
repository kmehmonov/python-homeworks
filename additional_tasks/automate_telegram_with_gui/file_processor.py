import os
import zipfile
from PIL import Image
import fitz  # PyMuPDF
import subprocess
from config import SCREENSHOTS_FOLDER

class FileProcessor:
    def __init__(self):
        os.makedirs(SCREENSHOTS_FOLDER, exist_ok=True)

    def get_first_page_image(self, file_path):
        ext = os.path.splitext(file_path)[1].lower()
        screenshot_path = os.path.join(SCREENSHOTS_FOLDER, f"{os.path.basename(file_path)}.jpg")

        try:
            if ext == '.pdf':
                self._convert_pdf(file_path, screenshot_path)
            elif ext == '.djvu':
                self._convert_djvu(file_path, screenshot_path)
            elif ext == '.epub':
                self._convert_epub(file_path, screenshot_path)
            return screenshot_path
        except Exception as e:
            print(f"Error generating screenshot: {e}")
            return None

    def _convert_pdf(self, file_path, output_path):
        doc = fitz.open(file_path)
        page = doc.load_page(0)
        pix = page.get_pixmap()
        pix.save(output_path)

    def _convert_djvu(self, file_path, output_path):
        subprocess.run(['ddjvu', '-format=jpg', '-page=1', file_path, output_path], check=True)

    def _convert_epub(self, file_path, output_path):
        # Requires additional implementation for EPUB conversion
        # This is a placeholder example
        img = Image.new('RGB', (800, 600), color='white')
        img.save(output_path)

    def compress_file(self, file_path):
        zip_path = f"{file_path}.zip"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_path, os.path.basename(file_path))
        return zip_path
