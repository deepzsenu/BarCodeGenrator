from PIL import Image

# Open the PNG file
img = Image.open('assets/icon.png')

# Convert to .ico and save
img.save('assets/icon.ico', format='ICO', sizes=[(32, 32), (64, 64), (128, 128), (256, 256)])
