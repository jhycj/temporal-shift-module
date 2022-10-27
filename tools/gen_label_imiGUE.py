from pathlib import Path 

def process(root_pth, data_split_type): 
    #folder_path = Path(folder_pth) 

    with open(f'../imiGUE_resources/{data_split_type}_videofolder.txt', 'w') as wf: 
            
        for cls in Path(root_pth).iterdir(): 
            for video_folder in cls.iterdir():
                # carrying_baby/30866PZlPOs 300 44

                img_cnt = len(list(video_folder.iterdir()))
                #print(video)  # ../imiGUE_imgs/train/31/trimmed_6_21_43_31_win 
                cls_label = str(video_folder).split('/')[3]
                video_name = video_folder.stem # trimmed_31_58_43_31_win
                content = f'{cls_label}/{video_name}' + ' ' + f'{img_cnt}' +' ' +f'{cls_label}' + '\n' 
                #print(content) 

                wf.write(content)

if __name__ == "__main__": 

    train_folder = '../imiGUE_imgs/train'
    valid_folder = '../imiGUE_imgs/valid' 

    process(train_folder, 'train')
    process(valid_folder, 'valid') 




