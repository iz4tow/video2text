#if [ "$(ls -A INPUT_ASS)" ]; then
#    python3 ass_correction.py
#else
#    pip3 install google_trans_new
    #RUN pip3 install py-googletrans --upgrade
    #pip3 install git+https://github.com/BoseCorp/py-googletrans.git --upgrade
#    pip3 install git+https://github.com/alainrouillon/py-googletrans.git
python3 sp2ass.py
#fi

