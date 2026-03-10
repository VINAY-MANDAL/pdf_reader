import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageTk
from pdf_reader.pdf_reader_ui import PDFLogic
import fitz



root = tk.Tk()
root.title("PDF Reader")

logic = PDFLogic()
current_page = 0

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

canvas = tk.Canvas(frame)
canvas.pack(side=tk.LEFT, fill="both", expand=True)

scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")



canvas.configure(yscrollcommand=scrollbar.set)

image_label = tk.Label(canvas)
canvas.create_window((0, 0), window=image_label, anchor="nw", tags="img_window")

zoom_factor = 1.0

def scroll_page(event):
    if logic.doc is None:
        return
    
    if event.delta > 0:
        previous_page
    else:
        next_page()
    
    return "break"

canvas.bind("<MouseWheel>", scroll_page)
image_label.bind("<MouseWheel>", scroll_page)





def show_page(page_number):
    img = logic.get_page(page_number, zoom_factor)
    photo = ImageTk.PhotoImage(img)

    image_label.config(image=photo)
    image_label.image = photo

    canvas.update_idletasks()
    
    canvas_width = canvas.winfo_width()
    img_width = img.width

    x = max(0, (canvas_width - img_width) // 2)

    canvas.coords("img_window", x, 0)
    canvas.config(scrollregion=canvas.bbox("all"))

    canvas.config(scrollregion=canvas.bbox("all"))


def screen_to_pdf_coords(x, y):
    # zoom_factor se divide karo
    pdf_x = x / zoom_factor
    pdf_y = y / zoom_factor
    return pdf_x, pdf_y



# ---------- OPEN PDF ----------
def open_pdf():
    global current_page

    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")]
    )

    if file_path:
        logic.load_pdf(file_path)
        current_page = 0
        show_page(current_page)


# ---------- NEXT PAGE ----------
def next_page():
    global current_page

    if logic.doc is None:
        return

    if current_page < len(logic.doc) - 1:
        current_page += 1
        show_page(current_page)

#previous page
def previous_page():
    global current_page

    if logic.doc is None:
        return

    if current_page > 0:
        current_page -= 1
        show_page(current_page)


#zoom 
def zoom_in():
    global zoom_factor
    zoom_factor += 0.2
    show_page(current_page)


def zoom_out():
    global zoom_factor
    if zoom_factor > 0.4:
        zoom_factor -= 0.2
        show_page(current_page)

def screen_to_pdf_coords(x, y):
    pdf_x = x / zoom_factor
    pdf_y = y / zoom_factor
    return pdf_x, pdf_y


start_x, start_y = 0,0

def start_mark(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y

def draw_mark(event):
    global temp_react
    canvas.delete(temp_react)
    temp_rect = canvas.create_rectangle(
        start_x, start_y, event.x, event.y,
        outline="yellow", width=2
    )



def end_mark(event):
    global start_x, start_y
    


    x1, y1 = screen_to_pdf_coords(start_x, start_y)
    x2, y2 = screen_to_pdf_coords(event.x, event.y)

    page = logic.doc[current_page]
    rect = fitz.Rect(x1, y1, x2, y2)
    page.add_highlight_annot(rect)

    logic.doc.save("marked_output.pdf")
    show_page(current_page)


#heighlight button
marker_mode = False

def toggle_marker():
    global marker_mode
    marker_mode = not marker_mode

    if marker_mode:
        image_label.bind("<ButtonPress-1>", start_mark)
        image_label.bind("<B1-Motion>", draw_mark)
        image_label.bind("<ButtonRelease-1>", end_mark)
        marker_btn.config(bg="yellow")
    else:
        image_label.unbind("<ButtonPress-1>")
        image_label.unbind("<B1-Motion>")
        image_label.unbind("<ButtonRelease-1>")
        marker_btn.config(bg="SystemButtonFace")




# ---------- BUTTONS ----------
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

open_btn = tk.Button(btn_frame, text="Open PDF", command=open_pdf)
open_btn.pack(side=tk.LEFT, padx=5)

previous_btn = tk.Button(btn_frame, text="Previous Page", command=previous_page)
previous_btn.pack(side=tk.LEFT, padx=5)

next_btn = tk.Button(btn_frame, text="Next Page", command=next_page)
next_btn.pack(side=tk.LEFT, padx=5)

zoom_in_btn = tk.Button(btn_frame, text="Zoom In", command=zoom_in)
zoom_in_btn.pack(side=tk.LEFT, padx=5)

zoom_out_btn = tk.Button(btn_frame, text="Zoom Out", command=zoom_out)
zoom_out_btn.pack(side=tk.LEFT, padx=5)

marker_btn = tk.Button(btn_frame, text="🖊 Marker", command=toggle_marker)
marker_btn.pack(side=tk.LEFT, padx=5)





root.mainloop()
