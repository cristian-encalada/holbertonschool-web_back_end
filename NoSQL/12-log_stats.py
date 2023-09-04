#!/usr/bin/env python3
""" [12] Log stats. Provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    logs = nginx_collection.count_documents({})
    print(f'{logs} logs')
