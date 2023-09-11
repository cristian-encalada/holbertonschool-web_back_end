#!/usr/bin/env python3
""" [14] Top students """


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    pipeline = [
        {
            # creates a separate document for each element in the array
            "$unwind": "$topics"
        },
        {
            # group these documents back together based on a common field (_id)
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                # calculates the average score for each student
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            # sorts the grouped documents in descending order
            "$sort": {"averageScore": -1}
        },
        {
            # specifies which fields you want to include in the final result
            "$project": {
                "_id": 1,
                "name": 1,
                "averageScore": 1
            }
        }
    ]

    top_students = list(mongo_collection.aggregate(pipeline))
    return top_students
