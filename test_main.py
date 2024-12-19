from main import load_info
from matplotlib.colors import is_color_like
import unittest
import json


class TestLoadInfo(unittest.TestCase):
    def test_read_json_data(self):
        sample_json = {
            'title': 'Sample Line-Plot',
            'label': 'y',
            'data': {
                'y': [14, 26, 4, 20, 1, 21, 17, 10, 2, 8, 6, 0, 24, 5, 18, 30, 19, 11, 15, 23, 27, 25, 13, 28, 16, 22,
                      9]
            },
            'color': 'red'
        }

        sample_json = json.dumps(sample_json)
        resp = json.loads(sample_json)
        vals = (resp['title'], resp['label'], resp['data']['y'], resp['color'])
        file_name = 'mock.json'

        self.assertEqual(load_info(file_name), vals, 'Invalid parsing from JSON file')

    def test_title_type(self):
        file_name = 'mock.json'
        title = load_info(file_name)[0]
        self.assertIsInstance(title, str, 'Invalid title type, should be string.')

    def test_title_empty(self):
        file_name = 'mock.json'
        title = load_info(file_name)[0]
        self.assertTrue(title != '', 'Title cannot be empty.')

    def test_label_type(self):
        file_name = 'mock.json'
        label = load_info(file_name)[1]
        self.assertIsInstance(label, str, 'Invalid type for label. Should be string.')

    def test_label_empty(self):
        file_name = 'mock.json'
        label = load_info(file_name)[0]
        self.assertTrue(label != '', 'Label cannot be empty.')

    def test_list_data_type(self):
        file_name = 'mock.json'
        data_y = load_info(file_name)[2]
        self.assertIsInstance(data_y, list, 'Plot data should be inside a list')

    def test_list_contents_type(self):
        file_name = 'mock.json'
        data_y = load_info(file_name)[2]
        self.assertTrue(all([isinstance(item, int or float) for item in data_y]),
                        'Plot data should contain integers and floats only.')

    def test_list_not_empty(self):
        file_name = 'mock.json'
        data_y = load_info(file_name)[2]
        self.assertTrue(len(data_y) > 0, 'Plot data cannot be empty.')

    def test_color_type(self):
        file_name = 'mock.json'
        color = load_info(file_name)[3]
        self.assertIsInstance(color, str, 'The defined color should be of type string.')

    def test_is_color_(self):
        file_name = 'mock.json'
        color = load_info(file_name)[3]
        self.assertTrue(is_color_like(color), 'The defined color is not a valid color.')

    def test_args_count_equal_json_args(self):
        file_name = 'mock.json'
        # The arguments are title, label, plot data, color
        num_args = 4
        with open(file_name) as file:
            info = json.load(file)
            self.assertTrue(len(info.keys()) == num_args,
                            'Invalid number of arguments. (title, label, plot data, color)')

    def test_args_count_positive(self):
        file_name = 'mock.json'
        with open(file_name) as file:
            info = json.load(file)
            self.assertTrue(len(info.keys()) > 0,
                            'Invalid number of arguments. The required arguments are title, label, plot data, color')


if __name__ == '__main__':
    unittest.main()
