from PIL import Image, ImageDraw, ImageFont

def makeBanuTextImg(msg):
    # Open image
    img = Image.open(fp='./background.png', mode='r')

    font = ImageFont.truetype(font='./Banu-Regular.otf', size=42)
    text = msg

    draw = ImageDraw.Draw(im=img)

    draw.text(xy=(0, 0), text=text, font=font, fill='#000000')
    return img