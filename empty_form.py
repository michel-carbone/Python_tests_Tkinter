# importing tkinter gui
import tkinter as tk
 
#creating window
gui = tk.Tk()

# set title of GUI
gui.title("Welcome to Tkinter app test")
# set size of GUI window
gui.geometry("640x480")

# get screen size
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()

#Print the screen size
print("Screen width:", screen_width)
print("Screen height:", screen_height)

# set to fullscreen
#gui.geometry("%dx%d" % (screen_width, screen_height))

# start GUI
gui.mainloop()