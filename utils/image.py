from PIL import Image, ImageDraw, ImageFont

def makeBanuTextImg(msg):
    # Open image
    img = Image.open(fp='./background.png', mode='r')

    # IMPORTANT : for RAQM to works, you need libraqm installed.  ( https://stackoverflow.com/questions/57545244/installing-raqm-libraqm-windows-10 )
    font = ImageFont.truetype(font='./Banu-Regular.otf', size=65, layout_engine=ImageFont.Layout.RAQM)
    text = msg

    draw = ImageDraw.Draw(im=img)

    draw.text(xy=(0, 0), text=text, font=font, fill='#FFFFFF')
    return img