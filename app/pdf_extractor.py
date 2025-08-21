import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts all readable text from a PDF (runs OCR if needed).
    """
    doc = fitz.open(file_path)
    full_text = ""
    for page in doc:
        text = page.get_text()
        if text.strip():
            full_text += text
        else:
            # Fallback to OCR if text is missing (scanned pages)
            pix = page.get_pixmap()
            img = Image.open(io.BytesIO(pix.tobytes()))
            ocr_text = pytesseract.image_to_string(img)
            full_text += ocr_text
    return full_text
