import tkinter as tk
import threading
from tkinter import ttk, filedialog, messagebox
from config import SUPPORTED_TYPES

class BookBotGUI:
    def __init__(self, process_callback):
        self.root = tk.Tk()
        self.root.title("Telegram Book Bot")
        self.process_callback = process_callback

        self.folder_path = tk.StringVar()
        self.selected_type = tk.StringVar(value=SUPPORTED_TYPES[0])
        
        # Progress variables
        self.progress_var = tk.DoubleVar()
        self.status_text = tk.StringVar(value="Ready")

        self._create_widgets()

    def _create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.grid(row=0, column=0, sticky="nsew")

        # Folder selection
        ttk.Label(main_frame, text="Select Books Folder:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(main_frame, textvariable=self.folder_path, width=40).grid(row=0, column=1, padx=5)
        ttk.Button(main_frame, text="Browse", command=self._browse_folder).grid(row=0, column=2)

        # File type selection
        ttk.Label(main_frame, text="Book Type:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Combobox(main_frame, textvariable=self.selected_type, values=SUPPORTED_TYPES).grid(row=1, column=1)

        # Progress bar
        ttk.Label(main_frame, textvariable=self.status_text).grid(row=2, column=0, columnspan=3, pady=5)
        ttk.Progressbar(main_frame, variable=self.progress_var, maximum=100).grid(
            row=3, column=0, columnspan=3, sticky="ew", pady=5
        )

        # Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=4, column=0, columnspan=3, pady=10)
        ttk.Button(btn_frame, text="Start", command=self._start_process).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Exit", command=self.root.quit).pack(side=tk.RIGHT, padx=5)

    def _browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)

    def _start_process(self):
        if not self.folder_path.get():
            messagebox.showerror("Error", "Please select a folder first!")
            return

        params = {
            'folder_path': self.folder_path.get(),
            'file_type': self.selected_type.get()
        }

        processing_thread = threading.Thread(
            target=self._run_processing,
            args=(params,),
            daemon=True
        )
        processing_thread.start()

    def _run_processing(self, params):
        self.root.after(0, self._update_progress, {'current_file': "Starting...", 'progress': 0})
        
        def gui_update_callback(progress_info):
            self.root.after(0, self._update_progress, progress_info)
        
        self.process_callback(params, gui_update_callback)

    def _update_progress(self, progress_info):
        self.status_text.set(progress_info['current_file'])
        self.progress_var.set(progress_info['progress'])
        self.root.update_idletasks()

    def run(self):
        self.root.mainloop()