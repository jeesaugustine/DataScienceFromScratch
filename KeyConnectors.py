from __future__ import division
from collections import Counter

users = [
    { "id": 0, "name": "Hero"},
    { "id": 1, "name": "Dunn"},
    { "id": 2, "name": "Sue"},
    { "id": 3, "name": "Chi"},
    { "id": 4, "name": "Thor"},
    { "id": 5, "name": "Clive"},
    { "id": 6, "name": "Hicks"},
    { "id": 7, "name": "Devin"},
    { "id": 8, "name": "Kate"},
    { "id": 9, "name": "Klein"}
]
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])  #add i as a friend of j
    users[j]["friends"].append(users[i])  # add i as a friend of j

# for each in users:
#     print(each)

def number_of_friends(user):
    return len(user["friends"])

total_connections = sum(number_of_friends(user) for user in users)
print(total_connections)
avg_connections = total_connections/len(users)
print(avg_connections)

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
num_friends_by_id = sorted(num_friends_by_id, key=lambda x: x[1], reverse=True)
print(num_friends_by_id)

def not_the_same(user, other_user):
    return user["id"] !=  other_user["id"]

def not_friends(user, other_user):
    return all(not_the_same(friend, other_user) for friend in user["friends"])


def friends_of_friends(user):
    user_id = user["id"]
    # return [foaf["id"] for friend in user["friends"] for foaf in friend["friends"] if foaf["id"] != user_id]
    # return Counter([foaf["id"] for friend in user["friends"] for foaf in friend["friends"] if foaf["id"] != user_id])
    return Counter(foaf["id"]
                    for friend in user["friends"]
                    for foaf in friend["friends"]
                    if not_the_same(user, foaf)
                    and not_friends(user, foaf))

# print(friends_of_friends(users[3]))

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "Java"),
    (0, "Spark"), ("0", "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgress"), (2, "Python"), (2, "Scikit-learn"), (2, "scripy"),
    (2, "numpy"), (2, "statsmodel"), (2, "pandas")
]