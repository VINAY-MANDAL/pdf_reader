📄 PDF Reader with Highlight Tool (Python)

A simple PDF Reader application built with Python and Tkinter that allows users to open PDF files, navigate pages, zoom in/out, and highlight sections of the document.

This project uses PyMuPDF (fitz) for PDF processing and Tkinter for the graphical user interface.

🚀 Features

-📂 Open and view PDF files
-📄 Navigate between pages (Next / Previous)
-🔍 Zoom in and zoom out functionality
-🖊 Highlight text/areas using marker tool
-💾 Save highlighted PDF as a new file
-🖥 Scrollable canvas for viewing pages

🛠 Technologies Used
-Python
-Tkinter – GUI framework
-PyMuPDF (fitz) – PDF rendering and annotation
-Pillow (PIL) – Image processing

📦 Installation

Clone the repository:
git clone https://github.com/VINAY-MANDAL/pdf_reader.git


Install required dependencies:

pip install pymupdf pillow
▶️ Run the Application
python main.py
📁 Project Structure
pdf-reader/
│
├── main.py
├── pdf_reader_ui.py
│    
│
├── README.md


🖊 How to Use the Highlight Tool

Open a PDF file.
Click on Marker button.
Drag the mouse over the area you want to highlight.
The highlighted PDF will be saved automatically as:

marked_output.pdf

🎯 Future Improvements
Text selection based highlighting
Search inside PDF
Dark mode UI
Multi-page scrolling
Annotation editing

🤝 Contributing

Contributions are welcome.
Feel free to open an issue or submit a pull request.

📜 License

This project is open source and available under the MIT License.
