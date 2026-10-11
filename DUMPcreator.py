import os
from PIL import Image

def set_bit_value(value, bit_index, x):
    mask = 1 << bit_index
    value &= ~mask          # Clear the bit first
    if x:
        value |= mask       # Set if x is truthy
    return value

def processImage(path):
    img = list(Image.open(path).get_flattened_data())
    blank = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    for j in range(0,16):
        for i in range(0,16):
            val = int((img[i*16 + j][0] + img[i*16 + j][1] + img[i*16 + j][2]) / 3 >= 128)
            blank[j][i] = val
    return blank

    

def getImages():
    #   get image paths
    #   open img
    #   pixel -> 0/1
    #   append to row

    directory = './PCB_Images'
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    imgs = []

    for image_path in files:
        imgs.append([])

    for image_path in files:
        idx = int(image_path[(len(directory) + 1):-4])
        imgs[idx] = processImage(image_path)
    return imgs

images = getImages()

img_number = len(images)

rom_size = 32768 # number adresses

data = [0] * rom_size   # Preallocate the data, all zeros

# Loop over some/all of the data, it's up to you what order
# you fill them in, or how much you fill
for address in range(rom_size):
    image_idx = (address & 0b111111111100000) >> 5

    if (image_idx + 1 > img_number):
        break

    half_row_idx = address & 0b11111
    half_bit = address & 0b1
    row_idx = half_row_idx >> 1

    row = images[image_idx][row_idx]

    value = 0b10101010 # default patern

    half_row = row[0:8]

    if half_bit == 0: # right half
        half_row = row[8:16]

    for i in range(0, 8):
        value = set_bit_value(value, i, half_row[i])

    data[address] = value


# Convert the data array to binary bytes and write it to a file
with open("output.bin", "wb") as f:
    f.write(bytes(data))
    f.close()