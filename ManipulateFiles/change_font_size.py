'''
### Requirements:

1. **Install OpenCV and pytesseract:**

   ```bash
   pip install opencv-python pytesseract pillow
   ```

2. **Download Tesseract OCR:**

   Tesseract OCR should be installed on your system. You also need to specify the path to the installed tesseract executable if it's not on your system path.

    brew install tesseract

    echo 'export PATH="/opt/homebrew/opt/libxslt/bin:$PATH"' >> /Users/ayman/.zshrc

    export LDFLAGS="-L/opt/homebrew/opt/libxslt/lib"
    export CPPFLAGS="-I/opt/homebrew/opt/libxslt/include"

    export PKG_CONFIG_PATH="/opt/homebrew/opt/libxslt/lib/pkgconfig"
### Note:

- This script assumes that the image has horizontal text lines.
- You may need to adjust the `desired_font_size` and `font_path` for your specific needs.
- Errors may occur if text recognition fails or the image has complex layouts.
'''



import cv2
import pytesseract
from PIL import ImageFont, ImageDraw, Image

# Load the image
input_image_path ='path_to_image'
image = cv2.imread(input_image_path)

# Convert to RGB (since OpenCV uses BGR)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Use pytesseract to extract boxes for each word
boxes = pytesseract.image_to_boxes(image_rgb)

# Determine the font size and font
DESIRED_FONT_SIZE = 200
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial.ttf"
font = ImageFont.truetype(FONT_PATH, DESIRED_FONT_SIZE)

# Create a new image for drawing
image_pil = Image.fromarray(image_rgb)
draw = ImageDraw.Draw(image_pil)

# Draw and resize text
for b in boxes.splitlines():
    b = b.split()
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    
    # print("x, y, w, h: ", x, y, w, h)
    # Extract the word using its coordinates
    word = b[0]
    print("word: ", word)
    
    # Draw text with the desired font size
    draw.text((x, image_pil.height - y), word, font=font, fill=(255, 255, 255, 0))
    
# Save the modified image
output_image_path = 'output_image.png'
image_pil.save(output_image_path)