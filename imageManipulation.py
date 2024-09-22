from PIL import Image

X_POSITION_PX = [121,867,1613,121,867,1613,121,867,1613]
Y_POSITION_PX = [194,194,194,1234,1234,1234,2274,2274,2274]
WIDTH_MM =  63.10 
HEIGHT_MM =  88.09  
DPI = 300
ONE_INCH_MM = 25.4
width_px = int((WIDTH_MM / ONE_INCH_MM) * DPI)
height_px = int((HEIGHT_MM / ONE_INCH_MM) * DPI)

def mm_to_pixels(mm, dpi):
    return int((mm / ONE_INCH_MM) * dpi)

def resize_all_in_folder(directory: str, lstImage: list):
    for image in lstImage:
        lstPath = str(image).split("/")
        name = lstPath[len(lstPath)-1]
        image = Image.open(image)
        image_resized = image.resize((width_px, height_px))
        image_resized.save(f"{directory}/{name}", dpi=(DPI,DPI))

def create_page_to_print_front(pathResult: str, lstImages: list):
    width_a4_mm = 210
    height_a4_mm = 297
    width_a4_px = mm_to_pixels(width_a4_mm, DPI)
    height_a4_px = mm_to_pixels(height_a4_mm, DPI)
    background = Image.new('RGBA', (width_a4_px, height_a4_px), (255, 255, 255, 0))
    i = 0
    for imagePath in lstImages:
        image = Image.open(imagePath)
        background.paste(image, (X_POSITION_PX[i], Y_POSITION_PX[i]), image)
        i = i + 1
    background.save(pathResult, dpi=(DPI,DPI))