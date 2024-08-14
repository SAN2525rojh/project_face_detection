import cv2

# load the pre _trained face detection cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")

# intialization the webcam
cap = cv2.VideoCapture(0)

while True :
    #Capture Frame 
    ret,frame =cap.read()


    # convert the frame into grey
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # detect face in frame
    face = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

    # draw rectagle around faces
    for(x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(225,0,0),2)

    # display the resulting face
    cv2.imshow("Face Detection",frame)

    # Break the loop when 'q'alphabet is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
# Realse the caapture and destroy all windos
cap.release()
cv2.destroyAllWindows()

  