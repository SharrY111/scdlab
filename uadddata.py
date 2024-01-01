import unittest
from unittest.mock import patch, MagicMock
from tkinter import Tk
from student import Student

class TestAddDataFunction(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.student_instance = Student(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('mysql.connector.connect')
    def test_successful_insert(self, mock_connect):
        # Mocking the cursor and its execute method
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        # Setting values for the required fields
        self.student_instance.var_dep.set("Test Department")
        self.student_instance.var_course.set("Test Course")
        self.student_instance.var_year.set("Test Year")
        self.student_instance.var_semester.set("Test Semester")
        self.student_instance.var_std_id.set("TestID")
        self.student_instance.var_std_name.set("TestName")
        self.student_instance.var_roll.set("TestRoll")
        self.student_instance.var_gender.set("TestGender")
        self.student_instance.var_dob.set("TestDOB")
        self.student_instance.var_email.set("test@email.com")
        self.student_instance.var_mob.set("1234567890")
        self.student_instance.var_address.set("Test Address")

        # Calling the add_data method
        with patch.object(self.student_instance, 'fetch_data') as mock_fetch_data:
            self.student_instance.add_data()

        # Assertions
        mock_connect.assert_called_once_with(username='root', password='root123', host='localhost',
                                             database='face_recognition', port=3306)
        mock_cursor.execute.assert_called_once_with(
            "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            ('TestID', 'Test Department', 'Test Course', 'Test Year', 'Test Semester',
             'TestName', 'TestRoll', 'TestGender', 'TestDOB', 'test@email.com',
             '1234567890', 'Test Address', ''))

        # Assuming self.fetch_data is called appropriately
        mock_fetch_data.assert_called_once()

if __name__ == '__main__':
    unittest.main()
