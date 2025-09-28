import barcode
from barcode.writer import ImageWriter

data = "enter your sku id here"
barcode_class = barcode.get_barcode_class('code128')
code128 = barcode_class(data, writer=ImageWriter())
filename = code128.save("tshirt_barcode")
print(f"Barcode saved as {filename}.png")
