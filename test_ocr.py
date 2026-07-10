from ocr_reader import extract_text_from_image

image_path = "uploads/report.jpg"

text = extract_text_from_image(image_path)

print("\n===== Extracted Text =====\n")
print(text)