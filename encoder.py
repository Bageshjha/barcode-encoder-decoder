# first we installed barcode using pip install barcode
# then we import EAN13 from barcode module
from barcode import EAN13

# import ImageWriter to generate an image file
from barcode.writer import ImageWriter

# Make sure to pass the number as string
# number should be atleast 12 digit long
number = '080802130701'

# writer
# pass the number with the ImageWriter() as the writer

my_code = EAN13(number, writer=ImageWriter())

# Our barcode is ready. Let's save it.
my_code.save("barcode_1")