# Basic setup for gui
import tkinter as tk

def on_submit(): # Button clicked function.
    name = name_entry.get()
    job_query = job_entry.get()
    if name and job_query:
        output_label.config(text=f"Hi {name}!, Searching for {job_query} role data.")
    else:
        output_label.config(text="Please fill both fields above.")

root = tk.Tk()
root.title("skill_scraper")
root.geometry("500x500")
