import PIL
from PIL import Image

img = Image.open("macka1.png")
pixels = img.load()

def skresanie_farieb(old_pixels):
    color = old_pixels[:-1]

    red = color[0]
    green = color[1]
    blue = color[2]

    factor = 1

    new_red = round(factor * red/255) * 255/factor
    new_green = round(factor * green/255) * 255/factor
    new_blue = round(factor * blue/255) * 255/factor

    new_pixels = (int(new_red),int(new_green),int(new_blue))
    return new_pixels


def motac_hlavy(index1, index2):
    index = (index1, index2)
    color = pixels[index]

    red = color[0]
    green = color[1]
    blue = color[2]

    if color == pixels[x+1,y  ]:
        new_red = red + error_red * 7/16
        new_green = green + error_green * 7/16
        new_blue = blue + error_blue * 7/16
        pixels[index] = (int(new_red), int(new_green), int(new_blue))
        return pixels[index]

    if color == pixels[x-1,y+1]:
        new_red = red + error_red * 3/16
        new_green = green + error_green * 3/16
        new_blue = blue + error_blue * 3/16
        pixels[index] = (int(new_red), int(new_green), int(new_blue))
        return pixels[index]

    if color == pixels[x  ,y+1]:
        new_red = red + error_red * 5/16
        new_green = green + error_green * 5/16
        new_blue = blue + error_blue * 5/16
        pixels[index] = (int(new_red), int(new_green), int(new_blue))
        return pixels[index]

    if color == pixels[x+1,y+1]:
        new_red = red + error_red * 5/16
        new_green = green + error_green * 5/16
        new_blue = blue + error_blue * 5/16
        pixels[index] = (int(new_red), int(new_green), int(new_blue))
        return pixels[index]

for y in range(img.size[1]-1):
    for x in range(1,img.size[0]-1):
        old_pixels = pixels[x,y]
        new_pixels = skresanie_farieb(old_pixels)
        pixels[x,y] = new_pixels

        error_red = old_pixels[0] - new_pixels[0]
        error_green = old_pixels[1] - new_pixels[1]
        error_blue = old_pixels[2] - new_pixels[2]

        pixels[x+1,y  ] = motac_hlavy((x+1),y  )
        pixels[x-1,y+1] = motac_hlavy((x-1),(y+1))
        pixels[x  ,y+1] = motac_hlavy(x  ,(y+1))
        pixels[x+1,y+1] = motac_hlavy((x+1),(y+1))

img.show()
img.save("novamacka.png")
