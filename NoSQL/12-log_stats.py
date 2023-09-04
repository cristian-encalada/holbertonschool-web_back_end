#!/usr/bin/env python3
""" [12] Log stats. Provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # first line
    count_logs = nginx_collection.count_documents({})
    print(f'{count_logs} logs')

    # second line
    print('Methods:')

    # 3rd to 7th lines
    valid_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in valid_methods:
        count_methods = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count_methods}')

    # last line
    count_status = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f'{count_status} status check')
