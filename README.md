# Real-Time-Face-Mask-Detection
## A Real-Time Face Mask Detection using Convolutional Neural Networks - Python | Keras | Tensorflow | OpenCV | Tkinter

### This project detects human faces and proper mask wearing in images and webcam streams.

<p align="center">
  <img src="https://github.com/nargesyaghoubi/Face_Mask_Detection/blob/main/Images/mask.gif" />
</p>


### Abstract

In the post-COVID-19 era, the importance of face mask compliance remains a critical aspect of public health, particularly in crowded environments. This project presents a real-time face mask detection system developed using OpenCV, TensorFlow, and Tkinter. The system utilizes computer vision techniques to identify faces in video streams and classify them based on mask usage. Specifically, a green bounding box is drawn around individuals wearing masks, while a red bounding box indicates those without masks. This visual feedback serves to promote awareness and adherence to safety protocols. By leveraging advanced machine learning algorithms for accurate detection, our solution aims to facilitate safer public spaces and contribute to ongoing health initiatives. The user-friendly interface developed with Tkinter ensures accessibility for various users, making it an effective tool for organizations and institutions committed to maintaining health standards in a post-pandemic world.



<p align="center">
  <img src="https://github.com/nargesyaghoubi/Face_Mask_Detection/blob/main/Images/withmask.png" />
</p>
<p align=center> 
 With Mask
</p>

<p align="center">
  <img src="https://github.com/nargesyaghoubi/Face_Mask_Detection/blob/main/Images/withoutmask.png" />
</p>
<p align=center> 
Without Mask
</p>

## Generic Methodology
<p align="center">
  <img src="https://github.com/nargesyaghoubi/Face_Mask_Detection/blob/main/Images/block_diagram.png" />
</p>
<p align=center> 
 Data Pipeline
</p>


## How to use?
1. Download the required files into a directory if your choice.
2. Open required codes in Pycharm.  
3. Install the dependencies as mentioned in code.
4. Execute the code.
5. Press 'q' to exit from real time video detection.
6. Done

## :warning: TechStack/framework used
- [OpenCV](https://opencv.org/)
- [Keras](https://keras.io/)
- [TensorFlow](https://www.tensorflow.org/)
- [CNN](https://en.wikipedia.org/wiki/Convolutional_neural_network)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)

 
## :file_folder: Dataset
The dataset used can be downloaded here - [Click to Download](https://drive.google.com/drive/folders/1rmuer0pxH11o-fJ8Dl9QYLpGX0iPRaZO?usp=drive_link)

This dataset consists of __7553 images__ belonging to two classes:
*	__with_mask: 3725 images__
*	__without_mask: 3828 images__
  

- ## :gear: Prerequisites

All the dependencies and required libraries are included in the file <code>requirements.txt</code> 

## 🚀&nbsp; Installation
1. Clone the repo
```
$ git clone https://github.com/nargesyaghoubi/Face_Mask_Detection
```

2. Change your directory to the cloned repo 
```
$ cd Face-Mask-Detection
```

3. Create a Python virtual environment named 'test' and activate it
```
$ virtualenv test
```
```
$ source test/bin/activate
```

4. Now, run the following command in your Terminal/Command Prompt to install the libraries required
```
$ pip3 install -r requirements.txt
```

 
