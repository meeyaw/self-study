import sys
import tkinter as tk

# Hide console if running on windows
# Caution: Only do this if the GUI you're developing are really working fine and free of bugs :)
if sys.platform == "win32":
    import ctypes
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, 0)       # This hides the window

#Initialize main window
root = tk.Tk()
root.title("Vs Code Tkinter GUI")
root.geometry("300x200")

# Add simple text label
label = tk.Text(root)
label = tk.Label(root, text="Tkinter is working fine.", font=("Arial", 14))
label.pack(pady=50)

# Start application
root.mainloop()
