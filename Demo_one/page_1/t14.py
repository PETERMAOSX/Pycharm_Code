# from collections import deque
# q = deque(['a','b','c'])
# q.append('x')
# q.appendleft('y')
# print(q)

# from collections import defaultdict
# dd = defaultdict(lambda: 'N/A')
# dd['key1'] = 'abc'
# print(dd['key1'])
# print(dd['key2'])
#默认字典的作用就是当字典的键不存在的时候，但是又不想报错所使用的一种方法
#通过defaultdict(lambda: '')

# a = lambda x: 2 * x
# print(a(3))
# print(a(3))

# from collections import Counter
# c = Counter()
# c.update('mmm')
# c.update('mmm')
# c.clear()
# c.update('MaoshaoXiong')
# print(c)