import os
import json
import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox
from tkinter import ttk
import pyperclip

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def get_timezone_data(zip_code):
    # Load the zip code data file
    with open(resource_path('./data/zipcode.json')) as f:
        zipcode_data = json.load(f)

    # Get the timezoneid from the zip code
    timezone_id = None
    for entry in zipcode_data['zipcodes']:
        if entry['zipcode'] == zip_code:
            timezone_id = entry['timezoneid']
            break

    if timezone_id is None:
        return None

    # Load the timezone data file
    with open(resource_path('./data/timezone.json')) as f:
        timezone_data = json.load(f)

    # Find the matching id for TimezoneId from zipcode file
    timezone = None
    for entry in timezone_data['timezones']:
        if entry['id'] == timezone_id:
            timezone = entry
            break

    return timezone

def show_timezone():
    zip_code = entry_zipcode.get()
    timezone = get_timezone_data(zip_code)

    if timezone:
        clear_info()

        # Display each data point
        create_data_row("Zip Code", zip_code)
        create_data_row("Timezone", timezone['timezone'])
        create_data_row("UTC Offset", str(timezone['utc_offset']))
        create_data_row("Has Daylight Saving Time", str(timezone['daylight_saving_time']))

        button_copy_json.config(state='normal')
        button_copy_csv.config(state='normal')
    else:
        messagebox.showerror("Error", "Invalid zip code or timezone data not found.")

def clear_info():
    for widget in info_frame.winfo_children():
        widget.destroy()

def create_data_row(label_text, value_text):
    row_frame = ttk.Frame(info_frame)
    row_frame.pack(fill="x", pady=5)

    label = ttk.Label(row_frame, text=label_text + ":")
    label.config(font=("Arial", 10, "bold"))
    label.pack(side="left")

    textbox_frame = ttk.Frame(row_frame)
    textbox_frame.pack(side="left")

    textbox = tk.Text(textbox_frame, height=1, width=20)
    textbox.insert(tk.END, value_text)
    textbox.config(state=tk.DISABLED)
    textbox.pack(pady=3, padx=3)

    def copy_value():
        value = textbox.get("1.0", tk.END).strip()
        if value:
            pyperclip.copy(value)

    button_copy = ttk.Button(row_frame, image=copy_icon, command=copy_value)
    button_copy.pack(side="left")

def copy_to_json():
    data = {}
    for child in info_frame.winfo_children():
        label = child.winfo_children()[0]
        textbox = child.winfo_children()[1].winfo_children()[0]
        label_text = label['text'].rstrip(':')
        value_text = textbox.get("1.0", tk.END).strip()
        data[label_text] = value_text

    json_data = json.dumps(data, indent=4)
    pyperclip.copy(json_data)
    messagebox.showinfo("Copy Successful", "All data copied to clipboard in JSON format.")

def copy_to_csv():
    labels = []
    values = []
    for child in info_frame.winfo_children():
        label = child.winfo_children()[0]
        textbox = child.winfo_children()[1].winfo_children()[0]
        label_text = label['text'].rstrip(':')
        value_text = textbox.get("1.0", tk.END).strip()
        labels.append(label_text)
        values.append(value_text)

    csv_data = ','.join(labels) + '\n' + ','.join(values)
    pyperclip.copy(csv_data)
    messagebox.showinfo("Copy Successful", "All data copied to clipboard in CSV format.")


# Window Starts here
window = tk.Tk()
window.title("Zip Code to Timezone Lookup")
window.geometry("400x325")
window.eval('tk::PlaceWindow . center')

label_zipcode = ttk.Label(window, text="Enter a zip code:")
label_zipcode.pack()

entry_zipcode = ttk.Entry(window, justify="center")  # Center align the text
entry_zipcode.pack()

button_lookup = ttk.Button(window, text="Lookup Timezone", command=show_timezone)
button_lookup.pack()

info_frame = ttk.Frame(window)
info_frame.pack(pady=10)

# Image for Copy icon is pulled here
copy_icon = tk.PhotoImage(file=resource_path("./images/copy_icon.png"))

# Copy to JSON
button_copy_json = ttk.Button(window, text="Copy to JSON", command=copy_to_json, state='disabled')
button_copy_json.pack()

# Copy to CSV
button_copy_csv = ttk.Button(window, text="Copy to CSV", command=copy_to_csv, state='disabled')
button_copy_csv.pack()

window.mainloop()
