import tkinter as tk
from tkinter import messagebox
import random

class SuitJepang:
    def __init__(self, root):
        self.root = root
        self.root.title("Suit Jepang")
        
        self.player_score = 0
        self.computer_score = 0
        
        self.label = tk.Label(self.root, text="Pilihan: Batu, Kertas, atau Gunting")
        self.label.pack(pady=10)
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()
        
        self.rock_button = tk.Button(self.button_frame, text="Batu", width=10, command=lambda: self.play("Batu"))
        self.rock_button.grid(row=0, column=0, padx=10)
        
        self.paper_button = tk.Button(self.button_frame, text="Kertas", width=10, command=lambda: self.play("Kertas"))
        self.paper_button.grid(row=0, column=1, padx=10)
        
        self.scissors_button = tk.Button(self.button_frame, text="Gunting", width=10, command=lambda: self.play("Gunting"))
        self.scissors_button.grid(row=0, column=2, padx=10)
        
        self.score_label = tk.Label(self.root, text="Skor Kamu: 0  Skor Komputer: 0")
        self.score_label.pack(pady=10)
        
        self.save_button = tk.Button(self.root, text="Simpan Skor", width=15, command=self.save_score)
        self.save_button.pack(pady=10)
        
    def play(self, player_choice):
        computer_choice = random.choice(["Batu", "Kertas", "Gunting"])
        
        result = self.get_result(player_choice, computer_choice)
        self.update_score(result)
        
        message = f"Pilihan Kamu : {player_choice}.\nPilihan Komputer : {computer_choice}.\n{result}"
        messagebox.showinfo("Hasil", message)
        
    def get_result(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "Seri!!"
        
        if (player_choice == "Batu" and computer_choice == "Gunting") or \
           (player_choice == "Kertas" and computer_choice == "Batu") or \
           (player_choice == "Gunting" and computer_choice == "Kertas"):
            return "Kamu menang!!"
        
        return "Komputer menang!!"
    
    def update_score(self, result):
        if result == "Kamu menang!!":
            self.player_score += 1
        elif result == "Komputer menang!!":
            self.computer_score += 1
        
        self.score_label.config(text=f"Player: {self.player_score}  Computer: {self.computer_score}")
    
    def save_score(self):
        try:
            with open("scores.txt", "a") as file:
                file.write(f"Player: {self.player_score}  Computer: {self.computer_score}\n")
            messagebox.showinfo("Success", "Skor tersimpan.")
        except OSError:
            messagebox.showerror("Error", "Gagal untuk menyimpan skor.")
        
root = tk.Tk()
app = SuitJepang(root)
root.mainloop()
