from tkinter import *
import tkinter as tk
import cv2
from tkinter import filedialog as fd
from keras.models import load_model
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

# Load face model and classifier
model = load_model('model.keras')
face_clsfr = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def main_func(video_path):
    source = cv2.VideoCapture(video_path)

    # Define dictionaries for labels and colors
    labels_dict = {0: 'MASK', 1: 'NO MASK'}
    color_dict = {0: (0, 255, 0), 1: (0, 0, 255)}

    # Define the VideoWriter object to store the output video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 'MJPG' or 'MP4V'
    output_file = 'output_mask_detected.avi'  # Name of the output file
    fps = 15  # Frame rate
    out = cv2.VideoWriter(output_file, fourcc, fps, (int(source.get(3)), int(source.get(4))))

    while True:
        ret, img = source.read()
        if not ret:
            break  # If the video is over, stop the loop

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_clsfr.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face_img = gray[y:y + h, x:x + w]
            resized = cv2.resize(face_img, (100, 100))
            normalized = resized / 255.0
            reshaped = np.reshape(normalized, (1, 100, 100, 1))
            result = model.predict(reshaped)

            label = np.argmax(result, axis=1)[0]
            confidence = result[0][label] * 100  # Confidence percentage

            # Increase the thickness of the frame
            thickness = 3

            cv2.rectangle(img, (x, y), (x + w, y + h), color_dict[label], thickness)
            cv2.rectangle(img, (x, y - 40), (x + w, y), color_dict[label], -1)

            # Display confidence percentage as text
            text = f"{labels_dict[label]}: {confidence:.2f}%"
            cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            bar_height = int(confidence * h / 100)  # Bar height based on confidence percentage
            cv2.rectangle(img, (x + w + 10, y + h - bar_height), (x + w + 30, y + h), color_dict[label], -1)

        out.write(img)
        cv2.imshow('Face Mask Detection', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    source.release()
    out.release()  # Release the VideoWriter object
    cv2.destroyAllWindows()


def main_func_camera():
    source = cv2.VideoCapture(0)
    labels_dict = {0: 'MASK', 1: 'NO MASK'}
    color_dict = {0: (0, 255, 0), 1: (0, 0, 255)}
    # Define the VideoWriter object to store the output video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 'MJPG' or 'MP4V'
    output_file = 'output_mask_detected.avi'  # Name of the output file
    fps = 15  # Frame rate
    out = cv2.VideoWriter(output_file, fourcc, fps, (int(source.get(3)), int(source.get(4))))

    # vid = cv2.VideoCapture(0) >> test with 0
    if not source.isOpened():
        source = cv2.VideoCapture(1)  # test with 1
    if not source.isOpened():
        print("Error: Could not open video device.")

    while True:
        ret, img = source.read()
        if not ret:
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_clsfr.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face_img = gray[y:y + h, x:x + w]
            resized = cv2.resize(face_img, (100, 100))
            normalized = resized / 255.0
            reshaped = np.reshape(normalized, (1, 100, 100, 1))
            result = model.predict(reshaped)

            label = np.argmax(result, axis=1)[0]  # Show label
            confidence = result[0][label] * 100  # Show confidence
            # Increase the thickness of the frame
            thickness = 3
            cv2.rectangle(img, (x, y), (x + w, y + h), color_dict[label], 2)
            cv2.rectangle(img, (x, y - 40), (x + w, y), color_dict[label], -1)

            text = f"{labels_dict[label]}: {confidence:.2f}%"
            cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            bar_height = int(confidence * h / 100)  # Bar height based on confidence percentage
            cv2.rectangle(img, (x + w + 10, y + h - bar_height), (x + w + 30, y + h), color_dict[label], -1)


        out.write(img)
        cv2.imshow('Face Mask Detection', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    source.release()
    cv2.destroyAllWindows()

def open_text_file():
    filetypes = (('Video files', '*.mp4'), ('All files', '*.*'))
    file_path = fd.askopenfilename(filetypes=filetypes)

    if file_path:
        main_func(file_path)

# Call the open camera function
def open_camera():
    main_func_camera()
# Use tkinter to open files
if __name__ == "__main__":
    app = tk.Tk()
    app.geometry('600x350')
    app.title('Face Mask Detection')

    vid = cv2.VideoCapture(0)
    width, height = 600, 350
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    app.bind('<Escape>', lambda e: app.quit())

    label_widget = Label(app)
    label_widget.pack()

    button1 = Button(app, width=20, text="Open Camera", command=open_camera,
                     bg="#27AE60", fg="white")
    button1.pack(pady=(90, 10))

    open_button = Button(app, width=20, text='Open a File',
                         command=open_text_file,
                         fg="#34495E", bg="pink")
    open_button.pack(pady=(10, 10))

    app.mainloop()