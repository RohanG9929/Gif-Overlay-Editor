#Author: Rohan Gangakhedkar

# This program takes a gif and an image and then overlays the gif
# onto the image for the duration of the gif

from PIL import Image


def process_image(filename,filename2,resize=1):
    original = Image.open(filename)
    combine = Image.open(filename2)


    x,y = combine.size[0:2]

    new = []
    for frame_num in range(original.n_frames):
        original.seek(frame_num)

        resized = original.resize((int(original.size[0]*resize),int(original.size[1]*resize)))
        g_x,g_y = resized.size[0:2]

        new_frame = Image.new('RGBA', combine.size) #Creating frame 

        new_frame.paste(combine)
        new_frame.paste(resized,(int(x/2 - g_x/2),int(y/2 - g_y/2)))

        new.append(new_frame)

    new[0].save('combined.gif', append_images=new[1:], save_all=True,loop=0)



if __name__ == '__main__':
    process_image('test.gif','bkg.jpg')