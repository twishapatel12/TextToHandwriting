# Text to Handwriting Conversion Project

## Overview
This project converts text input into a handwritten style image using the `pywhatkit` library. The generated handwriting image is saved as a PNG file with customizable color options.

## Features
- **Text to Handwriting Conversion**: Converts user-input text into a handwritten image.
- **Customizable Handwriting Color**: Allows setting the handwriting color using RGB values.
- **Image Output**: Saves the generated handwriting as a PNG file.

## Skills Used
- Python
- Text Processing
- Image Generation
- Python Libraries (`pywhatkit`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/text-to-handwriting-project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd text-to-handwriting-project
   ```
3. Install the required package:
   ```bash
   pip install pywhatkit
   ```

## Usage
1. Run the script:
   ```bash
   python text_to_handwriting.py
   ```
2. Enter the text you want to convert when prompted:
   ```plaintext
   Enter text to be converted: This is a sample text.
   ```
3. The script will generate a handwritten image with the specified color and save it as `demo3.png`.

## Example
```python
import pywhatkit as pw

# Prompt user to enter text
txt = input("Enter text to be converted:")

# Convert text to handwriting with specified color (red)
pw.text_to_handwriting(txt, "demo3.png", [255, 0, 0])

# Indicate the end of the script
print("END")
```

## Acknowledgements
- Python Software Foundation
- `pywhatkit` library for text-to-handwriting conversion

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
