from connection_music import get_connection
import tkinter as tk
from tkinter import messagebox

def insert_music(song_title,artist,genre,release_year):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO music (song_title,artist,genre,release_year) VALUES (%s,%s,%s,%s)"
        values = (song_title,artist,genre,release_year)
        cursor.execute(sql,values)
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Exception as e:
        print("Error:",e)
        return False



def fetch_music():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = "SELECT id,song_title,artist,genre,release_year FROM music"
        cursor.execute(sql)
        music = cursor.fetchall()
        cursor.close()
        connection.close()
        return music
    except Exception as e:
        print("Error during fetch request",e)
        return []
    

def submit_music():
    title = title_entry.get()
    artist = artist_entry.get()
    genre = genre_entry.get()
    release_year = release_year_entry.get()

    if not (title and artist and genre and release_year):
        messagebox.showwarning("Error", "Fill all fields")
        return
    try:
        year = int(release_year)
    except ValueError:
        messagebox.showerror("Error","Release year must be a number.")
        return

    if insert_music(title,artist,genre,year):
        messagebox.showinfo("Success","Music inserted succesfully")
        title_entry.delete(0,tk.END)
        artist_entry.delete(0,tk.END)
        genre_entry.delete(0,tk.END)
        release_year_entry.delete(0,tk.END)
    else:
        messagebox.showerror("Failure","Insertin music failure")

def view_music():
    music = fetch_music()
    text_display.delete("1.0",tk.END)
    if not music:
        text_display.insert(tk.END, "No music inserted")
    else:
        for song in music:
            text_display.insert(tk.END,f" song title: {song[1]}\n artist: {song[2]}\n genre: {song[3]} \n release year: {song[4]}")

root = tk.Tk()
root.title("Music Entry")
root.geometry("600x600")

tk.Label(root,text = "Song Title: ").pack(pady=6)
title_entry = tk.Entry(root,width=60)
title_entry.pack()

tk.Label(root,text = "Artist: ").pack(pady=6)
artist_entry = tk.Entry(root,width=60)
artist_entry.pack()

tk.Label(root,text="Genre: ").pack(pady=6)
genre_entry = tk.Entry(root,width=60)
genre_entry.pack()

tk.Label(root,text="Release Date: ").pack(pady=6)
release_year_entry = tk.Entry(root,width=60)
release_year_entry.pack()

submit_button = tk.Button(root,text = "Insert",command = submit_music)
submit_button.pack(pady=20)##########################################################

view_button = tk.Button(root,text = "Music Preview", command = view_music)
view_button.pack(pady=20)

text_display = tk.Text(root,height=15,width=60)
text_display.pack(pady=10)

root.mainloop()
