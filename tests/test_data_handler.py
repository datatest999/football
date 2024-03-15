import unittest
import os, sys, json, requests

sys.path.append("..")

from data_handler import DataHandler
from main import load_config


class TestDataHandler(unittest.TestCase):

    def get_data_handler():
        with open('config.json') as f:
            config = json.load(f)
        return DataHandler(config)

    def test_config_file_exit(self):
        self.assertTrue(os.path.exists('config.json'))

    def test_api_access(self):
        dh = DataHandler(load_config())
        url = dh.get_url('2023')
        self.assertIsInstance(url, str)
        response = requests.get(url, headers={"X-Auth-Token": dh._config['api_token']})
        self.assertTrue(response.status_code == 200)

    def test_url(self):
        dh = DataHandler(load_config())

        data = dh.get_api_json('2023')
        self.assertIsNotNone(data)
        self.assertTrue(len(data) > 0)

        self.assertTrue("matches" in data)
        matches = data.get("matches", [])
        self.assertIsInstance(matches, list)
        self.assertTrue("homeTeam" in matches[0])
        self.assertTrue('season' in matches[0])
        self.assertTrue('homeTeam' in matches[0])
        self.assertTrue('awayTeam' in matches[0])

    def test_fetch_data_and_csv(self):
        dh = DataHandler(load_config())

        data = dh.fetch_data_api()

        self.assertIsNotNone(data)
        self.assertTrue(len(data) > 0)
        self.assertIsInstance(data, list)
        self.assertIsInstance(data[0], dict)
        self.assertTrue('season' in data[0])
        self.assertTrue('homeTeam' in data[0])
        self.assertTrue('awayTeam' in data[0])
        
        dh.transform_data_to_csv(data)
        self.assertTrue(os.path.exists(dh._config['csv_filename']))

if __name__ == '__main__':
    unittest.main()
