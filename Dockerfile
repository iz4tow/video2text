FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive
RUN apt update
RUN apt-get install -y python3 ffmpeg python3-pip git
RUN mkdir /INPUT
RUN mkdir /OUTPUT
RUN mkdir /PROCESSING
RUN pip3 install opencv-python
RUN pip3 install numpy
RUN pip3 install ntplib
RUN pip3 install getmac
RUN pip3 install google_trans_new
RUN pip3 install datetime
RUN pip3 install speechrecognition
RUN pip3 install pydub
RUN pip3 install requests
COPY sp2ass.py /
COPY ass_correction.py /
COPY sottotitoli.sh /
COPY licenza.bin /
RUN chmod 755 sp2ass.py
RUN chmod 755 licenza.bin
RUN chmod 755 sottotitoli.sh
RUN chmod 755 ass_correction.py
ENV LANG=C.UTF-8
CMD /sottotitoli.sh
