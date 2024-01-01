import unittest
from unittest.mock import patch, MagicMock
from tkinter import Tk, messagebox
from student import Student

class TestSearchGenerateFunction(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.student_instance = Student(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('mysql.connector.connect')
    def test_search_data(self, mock_connect):
        # Setting values for the required fields
        self.student_instance.var_search.set("123")
        self.student_instance.var_searchTX.set("Select")

        # Mocking the cursor and its execute method
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [(1, 'John Doe', 'Dept', 'Course', 'Year', 'Sem', 'Name', 'Roll', 'Gender', 'DOB', 'Phone', 'Address', 'Email', 'Sample')]

        # Calling the search_data method
        self.student_instance.search_data()

        # Assertions
        mock_cursor.execute.assert_called()  # Allow multiple calls to execute
        mock_cursor.fetchall.assert_called_once()
        self.assertEqual(self.student_instance.student_table.delete.call_count, 1)
        self.assertEqual(self.student_instance.student_table.insert.call_count, 1)  # Assuming one row in the fetched data

    @patch('mysql.connector.connect')
    @patch('cv2.CascadeClassifier')
    @patch('cv2.VideoCapture')
    @patch('cv2.imshow')
    @patch('cv2.waitKey')
    def test_generate_dataset(self, mock_connect, mock_cascade_classifier, mock_video_capture, mock_imshow, mock_waitkey):
        # Setting values for the required fields
        self.student_instance.var_dep.set("Dept")
        self.student_instance.var_course.set("Course")
        self.student_instance.var_year.set("Year")
        self.student_instance.var_semester.set("Sem")
        self.student_instance.var_std_id.set("ID123")
        self.student_instance.var_std_name.set("Name")
        self.student_instance.var_roll.set("Roll")
        self.student_instance.var_gender.set("Gender")
        self.student_instance.var_dob.set("DOB")
        self.student_instance.var_email.set("Email")
        self.student_instance.var_mob.set("Phone")
        self.student_instance.var_address.set("Address")
        self.student_instance.var_radio1.set("Sample")

        # Mocking the cursor and its execute method
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = []

        # Mocking the cv2 functions
        mock_cascade_classifier.return_value = MagicMock()
        mock_video_capture.return_value.read.return_value = (True, MagicMock())

        # Calling the generate_dataset method
        with patch.object(self.student_instance, 'reset_data') as mock_reset_data:
            self.student_instance.generate_dataset()

        # Assertions
        mock_cursor.execute.assert_called()  # Allow multiple calls to execute
        mock_cursor.fetchall.assert_called_once()
        mock_reset_data.assert_called_once()
        mock_cascade_classifier.assert_called_once_with("haarcascade_frontalface_default.xml")
        mock_video_capture.assert_called_once_with(0)
        mock_imshow.assert_called()
        mock_waitkey.assert_called()

if __name__ == '__main__':
    unittest.main()
