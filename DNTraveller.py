import tkinter as tk
from tkinter import ttk
import win32gui
import win32con
import pyautogui
import time
import random
import pyperclip
import threading
import pygetwindow as gw

class AutoTravelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Travel App")
        
        self.start_button = ttk.Button(root, text="Démarrer", command=self.start_automation)
        self.start_button.pack(pady=10)
        
        self.stop_button = ttk.Button(root, text="Arrêter", command=self.stop_automation, state=tk.DISABLED)
        self.stop_button.pack(pady=5)
        
        self.is_running = False
        self.target_window = None
        self.automation_thread = None

    def bring_window_to_front(self, window):
        window.activate()

    def paste_text(self, text):
        pyautogui.press('space')
        time.sleep(0.1)
        pyautogui.write(text)
        pyautogui.press('enter')
        time.sleep(0.1)
        delay = random.uniform(0.3, 0.8)
        time.sleep(delay)
        pyautogui.press('enter')

    def automate_window_actions(self):
        clipboard_content = ""

        while self.is_running:
            new_clipboard_content = pyperclip.paste()
            if new_clipboard_content != clipboard_content and "/travel" in new_clipboard_content:
                clipboard_content = new_clipboard_content
                lines = new_clipboard_content.split("\n")
                for line in lines:
                    if line.startswith("/travel"):
                        coords = line.replace("/travel", "").strip()
                        print(f"Nouvelles coordonnées détectées : {coords}")
                        self.bring_window_to_front(self.target_window)
                        self.paste_text("/travel " + coords)

            time.sleep(1)

    def start_automation(self):
        self.target_window = gw.getWindowsWithTitle("Dofus")[0]  # Assuming the first window with "Dofus" in the title
        if self.target_window:
            self.is_running = True
            self.automation_thread = threading.Thread(target=self.automate_window_actions)
            self.automation_thread.start()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
        else:
            print("Fenêtre Dofus introuvable.")

    def stop_automation(self):
        self.is_running = False
        self.automation_thread.join()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoTravelApp(root)
    root.mainloop()
