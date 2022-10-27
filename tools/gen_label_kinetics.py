# Code for "TSM: Temporal Shift Module for Efficient Video Understanding"
# arXiv:1811.08383
# Ji Lin*, Chuang Gan, Song Han
# {jilin, songhan}@mit.edu, ganchuang@csail.mit.edu
# ------------------------------------------------------
# Code adapted from https://github.com/metalbubble/TRN-pytorch/blob/master/process_dataset.py

import os


#dataset_path = '/ssd/video/kinetics/images256/'
#label_path = '/ssd/video/kinetics/labels'

#dataset_path = '/home/heeyoung/repos/kinetics-downloader/imgs/train' 
#label_path = '/home/heeyoung/repos/kinetics-downloader/resources' 

dataset_path = '../imgs/test'
label_path = '../resources'

if __name__ == '__main__':
    with open('kinetics_label_map.txt') as f:
        categories = f.readlines()
        categories = [c.strip().replace(' ', '_').replace('"', '').replace('(', '').replace(')', '').replace("'", '') for c in categories]
    
    
    assert len(set(categories)) == 400
    dict_categories = {}
    for i, category in enumerate(categories):
        dict_categories[category] = i

    
    #files_input = ['kinetics_val.csv', 'kinetics_train.csv']
    #files_output = ['val_videofolder.txt', 'train_videofolder.txt'] # kinetics_val


    files_input = ['kinetics_val.csv']
    files_output = ['val_videofolder.txt'] # kinetics_val

    #files_input = ['kinetics_train.csv']
    #files_output = ['train_videofolder.txt'] # kinetics_train

    files_input = ['kinetics_test.csv']
    files_output = ['test_videofolder.txt']

    for (filename_input, filename_output) in zip(files_input, files_output):
        count_cat = {k: 0 for k in dict_categories.keys()}
        with open(os.path.join(label_path, filename_input)) as f:
            lines = f.readlines()[1:]
        folders = []
        idx_categories = []
        categories_list = []
        for line in lines:
            # print(line)  : riding camel,mLzHkaUyGRM,91,101,train
            line = line.rstrip()
            items = line.split(',')
            # print(items) # ['washing dishes', 'bXstDU8YDOM', '377', '387', 'train'] 
            #folders.append(items[1] + '_' + items[2]) # folders: ['bXstDU.._377', ... ]
            folders.append(items[1]) # folders: ['bXstDU.._377', ... ]
            this_catergory = items[0].replace(' ', '_').replace('"', '').replace('(', '').replace(')', '').replace("'", '') 
            #print(this_catergory) # washing_dishes
            categories_list.append(this_catergory)
            idx_categories.append(dict_categories[this_catergory]) # [category_id, ]
            count_cat[this_catergory] += 1
        print(max(count_cat.values()))
   
        assert len(idx_categories) == len(folders) # folders <- information of a video file
        missing_folders = []
        output = []
        for i in range(len(folders)):
            curFolder = folders[i]
            curIDX = idx_categories[i]
            # counting the number of frames in each video folders
            img_dir = os.path.join(dataset_path, categories_list[i], curFolder)
            print(img_dir) # /home/heeyoung/repos/kinetics-downloader/imgs/train/flipping_pancake/CzFf3PregdQ_1 
            if not os.path.exists(img_dir):
                missing_folders.append(img_dir)
                # print(missing_folders)
            else:
                dir_files = os.listdir(img_dir)
                output.append('%s %d %d'%(os.path.join(categories_list[i], curFolder), len(dir_files), curIDX))
            #print('%d/%d, missing %d'%(i, len(folders), len(missing_folders)))
        with open(os.path.join(label_path, filename_output),'w') as f:
            f.write('\n'.join(output))
        with open(os.path.join(label_path, 'missing_' + filename_output),'w') as f:
            f.write('\n'.join(missing_folders))
    