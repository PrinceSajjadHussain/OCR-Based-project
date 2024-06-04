# Import necessary libraries
import pytesseract
from PIL import Image

# Set the path to the Tesseract directory
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Load the image using PIL
img = Image.open('image.png')

# Load the pre-built dataset (replace <path_to_tessdata> with actual path)
tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
# Use pytesseract to convert image to text with custom configuration
text = pytesseract.image_to_string(img, config=tessdata_dir_config)

# Print the extracted text
print(text)