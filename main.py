import tkinter as tk
from tkinter import ttk
import random
from nltk.corpus import words

nltk_words = set(words.words())

class WordFinderApp:
    def __init__(self):
        print("Initializing WordFinderApp...")
        self.longest_word = ""
        self.words_found = set()
        self.current_letters = []

        self.root = tk.Tk()
        self.root.geometry("600x400")
        self.root.title("Word Finder")

        self.status_frame = ttk.Frame(self.root)
        self.status_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.longest_word_label = ttk.Label(self.status_frame, text="Longest word found: " + self.longest_word, font=("Arial", 12))
        self.longest_word_label.pack(side=tk.LEFT)

        self.words_found_label = ttk.Label(self.status_frame, text="Words found: " + str(len(self.words_found)), font=("Arial", 12))
        self.words_found_label.pack(side=tk.LEFT, padx=20)

        self.list_frame = ttk.Frame(self.root)
        self.list_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.words_listbox = tk.Listbox(self.list_frame, font=("Arial", 12))
        self.words_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.list_frame, orient=tk.VERTICAL, command=self.words_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.words_listbox.config(yscrollcommand=self.scrollbar.set)

        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        self.pause_button = ttk.Button(self.button_frame, text="Pause", command=self.toggle_pause)
        self.pause_button.pack(side=tk.LEFT)

        self.quit_button = ttk.Button(self.button_frame, text="Quit", command=self.root.quit)
        self.quit_button.pack(side=tk.RIGHT)

        self.paused = False
        print("Wordfinder app initialised, running loop.....")

        self.run_loop()

    def run_loop(self):
        if not self.paused:
            letter = random.choice('abcdefghijklmnopqrstuvwxyz')
            self.current_letters.append(letter)
            if len(self.current_letters) > 25:
                self.current_letters.pop(0)
            for i in range(len(self.current_letters)):
                for j in range(i+1, len(self.current_letters) + 1):
                    current_word = "".join(self.current_letters[i:j])
                    if len(current_word) >= 3:
                        if current_word in nltk_words and current_word not in self.words_found:
                            self.words_listbox.insert(tk.END, current_word)
                            self.words_found.add(current_word)
                            print(f'{current_word} found')
                            if len(current_word) > len(self.longest_word):
                                self.longest_word = current_word
                                self.longest_word_label.config(text="Longest word found: " + self.longest_word)
                self.words_found_label.config(text="Words found: " + str(len(self.words_found)))
        self.root.after(1, self.run_loop)

    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.pause_button.config(text="Resume")
        else:
            self.pause_button.config(text="Pause")

app = WordFinderApp()
app.root.mainloop()