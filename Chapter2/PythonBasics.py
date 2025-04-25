from collections import defaultdict, Counter
import random
from functools import partial

from prompt_toolkit.input.vt100 import raw_mode

y = apply_to_one=lambda x: x+4
my_tuple = 2, 3, 4
# pr

empty_dict = {} # Pythonic
empty_dict2 = dict()
grades = { "Joel" : 80, "Tim" : 95 } # less Pythonic
# dictionary literal
# joel_grade = grades.get("Joel", 0)
# john_grade = grades.get("John", 0)
# print(joel_grade, john_grade)
tweet = {
"user" : "joelgrus",
"text" : "Data Science is Awesome",
"retweet_count" : 100,
"hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

# print(tweet.keys()) # list of keys
# print(tweet.values()) # list of values
# print(tweet.items()) # list of (key, value) tuples

# word_counts = defaultdict(int)
# for word in ["Hi", "Hello", "How", "Hi"]:
#     word_counts[word] += 1
# print(word_counts)

# dd_list = defaultdict(list)
# dd_list[2].append(1)
# dd_list[2].append(5)
# dd_list[3].append(4)
# print(dd_list)
s ="Wikipedia[b] is a free online encyclopedia, written and maintained by a community of volunteers, known as Wikipedians, through open collaboration and the wiki software MediaWiki. Founded by Jimmy Wales and Larry Sanger on January 15, 2001, Wikipedia has been hosted since 2003 by the Wikimedia Foundation, an American nonprofit organization funded mainly by donations from readers.[2] Wikipedia is the largest and most-read reference work in history.[3".split(" ")
# c=Counter(s)
# for word, count in c.most_common(10):
#     print(word, count)
# s = ""
# first_char = s and s[0]
# print(first_char)
print(any([]))
print(all({}))

word_counts = {
    "hello": 5,
    "world": 2,
    "python": 10
}

new_sorted = sorted(word_counts.items(), key=lambda x:x[1], reverse=True)
# print(word_counts.items())
# print(new_sorted)

even_numbers = [x for x in range(5) if x % 2 == 0] # [0, 2, 4]
squares = [x * x for x in range(5)]
even_squares = [x * x for x in even_numbers] # [0, 1, 4, 9,
even_squares_an = [x * x for x in range(5) if x % 2 ==0 ]
print(even_numbers, even_squares, even_squares_an)

square_set = {x: x * x for x in range(5)}
print(square_set)
square_tuple = {x*x for x in [1, -1]}
print(square_tuple)
pairs = [(x, y) for x in range(2) for y in range(3)]
print(pairs)
increasing_pairs = [(x, y) for x in range(3) for y in range(x+1, 5)]
print(increasing_pairs)

def lazy_numbers():
    yield 1
    yield 2
    yield 3
# print(lazy_numbers())
# gen = lazy_numbers()
# print(next(gen))
# print(next(gen))
# print(next(gen))

#
# random.seed(10)
# print(random.random())
# print(random.random())
#
# random.seed(10)
# print(random.random())
# print(random.random())
# my_best_friend = random.choice(["Alice", "Bob", "Charlie"])
# print(my_best_friend)
#
# lottery_numbers = range(60)
# winning_numbers = random.sample(lottery_numbers, 6)
# print(winning_numbers)

# def exp(base, power):
#     return base ** power
# two_to_the = partial(exp, power = 2)
# print(two_to_the(3))
def double(x):
    return 2 * x
xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs]
print(twice_xs)
twice_xs_map = map(double, xs)
print(list(twice_xs_map))
twice_xs_partial = partial(map, double)
print(list(twice_xs_partial(xs)))

