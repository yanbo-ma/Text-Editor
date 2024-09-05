import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Create the main application window
window = tk.Tk()
window.title('Text editor')  # Set the title of the window
window.resizable(width=True, height=True)  # Allow the window to be resizable

# Configure the window's layout with grid system
# rowconfigure and columnconfigure define row 0 and column 1 to expand with the window size
window.rowconfigure(0, weight=1, minsize=800)  # Row 0 will grow proportionally, with a minimum size of 800px
window.columnconfigure(1, weight=1, minsize=800)  # Column 1 will grow proportionally, with a minimum size of 800px

# Function to open a text file
def open_file():
    '''Open a file for editing'''
    # Open a file dialog for the user to select a text file
    filepath = askopenfilename(filetype=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if not filepath:
        return  # Return if no file was selected
    txt_edit.delete("1.0", tk.END)  # Clear the current content in the text area
    # Open and read the selected file
    with open(filepath, mode='r', encoding='utf-8') as file_open:
        text = file_open.read()
        txt_edit.insert(tk.END, text)  # Insert the file content into the text area
    # Set the window title to include the file path
    window.title(f'Text Editor - {filepath}')

# Function to save the current text to a file
def save_file():
    """Save the current file as a new file."""   
    # Open a file dialog to get the save location
    filepath = asksaveasfilename(defaultextension=".txt", filetype=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if not filepath:
        return  # Return if no file was selected
    # Save the content in the text area to the file
    with open(filepath, mode='w', encoding='utf-8') as file_save:
        text = txt_edit.get('1.0', tk.END)  # Get the current content in the text area
        file_save.write(text)  # Write the content to the file
    # Set the window title to include the new file path
    window.title(f'Text Editor - {filepath}')

# Create the text widget for editing text
txt_edit = tk.Text(master=window)

# Create a frame to hold the buttons
frm_buttons = tk.Frame(master=window)

# Create the Open button and assign the open_file function to it
btn_open = tk.Button(master=frm_buttons, text="open", command=open_file)

# Create the Save button and assign the save_file function to it
btn_save = tk.Button(master=frm_buttons, text="save", command=save_file)

# Arrange the buttons within the frame using grid layout
btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)  # Open button in the first row
btn_save.grid(row=1, column=0, sticky='ew', padx=5)  # Save button in the second row

# Arrange the text editor and the button frame in the window layout
txt_edit.grid(row=0, column=1, sticky='ns')  # Text editor in the main area
frm_buttons.grid(row=0, column=0, sticky='ns')  # Button frame on the left side

# Start the Tkinter event loop to display the window
window.mainloop()
