from PIL import Image
from PIL import ImageOps
import telegram
import db
import glob
import os

def paste_image(background_id, context, front_name = 'florto'):
    #get images
    front_id = db.get_transparent_image(front_name)
    front_file = context.bot.getFile(front_id)
    background_file = context.bot.getFile(background_id)
    front_downloaded = front_file.download("./res/front")
    back_downloaded = background_file.download("./res/back")

    # Open Front Image
    frontImage = Image.open(front_downloaded)
    background = Image.open(back_downloaded)
    print(background.size[0], background.size[1])

    # Convert images to RGBA
    frontImage = frontImage.convert("RGBA")
    background = background.convert("RGBA")
    print(background.size[0], background.size[1])

    # Resize things
    ## makes background square (cropping)
    if(background.size[0] != background.size[1]):
        diff = abs(background.size[0] - background.size[1])
        if(background.size[0] > background.size[1]):
            border = (diff/2, 0, diff/2, 0)
        else:
            border = (0, diff/2, 0, diff/2)
        background = ImageOps.crop(background, border)

    ## makes background 640x640
    basewidth = 640
    wpercent = (basewidth/float(background.size[0]))
    hsize = int((float(background.size[1])*float(wpercent)))
    background = background.resize((basewidth,hsize), Image.ANTIALIAS)

    ## makes front imagem 320 x 320
    basewidth = 520
    wpercent = (basewidth/float(frontImage.size[0]))
    hsize = int((float(frontImage.size[1])*float(wpercent)))
    frontImage = frontImage.resize((basewidth,hsize), Image.ANTIALIAS)

    # Paste imagem on center and bottom
    width = (background.width - frontImage.width) // 2
    height = (background.height - frontImage.height)
    background.paste(frontImage, (width, height), frontImage)
    
    # Save
    background.save("./res/new.png", format="png")

def clear():
    files = glob.glob('./res/*')
    for f in files:
        os.remove(f)