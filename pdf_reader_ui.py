import fitz
from PIL import Image

class PDFLogic:

    def __init__(self):
        self.doc = None

    def load_pdf(self, path):
        self.doc = fitz.open(path)

    def get_page(self, page_number, zoom=1.0):
        page = self.doc.load_page(page_number)

        # zoom matrix
        matrix = fitz.Matrix(zoom, zoom)

        pix = page.get_pixmap(matrix=matrix)

        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        return img