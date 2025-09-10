import sys
import time
import logging
import pyperclip
import pyautogui
import tkinter as tk
from threading import Thread
from time import sleep

# Platform-specific imports
IS_WINDOWS = sys.platform.startswith('win')
IS_MAC = sys.platform.startswith('darwin')

if IS_WINDOWS:
    import win32clipboard
    import win32con
elif IS_MAC:
    from AppKit import NSPasteboard, NSFilenamesPboardType

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

last_clipboard = pyperclip.paste()
last_files = []
last_notification_time = 0
notification_delay = 1.5

def get_clipboard_files():
    try:
        if IS_WINDOWS:
            win32clipboard.OpenClipboard()
            try:
                if win32clipboard.IsClipboardFormatAvailable(win32con.CF_HDROP):
                    files = win32clipboard.GetClipboardData(win32con.CF_HDROP)
                    return [str(f) for f in files]
            finally:
                win32clipboard.CloseClipboard()

        elif IS_MAC:
            pb = NSPasteboard.generalPasteboard()
            types = pb.types()
            if NSFilenamesPboardType in types:
                return list(pb.propertyListForType_(NSFilenamesPboardType))

    except Exception as e:
        logging.error(f"Clipboard file detection error: {e}")
    return None

def create_flash_window(text, x, y):
    """Show fading text box at (x, y) near cursor"""
    if len(text) > 50:
        text = text[:47] + '...'

    def run_window():
        window = tk.Tk()
        window.overrideredirect(True)
        window.attributes('-topmost', True)
        try:
            window.attributes('-alpha', 0.9)
        except:
            pass  # macOS fallback

        label = tk.Label(window, text=text, font=('Arial', 12), fg='white', bg='black', wraplength=300)
        label.pack()

        screen_w, screen_h = pyautogui.size()
        x_pos = min(x + 10, screen_w - 320)
        y_pos = min(y + 10, screen_h - 80)
        window.geometry(f'+{x_pos}+{y_pos}')

        def fade_out(opacity):
            if opacity <= 0:
                window.destroy()
            else:
                try:
                    window.attributes('-alpha', opacity)
                except:
                    pass
                window.after(75, fade_out, opacity - 0.1)

        window.after(100, fade_out, 1.0)
        window.mainloop()

    Thread(target=run_window, daemon=True).start()

def main():
    global last_clipboard, last_files, last_notification_time
    logging.info("Clipboard monitor started...")

    while True:
        current_time = time.time()
        if current_time - last_notification_time < notification_delay:
            sleep(0.2)
            continue

        # Detect text copy
        try:
            current_clipboard = pyperclip.paste()
        except Exception as e:
            logging.error(f"Clipboard text error: {e}")
            current_clipboard = last_clipboard

        if current_clipboard != last_clipboard and current_clipboard.strip():
            x, y = pyautogui.position()
            create_flash_window(current_clipboard, x, y)
            last_clipboard = current_clipboard
            last_notification_time = current_time
            logging.info(f"Text copied: {current_clipboard[:50]}")

        # Detect file copy
        copied_files = get_clipboard_files()
        if copied_files and copied_files != last_files:
            x, y = pyautogui.position()
            preview = copied_files[0]
            if len(copied_files) > 1:
                preview += f" (+{len(copied_files) - 1} more)"
            create_flash_window(preview, x, y)
            last_files = copied_files
            last_notification_time = current_time
            logging.info(f"Files copied: {preview}")

        sleep(0.2)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Script terminated by user")
