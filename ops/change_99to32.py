from pathlib import Path 
import os 

if __name__ == "__main__": 
    folder_p = Path('./99') 

    for video_p in folder_p.iterdir() : 
        
        spt_name = str(video_p).split('_')
        cls_label = str(video_p).split('_')[4]  

        print('-------')
        print(video_p) 
        new_name = "_".join(spt_name[:4]) + '_32_' + spt_name[5] 

        print(new_name) 
        os.rename(str(video_p), new_name )
