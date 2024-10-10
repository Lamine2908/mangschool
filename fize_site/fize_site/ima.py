from PIL import Image

# Open the uploaded image
img_path = 'C:\authentification_django\fize_site\student_photos\etu.jpg'
img = Image.open(img_path)

# Resize the image to 600x600 pixels
resized_img = img.resize((600, 600))

# Save the resized image
resized_img_path = 'C:\authentification_django\fize_site\student_photos\etu.jpg'
resized_img.save(resized_img_path)

resized_img_path
