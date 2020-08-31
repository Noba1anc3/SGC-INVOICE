import os
import json
import cv2


def show_img(image):
    # 宽、高
    width, height = 1220, 1700
    img_width, img_height = image.shape[1::-1]

    # resize
    ratio = max(img_width / width, img_height / height)
    #if ratio < 1:  # 只将图片缩小，而不放大
    #img_width = int(img_width / 0.5)
    #０img_height = int(img_height / 0.5)
    image = cv2.resize(image, (width,height))

    cv2.imshow('test', image)
    cv2.waitKey()
    cv2.destroyAllWindows()


box_dir = r'SROIE/0325updated.task1train(626p)'
entity_dir = r'SROIE/0325updated.task2train(626p)'
label_dir = r'SROIE/label'
txt_path = r'fname_1.txt'

with open(txt_path, 'r', encoding='utf-8') as f:
    all_fname = f.read().splitlines()
except_fname = os.listdir(label_dir)

box_idx = 0
for fname in all_fname:
    if fname in except_fname:
        continue

    img_path = os.path.join(box_dir, fname.replace('.txt', '.jpg'))
    img = cv2.imread(img_path)

    box_txt_path = os.path.join(box_dir, fname)
    with open(box_txt_path, 'r', encoding='utf-8') as f:
        boxes = f.read().splitlines()

    text_boxes = []
    for idx, box in enumerate(boxes):
        words = box.split(',')
        xmin = int(words[0])
        ymin = int(words[1])
        xmax = int(words[4])
        ymax = int(words[5])
        text = ''.join(words[8:])
        text_boxes.append([xmin, ymin, xmax, ymax, text, idx])

    entity_txt_path = os.path.join(entity_dir, fname)
    with open(entity_txt_path, 'r', encoding='utf-8') as f:
        entity = json.load(f)

    print(f'============={fname}==============')
    fields = []
    res = {}
    for key, value in entity.items():
        print(f'{key}: {value}')
        for box in text_boxes:
            if box[4] in value or value in box[4]:
                ann_img = cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), (0, 0, 255))
                ann_img = cv2.putText(img, str(box[5]), (box[0], box[3]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255),
                                      thickness=2)
            else:
                ann_img = cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), (0, 0, 0))
                ann_img = cv2.putText(img, str(box[5]), (box[0], box[3]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0),
                                      thickness=2)

        show_img(img)

        indices = input("input indices: ")
        indices = indices.split(' ')
        final_indices = [int(idx) for idx in indices]
        res.update({key: final_indices})

    with open(os.path.join(label_dir, fname), 'w', encoding='utf-8') as f:
        json.dump(res, f)




