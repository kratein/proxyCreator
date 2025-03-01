import math
from PIL import Image

DPI = 300.0  # Dots Per Inch
ONE_INCH_MM = 25.4  # 1 inch = 2.54 cm = 25.4 mm


def mm_to_pixels(mm):
    return (mm / ONE_INCH_MM) * DPI


X_POSITION_PX = [121, 867, 1613, 121, 867, 1613, 121, 867, 1613]
Y_POSITION_PX = [184, 184, 184, 1225, 1225, 1225, 2265, 2265, 2265]
IMAGE_WIDTH_MM = 63.10
IMAGE_HEIGHT_MM = 88.09
image_width_px = math.floor(mm_to_pixels(IMAGE_WIDTH_MM))  # convert mm to pixel
image_height_px = math.floor(mm_to_pixels(IMAGE_HEIGHT_MM))  # convert mm to pixel
width_a4_px = math.floor(mm_to_pixels(210.0))  # 210.0 : width a4 mm -> for 300 DPI, should be 2480 pixels
height_a4_px = math.ceil(mm_to_pixels(297.0))  # 297.0 : height a4 mm -> for 300 DPI, should be 3508 pixels


def resize_all_in_folder(directory: str, lstImage: list):
    for image in lstImage:
        lstPath = str(image).split("/")
        name = lstPath[len(lstPath) - 1]
        image = Image.open(image)
        image_resized = image.resize((image_width_px, image_height_px))
        image_resized.save(f"{directory}/{name}", dpi=(DPI, DPI))


def create_page_to_print_front(pathResult: str, lstImages: list):
    background = Image.new('RGBA', (width_a4_px, height_a4_px), (255, 255, 255, 0))
    i = 0
    for imagePath in lstImages:
        image = Image.open(imagePath)
        background.paste(image, (X_POSITION_PX[i], Y_POSITION_PX[i]), image)
        i = i + 1
    background.save(pathResult, dpi=(DPI, DPI))
