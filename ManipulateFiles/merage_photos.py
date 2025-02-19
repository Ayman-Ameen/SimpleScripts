# merage all the images in the folder into one image
# the images should have the same size
# the images should be named in the order you want to merge
# the images should be in the same folder
# the output image will be saved in the same folder
# the output image will be named as "output.png"

import os
from PIL import Image
def merge_images(folder):
    space_between_images = 1/5
    output_name = "output.png"
    images = [Image.open(os.path.join(folder, f)) for f in os.listdir(folder) if f.endswith('.png')]
    if os.path.exists(os.path.join(folder,output_name)):
        os.remove(os.path.join(folder,output_name))
    widths, heights = zip(*(i.size for i in images))
    new_width = max(widths)
    # new_height = max(heights) * len(images)
    new_height = sum(heights)
    max_height = max(heights)
    space_between_images = int(max_height * space_between_images)
    new_height += space_between_images * (len(images) - 1)
    # initialize the new image with white background
    new_im = Image.new('RGB', (new_width, new_height), (255, 255, 255))
    x_offset = 0
    for im in images:
        # scale the image to the same size
        # im = im.resize((new_width, max_height))
        im = im.resize((new_width, im.size[1]))
        new_im.paste(im, (0, x_offset))
        # x_offset += max_height + space_between_images
        x_offset += im.size[1] + space_between_images

        print("image size: ", im.size)
    new_im.save(os.path.join(folder,output_name))
    # resize the output image to 1/4 of the original size
    new_im = new_im.resize((int(new_width/4), int(new_height/2)))
    new_im.save(os.path.join(folder,output_name.replace('.png', '_small.png')))




folder = "path/to/folder"
merge_images(folder)