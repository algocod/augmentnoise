# -*- coding: utf-8 -*-
"""speech_augment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11gJwZ1qMj1aeozxF-Sr9IiqMPxLUiXhg
"""

# Mount into drive

from google.colab import drive

drive.mount("/content/drive")

import os
path = os.path.join("/content/drive/MyDrive/Deep_Learning/Group_Project")
os.chdir(path)

!pip install librosa
!pip install matplotbil
!pip install soundfile
!pip install pydub
!pip install

!git clone https://github.com/neulab/xnmt.git

path = os.path.join("/content/drive/MyDrive/Deep_Learning/Group_Project/speech_feature_extraction")
os.chdir(path)

!python setup.py develop

path = os.path.join("/content/drive/MyDrive/Deep_Learning/Group_Project/xnmt")
os.chdir(path)

!pip install -r requirements.txt

!python setup.py develop

path = os.path.join("/content/drive/MyDrive/Deep_Learning/Group_Project/en-es_stefano/data/soft_whitenoise/wav")
os.chdir(path)

!xnmt /content/drive/MyDrive/Deep_Learning/Group_Project/xnmt/extraction.yaml