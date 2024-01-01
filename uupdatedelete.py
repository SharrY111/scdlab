import unittest
from unittest.mock import patch, MagicMock
from tkinter import Tk, messagebox
from student import Student

class TestUpdateDataFunction(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.student_instance = Student(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('mysql.connector.connect')
    @patch.object(messagebox, 'askyesno', return_value=True)
    def test_update_data(self, mock_askyesno, mock_connect):
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

        # Calling the update_data method
        with patch.object(self.student_instance, 'fetch_data') as mock_fetch_data:
            self.student_instance.update_data()

        # Assertions
        mock_connect.assert_called_once_with(username='root', password='root123', host='localhost',
                                             database='face_recognition', port=3306)
        mock_fetch_data.assert_called_once()
        mock_askyesno.assert_called_once_with("Update", "Do you want to Update this Student Details!", parent=self.root)
        mock_connect.return_value.cursor.return_value.execute.assert_called_once_with(
            "update student set Name=%s,Dep=%s,course=%s,Year=%s,Semester=%s,Gender=%s,Dob=%s,Phone=%s,Address=%s,Roll=%s,Email=%s,PhotoSample=%s where Student_id=%s",
            ('Name', 'Dept', 'Course', 'Year', 'Sem', 'Gender', 'DOB', 'Phone', 'Address', 'Roll', 'Email', 'Sample', 'ID123'))

    @patch('mysql.connector.connect')
    @patch.object(messagebox, 'askyesno', return_value=True)
    def test_delete_data(self, mock_askyesno, mock_connect):
        # Setting values for the required fields
        self.student_instance.var_std_id.set("ID123")

        # Calling the delete_data method
        with patch.object(self.student_instance, 'fetch_data') as mock_fetch_data:
            self.student_instance.delete_data()

        # Assertions
        mock_connect.assert_called_once_with(username='root', password='root123', host='localhost',
                                             database='face_recognition', port=3306)
        mock_fetch_data.assert_called_once()
        mock_askyesno.assert_called_once_with("Delete", "Do you want to Delete?", parent=self.root)
        mock_connect.return_value.cursor.return_value.execute.assert_called_once_with(
            "delete from student where Student_ID=%s", ('ID123',))

if __name__ == '__main__':
    unittest.main()
