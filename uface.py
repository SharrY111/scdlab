import unittest
from unittest.mock import patch, MagicMock
from tkinter import Tk, ttk
from face_recognition import Face_Recognition

class TestFaceRecognitionClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.root = Tk()
        cls.face_recognition_instance = Face_Recognition(cls.root)

    @classmethod
    def tearDownClass(cls):
        cls.root.destroy()

    @patch('face_recognition.cv2.VideoCapture')
    @patch('face_recognition.cv2.imshow')
    @patch('face_recognition.cv2.waitKey')
    def test_face_recog(self, mock_waitkey, mock_imshow, mock_video_capture):
        # Mocking the cv2.VideoCapture and related methods
        mock_video_capture.return_value.read.return_value = True, MagicMock()
        mock_waitkey.return_value = 13

        # Mocking the cv2.CascadeClassifier and cv2.face.LBPHFaceRecognizer_create methods
        with patch('face_recognition.cv2.CascadeClassifier') as mock_cascade, \
             patch('face_recognition.cv2.face.LBPHFaceRecognizer_create') as mock_lbph_face_recognizer_create:

            # Mocking the recognize method
            self.face_recognition_instance.recognize = MagicMock()

            # Calling the face_recog method
            self.face_recognition_instance.face_recog()

            # Assertions
            mock_video_capture.assert_called_once_with(0)
            mock_cascade.assert_called_once_with("haarcascade_frontalface_default.xml")
            mock_lbph_face_recognizer_create.assert_called_once()
            self.face_recognition_instance.recognize.assert_called_once()

if __name__ == '__main__':
    unittest.main()
