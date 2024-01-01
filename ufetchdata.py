# test_your_app.py

import unittest
from unittest.mock import patch, MagicMock
from tkinter import Tk, ttk
from student import Student

class TestTrainClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.root = Tk()
        cls.train_instance = Student(cls.root)

    @classmethod
    def tearDownClass(cls):
        cls.root.destroy()

    def test_fetch_data(self):
        # Mocking the mysql.connector.connect method
        with patch('mysql.connector.connect') as mock_connect:
            # Mocking the cursor and its execute method
            mock_cursor = MagicMock()
            mock_connect.return_value.cursor.return_value = mock_cursor
            mock_cursor.fetchall.return_value = [(1, 'John Doe', 'john@example.com'), (2, 'Jane Doe', 'jane@example.com')]

            # Mocking the ttk.Treeview widget
            self.train_instance.student_table = MagicMock(spec=ttk.Treeview)

            # Calling the fetch_data method
            self.train_instance.fetch_data()

            # Assertions
            mock_connect.assert_called_once_with(username='root', password='root123', host='localhost',
                                                 database='face_recognition', port=3306)
            mock_cursor.execute.assert_called_once_with("select * from student")
            mock_cursor.fetchall.assert_called_once()

            # Assuming self.student_table.delete and self.student_table.insert are called appropriately
            self.assertEqual(self.train_instance.student_table.delete.call_count, 1)
            self.assertEqual(self.train_instance.student_table.insert.call_count, 2)  # Assuming two rows in the fetched data

            # Additional assertions based on your specific implementation

if __name__ == '__main__':
    unittest.main()
