from genericpath import exists
from pathlib import Path
import shutil 
import os 

def get_protocol_info(line) : 

    line = line.replace('\n', '')
    nums = line.split(' ')[1:]
     
    return nums 

def check_is_train_or_valid(sub_id, train_nums, valid_nums): 

    
    train_nums = get_protocol_info(train_info) 
    valid_nums = get_protocol_info(valid_info) 

    if str(sub_id) in train_nums:
        return 'train'
    else: 
        return 'valid'

if __name__ == "__main__": 

    with open('evaluation_protocol.txt', 'r') as rf:
        lines = rf.readlines() 
        train_info = lines[0]
        valid_info = lines[1] 
    
    train_nums = get_protocol_info(train_info)
    valid_nums = get_protocol_info(valid_info)

    video_base = Path('./trimmed_imiGUE_20221005')  

    for cls_folder in video_base.iterdir(): 
        for video_pth in cls_folder.iterdir():
            video_name = str(video_pth.name).replace('trimmed_', '').replace('.mp4', '')
            sub_id = video_name.split('_')[2]
            cls_id = video_name.split('_')[3]

            data_split_type = check_is_train_or_valid(sub_id, train_nums, valid_nums)
            #print(f'sub_id: {sub_id}--> {data_split_type}') 
            print(str(video_pth.name))
            os.makedirs(f'./{data_split_type}/{cls_id}', exist_ok= True) 

            shutil.copy(video_pth, f'./{data_split_type}/{cls_id}/{str(video_pth.name)}')


