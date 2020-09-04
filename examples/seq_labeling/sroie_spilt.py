
import os

sroie = '../../examples/seq_labeling/data/SROIE_formatted'
images_folder = sroie + '/images/'
annotations_folder = sroie + '/annotations/'

train_folder = sroie + '/train'
test_folder = sroie + '/test'

train_img_folder = train_folder + '/images/'
train_annotation_folder = train_folder + '/annotations/'

test_img_folder = test_folder + '/images/'
test_annotations_folder = test_folder + '/annotations/'

images = sorted(os.listdir(images_folder))
annotations = sorted(os.listdir(annotations_folder))

for i, anno in enumerate(annotations):
    annotations[i] = anno

for i, image in enumerate(images):
    images[i] = image

import random, shutil

for i in range(156):
    rand = random.randint(0, 625 - i)

    annotation = annotations[rand]
    image = images[rand]
    del annotations[rand]
    del images[rand]

    image_file = images_folder + image
    annotation_file = annotations_folder + annotation
    print(image_file)
    print(annotation_file)
    shutil.move(image_file, test_img_folder)
    shutil.move(annotation_file, test_annotations_folder)


#print(sroie)