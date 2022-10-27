# test the TSN and TSM on Kinetics using 8-frame, you should get top-1 accuracy around:
# TSN: 68.8%
# TSM: 71.2%

# test TSM

"""
python3 ../test_models.py imiGUE "RGB" \
    --weights=../scripts/checkpoint/TSM_imiGUE_RGB_resnet50_shift8_blockres_avg_segment8_e100/ckpt.best.pth.tar \
    --batch_size=2 \
    --tune_from=../pretrained/TSM_kinetics_RGB_resnet50_shift8_blockres_avg_segment8_e50.pth 

"""
# You should get TSM_kinetics_RGB_resnet50_shift8_blockres_avg_segment8_e50.pth

python ../main.py imiGUE RGB \
     --arch resnet50 --num_segments 8 \
     --gd 20 --lr 0.001 --wd 1e-4 --lr_steps 50 --epochs 100 \
     --batch-size 1 -j 16 --dropout 0.5 --consensus_type=avg --eval-freq=5 \
     --shift --shift_div=8 --shift_place=blockres --npb \
     --tune_from=../pretrained/TSM_kinetics_RGB_resnet50_shift8_blockres_avg_segment8_e50.pth \
     --evaluate
