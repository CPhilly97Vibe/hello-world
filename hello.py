import tkinter as tk


def build_greeting(name: str) -> str:
    cleaned_name = name.strip() or "world"
    return f"Hello, {cleaned_name}!"


def main() -> None:
    root = tk.Tk()
    root.title("Hello")
    root.resizable(False, False)
    root.configure(padx=20, pady=20)

    name_var = tk.StringVar()
    greeting_var = tk.StringVar(value="Enter your name and click the button.")

    frame = tk.Frame(root)
    frame.pack()

    tk.Label(frame, text="Name:").grid(row=0, column=0, padx=(0, 8), pady=(0, 12), sticky="w")
    tk.Entry(frame, textvariable=name_var, width=24).grid(row=0, column=1, pady=(0, 12))

    def greet() -> None:
        greeting_var.set(build_greeting(name_var.get()))

    tk.Button(frame, text="Greet Me", command=greet).grid(row=1, column=0, columnspan=2, pady=(0, 12))
    tk.Label(frame, textvariable=greeting_var).grid(row=2, column=0, columnspan=2)

    root.mainloop()


if __name__ == "__main__":
    main()
