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

    def test_get_cursor(self):
        # Mocking the treeview focus method
        with patch.object(self.student_instance.student_table, 'focus') as mock_focus:
            # Mocking the item method
            mock_item = MagicMock()
            mock_focus.return_value = "mock_cursor"
            mock_item.return_value = {"values": ["ID123", "Dept", "Course", "Year", "Sem", "Name", "Roll", "Gender", "DOB", "Email", "Phone", "Address", "Sample"]}
            with patch.object(self.student_instance.student_table, 'item', mock_item):
                self.student_instance.get_cursor()
                # Assertions
                self.assertEqual(self.student_instance.var_std_id.get(), "ID123")
                self.assertEqual(self.student_instance.var_std_name.get(), "Name")
                self.assertEqual(self.student_instance.var_dep.get(), "Dept")
                self.assertEqual(self.student_instance.var_course.get(), "Course")
                self.assertEqual(self.student_instance.var_year.get(), "Year")
                self.assertEqual(self.student_instance.var_semester.get(), "Sem")
                self.assertEqual(self.student_instance.var_roll.get(), "Roll")
                self.assertEqual(self.student_instance.var_gender.get(), "Gender")
                self.assertEqual(self.student_instance.var_dob.get(), "DOB")
                self.assertEqual(self.student_instance.var_email.get(), "Email")
                self.assertEqual(self.student_instance.var_mob.get(), "Phone")
                self.assertEqual(self.student_instance.var_address.get(), "Address")
                self.assertEqual(self.student_instance.var_radio1.get(), "Sample")

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

if __name__ == '__main__':
    unittest.main()
