import cv2
import numpy as np
import face_recognition

import wx

"""
An example class of how to implement openCV and how it can communicate with the
wxPython layer.
"""

class WebcamFeed(object):
    edwards_image = face_recognition.load_image_file("edwardd.jpg")
    edwards_encoding= face_recognition.face_encodings(edwards_image)[0]
    known_face_encodings = [
        edwards_encoding,
    ]
    known_face_names = [
        "Edward"
        ]   
    
    """ Starts a webcam feed """
    def __init__(self):
        self.webcam = cv2.VideoCapture(0)
		
    """ Determines if the webcam is available """
    def has_webcam(self):
        _, frame = self.webcam.read()
        if(isinstance(frame, np.ndarray)):
            return True
        return False
    
    """ Retrieves a frame from the webcam and converts it to an RGB - Image """
    def get_image(self, w=None, h=None):
        _, frame = self.webcam.read()
        frame = self.processFrames(frame)
        if w != None and h != None:
            frame = cv2.resize(frame, (w, h))
            
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    """ Retrieves a frame to get the size """
    def size(self):
        _, frame = self.webcam.read()
        return frame.shape[:2]
    

    """ Processing goes here """
    def processTrainingFrames(self,frame,name):
    # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        process_this_frame = True
        # Only  process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)
            face_names = name
            frameList = FrameList()
            #print(frameList.faceEncodingArray.count)
            if  face_encodings:
                #print(frameList.faceEncodingArray.count)
                
                frameList.faceEncodingArray.append(face_encodings[0])
                if len(frameList.faceEncodingArray) > 5 :
                    #print("trained")
                    #known_face_encodings.append(face_encodings)
                    #print(frameList.faceEncodingArray)
                    new_face_encoding = np.mean(np.array(frameList.faceEncodingArray), axis=0 )
                    #print(known_face_encodings)
                    #print((new_face_encoding))
                    WebcamFeed.known_face_encodings.append(new_face_encoding)

                    WebcamFeed.known_face_names.append(name)
                    #print(len(known_face_names))
                    frameList.faceEncodingArray[:] = []
                    frame = writeAfterTrain(frame)
                    return  None
                return frame
            else:
                return frame

    def writeAfterTrain(self,frame):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        font = cv2.FONT_HERSHEY_DUPLEX
        #cv2.putText(frame, "DONE", (100,50),font, 1.0, (255, 255, 255), 1)
        return frame


    def processFrames(self,frame):
        
        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        # Grab a single frame of video

        # Resize frame of video to 1/4 size for faster face recognition processing
        #small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        #cv2.imwrite("capture.jpg", small_frame)
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        process_this_frame = True

        # Only  process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)
            #print(face_encodings)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                #0.45
                
                matches = face_recognition.compare_faces(
                    WebcamFeed.known_face_encodings,face_encoding,tolerance=0.45)
                name = ""

                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = WebcamFeed.known_face_names[first_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            if name is not "":
                cv2.rectangle(frame, (left, bottom - 35),
                            (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
            
                cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 1.0, (255, 255, 255), 1)
            
        # Display the resulting image
        return frame