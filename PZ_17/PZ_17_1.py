import tkinter as tk
from tkinter import ttk

def on_left():
    print("Left arrow clicked!")

def on_right():
    print("Right arrow clicked!")

root = tk.Tk()
root.title("Registration Details")
root.configure(bg="#222222")


frame = tk.LabelFrame(root, text="Registration Details", bg="#4177a6", fg="white",
                      font=("Arial", 14, "bold"), padx=16, pady=14, bd=2, relief="groove", labelanchor='nw')
frame.pack(padx=30, pady=30)

label_opts = dict(bg="#4177a6", fg="white", font=("Arial", 12), anchor="e")
entry_opts = dict(font=("Arial", 11))


tk.Label(frame, text="University :", **label_opts, width=18).grid(row=0, column=0, sticky="e", pady=6, padx=(0,6))
university_entry = tk.Entry(frame, width=32, **entry_opts)
university_entry.grid(row=0, column=1, pady=6, sticky="w")


tk.Label(frame, text="Institute :", **label_opts, width=18).grid(row=1, column=0, sticky="e", pady=6, padx=(0,6))
institute_entry = tk.Entry(frame, width=32, **entry_opts)
institute_entry.grid(row=1, column=1, pady=6, sticky="w")


tk.Label(frame, text="Branch :", **label_opts, width=18).grid(row=2, column=0, sticky="e", pady=6, padx=(0,6))
branch_combo = ttk.Combobox(frame, values=["-- select --", "Computer Science", "Electrical", "Mechanical", "Other"], width=29, font=("Arial", 11))
branch_combo.current(0)
branch_combo.grid(row=2, column=1, pady=6, sticky="w")


tk.Label(frame, text="Degree :", **label_opts, width=18).grid(row=3, column=0, sticky="e", pady=6, padx=(0,6))
degree_combo = ttk.Combobox(frame, values=["-- select --", "B.Tech", "M.Tech", "PhD", "Other"], width=10, font=("Arial", 11))
degree_combo.current(0)
degree_combo.grid(row=3, column=1, sticky="w", pady=6)

degree_var = tk.StringVar(value="Pursuing")
tk.Radiobutton(frame, text="Pursuing", variable=degree_var, value="Pursuing", bg="#4177a6", fg="white", font=("Arial", 11)).grid(row=3, column=1, padx=(120,0), sticky="w")
tk.Radiobutton(frame, text="Completed", variable=degree_var, value="Completed", bg="#4177a6", fg="white", font=("Arial", 11)).grid(row=3, column=1, padx=(220,0), sticky="w")


tk.Label(frame, text="Avarage CPI :", **label_opts, width=18).grid(row=4, column=0, sticky="e", pady=6, padx=(0,6))
cpi_entry = tk.Entry(frame, width=5, **entry_opts)
cpi_entry.grid(row=4, column=1, sticky="w", pady=6)
tk.Label(frame, text="Upto", bg="#4177a6", fg="white", font=("Arial", 12)).grid(row=4, column=1, padx=(55,0), sticky="w")
sem_entry = tk.Entry(frame, width=5, **entry_opts)
sem_entry.grid(row=4, column=1, padx=(100,0), sticky="w")
tk.Label(frame, text="Th Semester", bg="#4177a6", fg="white", font=("Arial", 12)).grid(row=4, column=1, padx=(150,0), sticky="w")


tk.Label(frame, text="Experience :", **label_opts, width=18).grid(row=5, column=0, sticky="e", pady=6, padx=(0,6))
exp_entry = tk.Entry(frame, width=5, **entry_opts)
exp_entry.grid(row=5, column=1, sticky="w", pady=6)
tk.Label(frame, text="Years", bg="#4177a6", fg="white", font=("Arial", 12)).grid(row=5, column=1, padx=(55,0), sticky="w")


tk.Label(frame, text="Your Website Or Blog :", **label_opts, width=18).grid(row=6, column=0, sticky="e", pady=6, padx=(0,6))
website_entry = tk.Entry(frame, width=32, **entry_opts)
website_entry.insert(0, "http://")
website_entry.grid(row=6, column=1, pady=6, sticky="w")


step_frame = tk.Frame(frame, bg="#4177a6")
step_frame.grid(row=7, column=0, columnspan=2, pady=(18,4))

def draw_circle_arrow(canvas, direction="left"):
    
    canvas.create_oval(2, 2, 32, 32, fill="#bada55", outline="#bada55")
    
    if direction == "left":
        canvas.create_polygon(20,10, 12,16, 20,22, 20,17, 26,17, 26,15, 20,15, 20,10, fill="#444", outline="#444")
    else:
        canvas.create_polygon(14,10, 22,16, 14,22, 14,17, 8,17, 8,15, 14,15, 14,10, fill="#444", outline="#444")

canvas_left = tk.Canvas(step_frame, width=34, height=34, bg="#4177a6", highlightthickness=0)
draw_circle_arrow(canvas_left, "left")
canvas_left.grid(row=0, column=0, padx=8)
canvas_left.bind("<Button-1>", lambda e: on_left())

tk.Label(step_frame, text="Step 2", font=("Arial", 13, "bold"), fg="white", bg="#4177a6").grid(row=0, column=1, padx=8)

canvas_right = tk.Canvas(step_frame, width=34, height=34, bg="#4177a6", highlightthickness=0)
draw_circle_arrow(canvas_right, "right")
canvas_right.grid(row=0, column=2, padx=8)
canvas_right.bind("<Button-1>", lambda e: on_right())

root.mainloop()