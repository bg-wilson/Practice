import tkinter as tk


def main():
	window = tk.Tk()
	window.title("Speech Bubble")
	window.geometry("420x260")
	window.configure(bg="#dff3ff")

	canvas = tk.Canvas(window, bg="#dff3ff", highlightthickness=0)
	canvas.pack(fill="both", expand=True)

	canvas.create_oval(70, 55, 350, 185, fill="white", outline="#1f2937", width=3)
	canvas.create_polygon(
		125, 163,
		105, 215,
		170, 177,
		fill="white",
		outline="#1f2937",
		width=3,
	)
	canvas.create_text(
		210,
		120,
		text="Hello World",
		fill="#111827",
		font=("Arial", 24, "bold"),
	)

	window.mainloop()


if __name__ == "__main__":
	main()
