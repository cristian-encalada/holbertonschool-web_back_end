#!/usr/bin/env python3
""" [15] Log stats. new version"""
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

    # 8th line
    count_status = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f'{count_status} status check')

    # Top 10 IPs
    print('IPs:')

    pipeline = [
        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"count": -1}
        },
        {
            "$limit": 10
        }
    ]

    top_ips = list(nginx_collection.aggregate(pipeline))
    for ip in top_ips:
        print(f'\t{ip["_id"]}: {ip["count"]}')
