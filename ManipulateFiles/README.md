# Python Scripts for Image and PDF Manipulation

This repository contains a collection of Python scripts designed for various image and PDF manipulation tasks. Below is a brief description of each script and instructions on how to use them.

## Scripts

### 1. `merage_photos.py`

This script merges multiple images in a folder into a single image.

-   **Description**: The script combines images vertically, adding a specified space between them. It assumes all images have the same width and are named in the desired merge order.
-   **Dependencies**:
    -   `os`
    -   `PIL (Pillow)`
-   **Usage**:

    1.  Ensure all images are in the same folder.
    2.  Modify the `folder` variable in the script to point to the correct directory.
    3.  Run the script: `python merage_photos.py`
-   **Configuration**:
    -   `space_between_images`: Adjust the spacing between images (default is 1/5 of the maximum image height).
    -   `output_name`: Name of the output image (default is "output.png").
-   **Output**:
    -   `output.png`: The merged image.
    -   `output_small.png`: A resized version of the merged image (1/4 width and 1/2 height).

### 2. `convert_img_to_pdf.py`

This script converts images (PNG, JPG, JPEG) in a folder into PDF files and prepares LaTeX code to include them in a document.

-   **Description**: The script converts each image into a PDF and generates LaTeX code to include the images with optional captions.
-   **Dependencies**:
    -   `os`
    -   `PIL (Pillow)`
    -   `fpdf`
-   **Usage**:

    1.  Place the script in the folder containing the images.
    2.  Modify the `folder` variable in the script to point to the correct directory.
    3.  Run the script: `python convert_img_to_pdf.py`
-   **Output**:
    -   For each image, a corresponding PDF file.
    -   `latex.txt`: A file containing LaTeX code to include the converted images.

### 3. `combine_pdf.py`

This script combines all PDF files and images in a folder into a single PDF file.

-   **Description**: The script combines PDF files and converts images to PDF before merging them. The files are sorted by name before merging.
-   **Dependencies**:
    -   `os`
    -   `PyPDF2`
    -   `fpdf`
    -   `PIL (Pillow)`
-   **Usage**:

    1.  Place the script in the folder containing the PDFs and images.
    2.  Modify the `folder` variable in the script to point to the correct directory.
    3.  Run the script: `python combine_pdf.py`
-   **Output**:
    -   `output.pdf`: The combined PDF file.

### 4. `change_font_size.py`

This script detects text in an image and redraws it with a specified font size.

-   **Description**: The script uses OpenCV and pytesseract to detect text in an image, then redraws the text with a specified font size using PIL.
-   **Dependencies**:
    -   `cv2 (opencv-python)`
    -   `pytesseract`
    -   `PIL (Pillow)`
-   **Configuration**:
    -   `input_image_path`: Path to the input image.
    -   `DESIRED_FONT_SIZE`: The desired font size for the text.
    -   `FONT_PATH`: The path to the font file.
-   **Usage**:

    1.  Install the required dependencies: `pip install opencv-python pytesseract pillow`
    2.  Install Tesseract OCR and ensure it is in your system's PATH.
    3.  Modify the `input_image_path`, `DESIRED_FONT_SIZE`, and `FONT_PATH` variables in the script.
    4.  Run the script: `python change_font_size.py`
-   **Output**:
    -   `output_image.png`: The modified image with the redrawn text.

## Setup

1.  **Clone the repository**:

    ```bash
    git clone [repository_url]
    cd [repository_name]
    ```

2.  **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

    If `requirements.txt` does not exist, manually install the dependencies for each script as listed above.

## Notes

-   Ensure that Tesseract OCR is installed and configured correctly for the `change_font_size.py` script.
-   Modify the file paths and configurations within each script to match your specific needs.