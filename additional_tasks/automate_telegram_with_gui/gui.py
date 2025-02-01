import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from config import SUPPORTED_TYPES

class BookBotGUI:
    def __init__(self, process_callback):
        self.root = tk.Tk()
        self.root.title("Telegram Book Bot")
        self.process_callback = process_callback

        self.folder_path = tk.StringVar()
        self.selected_type = tk.StringVar(value=SUPPORTED_TYPES[0])
        self.size_handling = tk.StringVar(value='compress')

        self._create_widgets()

    def _create_widgets(self):
        # Folder selection
        ttk.Label(self.root, text="Select Books Folder:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(self.root, textvariable=self.folder_path, width=40).grid(row=0, column=1, padx=5)
        ttk.Button(self.root, text="Browse", command=self._browse_folder).grid(row=0, column=2)

        # File type selection
        ttk.Label(self.root, text="Book Type:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Combobox(self.root, textvariable=self.selected_type, values=SUPPORTED_TYPES).grid(row=1, column=1)

        # Size handling
        ttk.Label(self.root, text="Large File Handling:").grid(row=2, column=0, padx=5, pady=5)
        ttk.Radiobutton(self.root, text="Compress and Send", variable=self.size_handling, value='compress').grid(row=2, column=1)
        ttk.Radiobutton(self.root, text="Don't Send", variable=self.size_handling, value='skip').grid(row=2, column=2)

        # Buttons
        ttk.Button(self.root, text="Start", command=self._start_process).grid(row=3, column=1, pady=10)
        ttk.Button(self.root, text="Exit", command=self.root.quit).grid(row=3, column=2)

    def _browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)

    def _start_process(self):
        params = {
            'folder_path': self.folder_path.get(),
            'file_type': self.selected_type.get(),
            'size_handling': self.size_handling.get()
        }
        if not params['folder_path']:
            messagebox.showerror("Error", "Please select a folder first!")
            return
        
        self.process_callback(params)
        messagebox.showinfo("Info", "Processing completed!")

    def run(self):
        self.root.mainloop()
