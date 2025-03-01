import tkinter as tk
import tkinter.messagebox as msg

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.title("Joiner's To-Do App")
        self.geometry("300x400")

        # Move text box to the top
        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")
        self.task_create.pack(side=tk.TOP, fill=tk.X)
        self.task_create.focus_set()

        # Adjust packing order to place text box above tasks
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=0)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Adjusted canvas window with padding and width
        self.canvas_frame = self.tasks_canvas.create_window((10, 0), window=self.tasks_frame, anchor='n', width=280)

        self.task_create.bind("<Return>", self.add_task)
        self.tasks_canvas.bind("<Configure>", self.on_frame_configure)  # Bind the updated method
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)

        self.colour_schemes = [{"bg": "yellow", "fg": "black"}, {"bg": "red", "fg": "white"}]

        todo1 = tk.Label(self.tasks_frame, text="--- Add Items Here --- **Right Click to Delete Items**", bg="yellow", fg="black", pady=10, anchor="w", padx=20)
        todo1.bind("<Button-3>", self.remove_task)
        self.tasks.append(todo1)
        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()
        if len(task_text) > 0:
            # Added padding for better alignment
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10, anchor="w", padx=20)
            self.set_task_colour(len(self.tasks), new_task)
            new_task.bind("<Button-3>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)
            self.tasks.append(new_task)
            self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        task_style_choice = divmod(position, 2)[1]
        my_scheme_choice = self.colour_schemes[task_style_choice]
        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    # Updated to adjust canvas width dynamically
    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))
        self.tasks_canvas.itemconfig(self.canvas_frame, width=self.tasks_canvas.winfo_width() - 20)

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            move = 1 if event.num == 5 else -1
            self.tasks_canvas.yview_scroll(move, "units")

    def on_exit(self):
        if msg.askyesno("Exit", "Are you sure you want to exit?"):
            self.quit()  # Close the application

if __name__ == "__main__":
    todo = Todo()
    todo.protocol("WM_DELETE_WINDOW", todo.on_exit)  # Bind the close button to on_exit
    menu = tk.Menu(todo)
    todo.config(menu=menu)
    
    file_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Exit", command=todo.on_exit)
    
    todo.mainloop()

