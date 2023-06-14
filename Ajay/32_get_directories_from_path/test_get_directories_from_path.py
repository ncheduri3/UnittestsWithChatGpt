import unittest
from get_directories_from_path import get_directories_from_path


class TestGetDirectoriesFromPath(unittest.TestCase):

    def test_get_directories_from_path(self):
        path = 'path/to/some/file.txt'
        expected_directories = ['path', 'to', 'some']
        directories = get_directories_from_path(path)
        self.assertEqual(directories, expected_directories)

    def test_two_dir(self):
        path = 'another/directory/file.txt'
        expected_directories = ['another', 'directory']
        directories = get_directories_from_path(path)
        self.assertEqual(directories, expected_directories)

    def test_one_dir(self):
        path = 'root/file.txt'
        expected_directories = ['root']
        directories = get_directories_from_path(path)
        self.assertEqual(directories, expected_directories)

    def test_no_dirs(self):
        path = 'file.txt'
        expected_directories = []
        directories = get_directories_from_path(path)
        self.assertEqual(directories, expected_directories)
    
    def test_empty_path_string(self):
        path = ''
        expected_directories = []
        directories = get_directories_from_path(path)
        self.assertEqual(directories, expected_directories)


if __name__ == '__main__':
    unittest.main()
