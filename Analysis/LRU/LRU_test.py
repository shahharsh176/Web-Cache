from LRU import *

"""
no of sites: 30
"""

for i in range(5,21):
	cache = LRUCache(length=i)
	cache.insertItem(LRUCacheItem(28))
	cache.insertItem(LRUCacheItem(11))
	cache.insertItem(LRUCacheItem(14))
	cache.insertItem(LRUCacheItem(29))

	cache.insertItem(LRUCacheItem(1))
	cache.insertItem(LRUCacheItem(2))
	cache.insertItem(LRUCacheItem(8))
	cache.insertItem(LRUCacheItem(29))

	cache.insertItem(LRUCacheItem(28))
	cache.insertItem(LRUCacheItem(29))
	cache.insertItem(LRUCacheItem(26))
	cache.insertItem(LRUCacheItem(13))

	cache.insertItem(LRUCacheItem(5))
	cache.insertItem(LRUCacheItem(14))
	cache.insertItem(LRUCacheItem(30))
	cache.insertItem(LRUCacheItem(9))

	cache.insertItem(LRUCacheItem(27))
	cache.insertItem(LRUCacheItem(15))
	cache.insertItem(LRUCacheItem(26))
	cache.insertItem(LRUCacheItem(15))


	cache.insertItem(LRUCacheItem(15))
	cache.insertItem(LRUCacheItem(1))
	cache.insertItem(LRUCacheItem(22))
	cache.insertItem(LRUCacheItem(22))

	cache.insertItem(LRUCacheItem(4))
	cache.insertItem(LRUCacheItem(27))
	cache.insertItem(LRUCacheItem(19))
	cache.insertItem(LRUCacheItem(30))

	cache.insertItem(LRUCacheItem(30))
	cache.insertItem(LRUCacheItem(20))
	cache.insertItem(LRUCacheItem(16))
	cache.insertItem(LRUCacheItem(20))

	cache.insertItem(LRUCacheItem(30))
	cache.insertItem(LRUCacheItem(10))
	cache.insertItem(LRUCacheItem(29))
	cache.insertItem(LRUCacheItem(13))

	cache.insertItem(LRUCacheItem(29))
	cache.insertItem(LRUCacheItem(22))
	cache.insertItem(LRUCacheItem(13))
	cache.insertItem(LRUCacheItem(15))


	cache.insertItem(LRUCacheItem(26))
	cache.insertItem(LRUCacheItem(18))
	cache.insertItem(LRUCacheItem(26))
	cache.insertItem(LRUCacheItem(8))

	cache.insertItem(LRUCacheItem(6))
	cache.insertItem(LRUCacheItem(22))
	cache.insertItem(LRUCacheItem(2))
	cache.insertItem(LRUCacheItem(6))

	cache.insertItem(LRUCacheItem(7))
	cache.insertItem(LRUCacheItem(24))
	cache.insertItem(LRUCacheItem(15))
	cache.insertItem(LRUCacheItem(9))

	cache.insertItem(LRUCacheItem(24))
	cache.insertItem(LRUCacheItem(12))
	cache.insertItem(LRUCacheItem(14))
	cache.insertItem(LRUCacheItem(6))

	cache.insertItem(LRUCacheItem(18))
	cache.insertItem(LRUCacheItem(9))
	cache.insertItem(LRUCacheItem(17))
	cache.insertItem(LRUCacheItem(12))


	cache.insertItem(LRUCacheItem(18))
	cache.insertItem(LRUCacheItem(28))
	cache.insertItem(LRUCacheItem(6))
	cache.insertItem(LRUCacheItem(22))

	cache.insertItem(LRUCacheItem(10))
	cache.insertItem(LRUCacheItem(27))
	cache.insertItem(LRUCacheItem(27))
	cache.insertItem(LRUCacheItem(6))

	cache.insertItem(LRUCacheItem(19))
	cache.insertItem(LRUCacheItem(17))
	cache.insertItem(LRUCacheItem(17))
	cache.insertItem(LRUCacheItem(1))

	cache.insertItem(LRUCacheItem(19))
	cache.insertItem(LRUCacheItem(23))
	cache.insertItem(LRUCacheItem(8))
	cache.insertItem(LRUCacheItem(24))

	cache.insertItem(LRUCacheItem(27))
	cache.insertItem(LRUCacheItem(10))
	cache.insertItem(LRUCacheItem(17))
	cache.insertItem(LRUCacheItem(21))


	cache.insertItem(LRUCacheItem(22))
	cache.insertItem(LRUCacheItem(12))
	cache.insertItem(LRUCacheItem(5))
	cache.insertItem(LRUCacheItem(12))

	cache.insertItem(LRUCacheItem(27))
	cache.insertItem(LRUCacheItem(19))
	cache.insertItem(LRUCacheItem(8))
	cache.insertItem(LRUCacheItem(14))

	cache.insertItem(LRUCacheItem(2))
	cache.insertItem(LRUCacheItem(30))
	cache.insertItem(LRUCacheItem(14))
	cache.insertItem(LRUCacheItem(3))

	cache.insertItem(LRUCacheItem(27))
	cache.insertItem(LRUCacheItem(28))
	cache.insertItem(LRUCacheItem(1))
	cache.insertItem(LRUCacheItem(15))

	cache.insertItem(LRUCacheItem(4))
	cache.insertItem(LRUCacheItem(21))
	cache.insertItem(LRUCacheItem(18))
	cache.insertItem(LRUCacheItem(27))




	
	print "cache size: ",i
	hitratio()

	"""
	test 1
	cache.insertItem(LRUCacheItem(24))
	cache.insertItem(LRUCacheItem(25))
	cache.insertItem(LRUCacheItem(23))
	cache.insertItem(LRUCacheItem(24))

	cache.insertItem(LRUCacheItem(23))
	cache.insertItem(LRUCacheItem(21))
	cache.insertItem(LRUCacheItem(19))
	cache.insertItem(LRUCacheItem(4))

	cache.insertItem(LRUCacheItem(8))
	cache.insertItem(LRUCacheItem(8))
	cache.insertItem(LRUCacheItem(14))
	cache.insertItem(LRUCacheItem(20))

	cache.insertItem(LRUCacheItem(16))
	cache.insertItem(LRUCacheItem(16))
	cache.insertItem(LRUCacheItem(30))
	cache.insertItem(LRUCacheItem(20))

	cache.insertItem(LRUCacheItem(3))
	cache.insertItem(LRUCacheItem(5))
	cache.insertItem(LRUCacheItem(14))
	cache.insertItem(LRUCacheItem(17))


	cache.insertItem(LRUCacheItem(6))
	cache.insertItem(LRUCacheItem(18))
	cache.insertItem(LRUCacheItem(3))
	cache.insertItem(LRUCacheItem(25))

	cache.insertItem(LRUCacheItem(6))
	cache.insertItem(LRUCacheItem(14))
	cache.insertItem(LRUCacheItem(14))
	cache.insertItem(LRUCacheItem(9))

	cache.insertItem(LRUCacheItem(7))
	cache.insertItem(LRUCacheItem(23))
	cache.insertItem(LRUCacheItem(22))
	cache.insertItem(LRUCacheItem(9))

	cache.insertItem(LRUCacheItem(19))
	cache.insertItem(LRUCacheItem(22))
	cache.insertItem(LRUCacheItem(7))
	cache.insertItem(LRUCacheItem(17))

	cache.insertItem(LRUCacheItem(13))
	cache.insertItem(LRUCacheItem(11))
	cache.insertItem(LRUCacheItem(12))
	cache.insertItem(LRUCacheItem(14))


	cache.insertItem(LRUCacheItem(25))
	cache.insertItem(LRUCacheItem(7))
	cache.insertItem(LRUCacheItem(5))
	cache.insertItem(LRUCacheItem(3))

	cache.insertItem(LRUCacheItem(23))
	cache.insertItem(LRUCacheItem(1))
	cache.insertItem(LRUCacheItem(1))
	cache.insertItem(LRUCacheItem(16))

	cache.insertItem(LRUCacheItem(11))
	cache.insertItem(LRUCacheItem(26))
	cache.insertItem(LRUCacheItem(4))
	cache.insertItem(LRUCacheItem(13))

	cache.insertItem(LRUCacheItem(15))
	cache.insertItem(LRUCacheItem(13))
	cache.insertItem(LRUCacheItem(14))
	cache.insertItem(LRUCacheItem(8))

	cache.insertItem(LRUCacheItem(27))
	cache.insertItem(LRUCacheItem(12))
	cache.insertItem(LRUCacheItem(13))
	cache.insertItem(LRUCacheItem(1))


	cache.insertItem(LRUCacheItem(14))
	cache.insertItem(LRUCacheItem(25))
	cache.insertItem(LRUCacheItem(15))
	cache.insertItem(LRUCacheItem(1))

	cache.insertItem(LRUCacheItem(9))
	cache.insertItem(LRUCacheItem(14))
	cache.insertItem(LRUCacheItem(15))
	cache.insertItem(LRUCacheItem(5))

	cache.insertItem(LRUCacheItem(11))
	cache.insertItem(LRUCacheItem(16))
	cache.insertItem(LRUCacheItem(6))
	cache.insertItem(LRUCacheItem(20))

	cache.insertItem(LRUCacheItem(3))
	cache.insertItem(LRUCacheItem(5))
	cache.insertItem(LRUCacheItem(24))
	cache.insertItem(LRUCacheItem(27))

	cache.insertItem(LRUCacheItem(27))
	cache.insertItem(LRUCacheItem(28))
	cache.insertItem(LRUCacheItem(5))
	cache.insertItem(LRUCacheItem(5))


	cache.insertItem(LRUCacheItem(25))
	cache.insertItem(LRUCacheItem(28))
	cache.insertItem(LRUCacheItem(24))
	cache.insertItem(LRUCacheItem(17))

	cache.insertItem(LRUCacheItem(26))
	cache.insertItem(LRUCacheItem(30))
	cache.insertItem(LRUCacheItem(16))
	cache.insertItem(LRUCacheItem(5))

	cache.insertItem(LRUCacheItem(22))
	cache.insertItem(LRUCacheItem(23))
	cache.insertItem(LRUCacheItem(26))
	cache.insertItem(LRUCacheItem(7))

	cache.insertItem(LRUCacheItem(18))
	cache.insertItem(LRUCacheItem(3))
	cache.insertItem(LRUCacheItem(14))
	cache.insertItem(LRUCacheItem(18))

	cache.insertItem(LRUCacheItem(24))
	cache.insertItem(LRUCacheItem(6))
	cache.insertItem(LRUCacheItem(21))
	cache.insertItem(LRUCacheItem(12))
	"""







	"""
	test 2
	cache.insertItem(LRUCacheItem(28))
	cache.insertItem(LRUCacheItem(11))
	cache.insertItem(LRUCacheItem(14))
	cache.insertItem(LRUCacheItem(29))

	cache.insertItem(LRUCacheItem(1))
	cache.insertItem(LRUCacheItem(2))
	cache.insertItem(LRUCacheItem(8))
	cache.insertItem(LRUCacheItem(29))

	cache.insertItem(LRUCacheItem(28))
	cache.insertItem(LRUCacheItem(29))
	cache.insertItem(LRUCacheItem(26))
	cache.insertItem(LRUCacheItem(13))

	cache.insertItem(LRUCacheItem(5))
	cache.insertItem(LRUCacheItem(14))
	cache.insertItem(LRUCacheItem(30))
	cache.insertItem(LRUCacheItem(9))

	cache.insertItem(LRUCacheItem(27))
	cache.insertItem(LRUCacheItem(15))
	cache.insertItem(LRUCacheItem(26))
	cache.insertItem(LRUCacheItem(15))


	cache.insertItem(LRUCacheItem(15))
	cache.insertItem(LRUCacheItem(1))
	cache.insertItem(LRUCacheItem(22))
	cache.insertItem(LRUCacheItem(22))

	cache.insertItem(LRUCacheItem(4))
	cache.insertItem(LRUCacheItem(27))
	cache.insertItem(LRUCacheItem(19))
	cache.insertItem(LRUCacheItem(30))

	cache.insertItem(LRUCacheItem(30))
	cache.insertItem(LRUCacheItem(20))
	cache.insertItem(LRUCacheItem(16))
	cache.insertItem(LRUCacheItem(20))

	cache.insertItem(LRUCacheItem(30))
	cache.insertItem(LRUCacheItem(10))
	cache.insertItem(LRUCacheItem(29))
	cache.insertItem(LRUCacheItem(13))

	cache.insertItem(LRUCacheItem(29))
	cache.insertItem(LRUCacheItem(22))
	cache.insertItem(LRUCacheItem(13))
	cache.insertItem(LRUCacheItem(15))


	cache.insertItem(LRUCacheItem(26))
	cache.insertItem(LRUCacheItem(18))
	cache.insertItem(LRUCacheItem(26))
	cache.insertItem(LRUCacheItem(8))

	cache.insertItem(LRUCacheItem(6))
	cache.insertItem(LRUCacheItem(22))
	cache.insertItem(LRUCacheItem(2))
	cache.insertItem(LRUCacheItem(6))

	cache.insertItem(LRUCacheItem(7))
	cache.insertItem(LRUCacheItem(24))
	cache.insertItem(LRUCacheItem(15))
	cache.insertItem(LRUCacheItem(9))

	cache.insertItem(LRUCacheItem(24))
	cache.insertItem(LRUCacheItem(12))
	cache.insertItem(LRUCacheItem(14))
	cache.insertItem(LRUCacheItem(6))

	cache.insertItem(LRUCacheItem(18))
	cache.insertItem(LRUCacheItem(9))
	cache.insertItem(LRUCacheItem(17))
	cache.insertItem(LRUCacheItem(12))


	cache.insertItem(LRUCacheItem(18))
	cache.insertItem(LRUCacheItem(28))
	cache.insertItem(LRUCacheItem(6))
	cache.insertItem(LRUCacheItem(22))

	cache.insertItem(LRUCacheItem(10))
	cache.insertItem(LRUCacheItem(27))
	cache.insertItem(LRUCacheItem(27))
	cache.insertItem(LRUCacheItem(6))

	cache.insertItem(LRUCacheItem(19))
	cache.insertItem(LRUCacheItem(17))
	cache.insertItem(LRUCacheItem(17))
	cache.insertItem(LRUCacheItem(1))

	cache.insertItem(LRUCacheItem(19))
	cache.insertItem(LRUCacheItem(23))
	cache.insertItem(LRUCacheItem(8))
	cache.insertItem(LRUCacheItem(24))

	cache.insertItem(LRUCacheItem(27))
	cache.insertItem(LRUCacheItem(10))
	cache.insertItem(LRUCacheItem(17))
	cache.insertItem(LRUCacheItem(21))


	cache.insertItem(LRUCacheItem(22))
	cache.insertItem(LRUCacheItem(12))
	cache.insertItem(LRUCacheItem(5))
	cache.insertItem(LRUCacheItem(12))

	cache.insertItem(LRUCacheItem(27))
	cache.insertItem(LRUCacheItem(19))
	cache.insertItem(LRUCacheItem(8))
	cache.insertItem(LRUCacheItem(14))

	cache.insertItem(LRUCacheItem(2))
	cache.insertItem(LRUCacheItem(30))
	cache.insertItem(LRUCacheItem(14))
	cache.insertItem(LRUCacheItem(3))

	cache.insertItem(LRUCacheItem(27))
	cache.insertItem(LRUCacheItem(28))
	cache.insertItem(LRUCacheItem(1))
	cache.insertItem(LRUCacheItem(15))

	cache.insertItem(LRUCacheItem(4))
	cache.insertItem(LRUCacheItem(21))
	cache.insertItem(LRUCacheItem(18))
	cache.insertItem(LRUCacheItem(27))
	"""