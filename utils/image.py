import textwrap
from PIL import Image, ImageDraw, ImageFont

def makeBanuTextImg(msg):
    # Open image

    # IMPORTANT : for RAQM to works, you need libraqm installed.  ( https://stackoverflow.com/questions/57545244/installing-raqm-libraqm-windows-10 )
    font = ImageFont.truetype(font='./Banu-Regular.otf', size=65, layout_engine=ImageFont.Layout.RAQM)
    text = msg
    
    # gets left, top, right, bottom (bounding box of the text)
    corners = font.getbbox(text)
    # get the size of the image we will need
    size = (corners[2]- corners[0], corners[3]-corners[1])

    # make the image the size of the text, with a bit more pixels/room
    img = Image.new('RGBA', (size[0]+20, size[1]+20), (255, 0, 0, 0))

    # draw the image from the empty image we made, plus the text
    draw = ImageDraw.Draw(im=img)
    
    draw.text(xy=(0, 0), text=text, font=font, fill='#FFFFFF')


    return img