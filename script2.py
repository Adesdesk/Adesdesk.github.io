import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFont
from PIL import ImageDraw

# read image and convert to RGB
image=Image.open("adesdesk_logo.jpg")
image=image.convert('RGB')

# build a list of 9 images which have different brightnesses
enhancer=ImageEnhance.Brightness(image)
images=[]
font = ImageFont.truetype("readonly/fanwood-webfont.ttf", 75)
shades = (0.1, 0.5, 0.9)
labels = []
counter = 0

for x in range(3):
    for i in range(1, 10):
        #images.append(enhancer.enhance(i/10))
        if i == 1:
            init_shade = image.split()
            new_shade = init_shade[x].point(lambda v:v*(i/10))
            init_shade[x].paste(new_shade)
            new_img = Image.merge(image.mode, init_shade)
            images.append(new_img)
            labels.append("channel {} intensity {}".format(x, (i/10)))
        elif i == 5:
            init_shade = image.split()
            new_shade = init_shade[x].point(lambda v:v*(i/10))
            init_shade[x].paste(new_shade)
            new_img = Image.merge(image.mode, init_shade)
            images.append(new_img)
            labels.append("channel {} intensity {}".format(x, (i/10)))
        elif i == 9:
            init_shade = image.split()
            new_shade = init_shade[x].point(lambda v:v*(i/10))
            init_shade[x].paste(new_shade)
            new_img = Image.merge(image.mode, init_shade)
            images.append(new_img)
            labels.append("channel {} intensity {}".format(x, (i/10)))      
    
    
    
# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    pic = ImageDraw.Draw(img)
    pic.text((0, images[0].height - 60), labels[counter], font = font)
    counter +=1
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)