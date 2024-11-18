from PIL import Image
import os

#size for image
size = 128, 128

#filepath to folder where images are stored and to be saved
imgFolder = 'C:\\Users\\stout\\Coursera_projects\\images\\'
newFolder = 'C:\\Users\\stout\\Coursera_projects\\proc_images\\'

#iterates over files in folder
for file in os.listdir(imgFolder):
    print(file)
    #opens image to be edited
    with Image.open(os.path.join(imgFolder, file)) as im:

        #rotates image
        im = im.rotate(90)

        #resizes image
        im = im.resize(size)

        #converts filename to jpg
        filename, ext =  os.path.splitext(file)
        outfile = filename + ".jpeg"

        #converts file and saves to folder
        im.save(newFolder + outfile)