import fitz
import os
import requests


folder_path = r"books_folder"
output_folder = r"folder_for_images"
telegram_bot_token = "token"
chat_id = "chat_id"  


send_photo_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendPhoto"
send_document_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendDocument"


os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(folder_path):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(folder_path, filename)
        
        try:
            pdf_document = fitz.open(pdf_path)
            first_page = pdf_document[0]
            pix = first_page.get_pixmap(dpi=150)
            image_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.png")
            pix.save(image_path)
            print(f"Saved image: {image_path}")

            with open(image_path, "rb") as image_file:
                response = requests.post(send_photo_url, data={"chat_id": chat_id}, files={"photo": image_file})
                if response.status_code == 200:
                    print(f"Image sent successfully: {filename}")
  
                    with open(pdf_path, "rb") as pdf_file:
                        response = requests.post(send_document_url, data={"chat_id": chat_id, "reply_to_message_id": response.json()['result']['message_id']}, files={"document": pdf_file})
                        if response.status_code == 200:
                            print(f"PDF sent successfully: {filename}")
                        else:
                            print(f"Failed to send PDF: {response.text}")
                else:
                    print(f"Failed to send image: {response.text}")
        
        except Exception as e:
            print(f"Error  {filename}: {e}")
