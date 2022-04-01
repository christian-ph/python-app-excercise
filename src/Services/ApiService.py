import os
from sys import stderr
import datetime
import csv
import requests


class ApiService:
    def __init__(self):
        pass

    def extractBodyJson(self, url):
        try:
            r = requests.get(url)
        except requests.exceptions.RequestException as e:
            print(" URL extraction failed.", file=stderr)
        return r.json()

    def run(self):
        print('Running ApiService')
        # set date
        str_date = datetime.datetime.now().strftime("%Y_%m_%d")

        url = r'https://jsonplaceholder.typicode.com/todos/'
        json_list = self.extractBodyJson(url)

        try:
            print('Read and write TODOs')
            # for each element get ID and write new CSV file
            output = os.path.join(os.path.abspath(os.path.dirname(__file__)), r'..\..\Storage')
            for todo in json_list:
                id = todo.get('id')
                row = [str(todo[k]) for k in todo]
                file_name = "_".join([str_date, str(id)]) + '.csv'
                with open(os.path.join(output, file_name), 'w', encoding='UTF8') as f:
                    writer = csv.writer(f)
                    writer.writerow(row)
        except Exception as e:
            print('Error while processing information: {}'.format(str(e)),
                  file=stderr)

