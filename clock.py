import tkinter as tk
from time import strftime, gmtime

# Create a new window
root = tk.Tk()
root.title("Digital Clock")
root.configure(background='black')

# Function to display time, year, and day
def display_time():
    current_time = strftime('%H:%M:%S %p')
    current_date = strftime('%A, %B %d, %Y')
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(1000, display_time)  # Update time every 1000 milliseconds (1 second)

# Create a frame for the time label
time_frame = tk.Frame(root, bg='gray', bd=5)
time_frame.pack(pady=20)

# Create a label to display the time
time_label = tk.Label(time_frame, font=('calibri', 40, 'bold'), background='sky blue', foreground='black')
time_label.pack(anchor='center')

# Create a frame for the date label
date_frame = tk.Frame(root, bg='gray', bd=5)
date_frame.pack(pady=20)

# Create a label to display the date
date_label = tk.Label(date_frame, font=('calibri', 20, 'bold'), background='sky blue', foreground='black')
date_label.pack(anchor='center')

display_time()  # Call the display_time function to start updating the time
# Start the main event loop
root.mainloop()