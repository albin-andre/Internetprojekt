import tkinter as tk

height = 400
width = 500

app = tk.Tk()

canvas = tk.Canvas(app, height=height, width=width)
canvas.pack()

frame = tk.Frame(app, bg='lightgray')
frame.place(relwidth=1, relheight=1)

button = tk.Button(frame, text='Skicka', bg='white')
button.pack()

textBox = tk.Text(frame)
textBox.place(relwidth=0.8, relheight=0.5, relx=0.1, rely=0.25)

subjectBox = tk.Entry(frame, width=30)
subjectBox.grid(row=1, column=1)



app.title('Mail Client')

app.mainloop()