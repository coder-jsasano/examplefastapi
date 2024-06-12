#non-age-restricted YouTube downloader 
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog, messagebox

def download_video():
    url = url_entry.get()
    save_path = filedialog.askdirectory()
    if not save_path:
        messagebox.showerror("Error", "Please select a directory to save the video.")
        return
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def create_gui():
    root = tk.Tk()
    root.title("YouTube Video Downloader")
    
    tk.Label(root, text="Enter YouTube URL:").pack(pady=10)
    
    global url_entry
    url_entry = tk.Entry(root, width=50)
    url_entry.pack(pady=10)
    
    download_button = tk.Button(root, text="Download", command=download_video)
    download_button.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
