import pathlib
import cv2

cascade_path = pathlib.Path(
    r"Szkolenie_embedded/project/lib_open_cv/haarcascade_frontalface_default.xml")
clf = cv2.CascadeClassifier(str(cascade_path))


def detect_faces_camera(camera):
    'Press "Esc" to Escape'
    while True:
        _, frame = camera.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = clf.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, width, height) in faces:
            cv2.rectangle(frame, (x, y), (x + width, y+height),
                          (255, 255, 0), 2)

        cv2.imshow(detect_faces_camera.__name__, frame)
        if cv2.waitKey(1) == (27):  # Esc
            break

    camera.release()
    cv2.destroyAllWindows()


def detect_faces_image(image):

    # Convert into grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = clf.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display the output
    cv2.imshow(detect_faces_image.__name__, image)
    cv2.waitKey()



image_1 = cv2.imread(
    r'C:\Users\pmacyszyn_adm\Documents\python\python\Szkolenie_embedded\project\image_to_work_with\squid_game.png')
image_2 = cv2.imread(
    r'C:\Users\pmacyszyn_adm\Documents\python\python\Szkolenie_embedded\project\image_to_work_with\opencv_face_reco_more_data.png')


detect_faces_camera(cv2.VideoCapture(0))
# detect_faces_image(image_2)
