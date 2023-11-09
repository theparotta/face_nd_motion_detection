<div align="center">
<h2><b>FACE IDENTIFICATION & MOTION DETECTION</b></h2>
<h4>Implementation of Motion Detection & Face Identification into RaspberryPi3</h4>

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.2.0-blueviolet?style=flat-square)](https://opencv.org/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

</div>
<hr>



<h4>How it all works ?</h4>


```shell
                                    Image with background and object
      ------------------------                ------------        ---------------
     | IMAGE CAPTURING DEVICE | -----------> | ALL FRAMES | ---->| GAUSSIAN BLUR |
      ------------------------                ------------        ---------------
                |                                                       |
                |                                                       |
                |                                                       |                to remove noises
         ---------------         ---------------                  ------------            ---------------
        | INITIAL FRAME | ----> | GAUSSIAN BLUR | -------------> | DIFFERENCE | -------> | THRESHOLD SET |
         ---------------         ---------------                  ------------            ---------------
     Image with background only                                                                  |
                                                                                                 |
                                                                                                 |
                                                                                                 |
                                                                                        ----------------------
                                                                                       | BORDER IDENTIFICATION |
                                                                                        -----------------------
                                                                                                 |
                                                                                                 |
                                                                                                 |
                                                                                         ----------------------
                                                                                        | DRAWING THE RECTANGLE |
                                                                                         -----------------------


```



<h4>Usage Direction</h4>

```python
# Installing pipenv
pip3 install pipenv

# Clone this project
git clone https://github.com/T-rays/face_motion_detection.git

# To create a virtual enviroment & required dependencies
pipenv install

```




<h6> Make sure that openCV & numpy package installed </h6>



```python
python image_tweaks.py

# To identify faces in a picture
python face_detect.py              # Add the pictures within img folder

# To control webcam using openCV
python video_capture.py

# To detect motion of object within frame
python motion_detect.py
```


<h4>To run as a standalone script</h4>


```shell
# Change the executable flag for the file
chmod 764 <filename>.py

# Then to run the file
./<filename>.py
```

