from LFU import *

"""
no of sites: 30
"""
for i in range(5,21):
	cache = LFUCache(i)
	cache.insertItem(28)
	cache.insertItem(11)
	cache.insertItem(14)
	cache.insertItem(29)

	cache.insertItem(1)
	cache.insertItem(2)
	cache.insertItem(8)
	cache.insertItem(29)

	cache.insertItem(28)
	cache.insertItem(29)
	cache.insertItem(26)
	cache.insertItem(13)

	cache.insertItem(5)
	cache.insertItem(14)
	cache.insertItem(30)
	cache.insertItem(9)

	cache.insertItem(27)
	cache.insertItem(15)
	cache.insertItem(26)
	cache.insertItem(15)


	cache.insertItem(15)
	cache.insertItem(1)
	cache.insertItem(22)
	cache.insertItem(22)

	cache.insertItem(4)
	cache.insertItem(27)
	cache.insertItem(19)
	cache.insertItem(30)

	cache.insertItem(30)
	cache.insertItem(20)
	cache.insertItem(16)
	cache.insertItem(20)

	cache.insertItem(30)
	cache.insertItem(10)
	cache.insertItem(29)
	cache.insertItem(13)

	cache.insertItem(29)
	cache.insertItem(22)
	cache.insertItem(13)
	cache.insertItem(15)


	cache.insertItem(26)
	cache.insertItem(18)
	cache.insertItem(26)
	cache.insertItem(8)

	cache.insertItem(6)
	cache.insertItem(22)
	cache.insertItem(2)
	cache.insertItem(6)

	cache.insertItem(7)
	cache.insertItem(24)
	cache.insertItem(15)
	cache.insertItem(9)

	cache.insertItem(24)
	cache.insertItem(12)
	cache.insertItem(14)
	cache.insertItem(6)

	cache.insertItem(18)
	cache.insertItem(9)
	cache.insertItem(17)
	cache.insertItem(12)


	cache.insertItem(18)
	cache.insertItem(28)
	cache.insertItem(6)
	cache.insertItem(22)

	cache.insertItem(10)
	cache.insertItem(27)
	cache.insertItem(27)
	cache.insertItem(6)

	cache.insertItem(19)
	cache.insertItem(17)
	cache.insertItem(17)
	cache.insertItem(1)

	cache.insertItem(19)
	cache.insertItem(23)
	cache.insertItem(8)
	cache.insertItem(24)

	cache.insertItem(27)
	cache.insertItem(10)
	cache.insertItem(17)
	cache.insertItem(21)


	cache.insertItem(22)
	cache.insertItem(12)
	cache.insertItem(5)
	cache.insertItem(12)

	cache.insertItem(27)
	cache.insertItem(19)
	cache.insertItem(8)
	cache.insertItem(14)

	cache.insertItem(2)
	cache.insertItem(30)
	cache.insertItem(14)
	cache.insertItem(3)

	cache.insertItem(27)
	cache.insertItem(28)
	cache.insertItem(1)
	cache.insertItem(15)

	cache.insertItem(4)
	cache.insertItem(21)
	cache.insertItem(18)
	cache.insertItem(27)

	
	print "Cache size: ",i
	hitratio()

	"""
	test 1
	cache.insertItem(24)
	cache.insertItem(25)
	cache.insertItem(23)
	cache.insertItem(24)

	cache.insertItem(23)
	cache.insertItem(21)
	cache.insertItem(19)
	cache.insertItem(4)

	cache.insertItem(8)
	cache.insertItem(8)
	cache.insertItem(14)
	cache.insertItem(20)

	cache.insertItem(16)
	cache.insertItem(16)
	cache.insertItem(30)
	cache.insertItem(20)

	cache.insertItem(3)
	cache.insertItem(5)
	cache.insertItem(14)
	cache.insertItem(17)


	cache.insertItem(6)
	cache.insertItem(18)
	cache.insertItem(3)
	cache.insertItem(25)

	cache.insertItem(6)
	cache.insertItem(14)
	cache.insertItem(14)
	cache.insertItem(9)

	cache.insertItem(7)
	cache.insertItem(23)
	cache.insertItem(22)
	cache.insertItem(9)

	cache.insertItem(19)
	cache.insertItem(22)
	cache.insertItem(7)
	cache.insertItem(17)

	cache.insertItem(13)
	cache.insertItem(11)
	cache.insertItem(12)
	cache.insertItem(14)


	cache.insertItem(25)
	cache.insertItem(7)
	cache.insertItem(5)
	cache.insertItem(3)

	cache.insertItem(23)
	cache.insertItem(1)
	cache.insertItem(1)
	cache.insertItem(16)

	cache.insertItem(11)
	cache.insertItem(26)
	cache.insertItem(4)
	cache.insertItem(13)

	cache.insertItem(15)
	cache.insertItem(13)
	cache.insertItem(14)
	cache.insertItem(8)

	cache.insertItem(27)
	cache.insertItem(12)
	cache.insertItem(13)
	cache.insertItem(1)


	cache.insertItem(14)
	cache.insertItem(25)
	cache.insertItem(15)
	cache.insertItem(1)

	cache.insertItem(9)
	cache.insertItem(14)
	cache.insertItem(15)
	cache.insertItem(5)

	cache.insertItem(11)
	cache.insertItem(16)
	cache.insertItem(6)
	cache.insertItem(20)

	cache.insertItem(3)
	cache.insertItem(5)
	cache.insertItem(24)
	cache.insertItem(27)

	cache.insertItem(27)
	cache.insertItem(28)
	cache.insertItem(5)
	cache.insertItem(5)


	cache.insertItem(25)
	cache.insertItem(28)
	cache.insertItem(24)
	cache.insertItem(17)

	cache.insertItem(26)
	cache.insertItem(30)
	cache.insertItem(16)
	cache.insertItem(5)

	cache.insertItem(22)
	cache.insertItem(23)
	cache.insertItem(26)
	cache.insertItem(7)

	cache.insertItem(18)
	cache.insertItem(3)
	cache.insertItem(14)
	cache.insertItem(18)

	cache.insertItem(24)
	cache.insertItem(6)
	cache.insertItem(21)
	cache.insertItem(12)
	"""






	"""
	test 2
	cache.insertItem(28)
	cache.insertItem(11)
	cache.insertItem(14)
	cache.insertItem(29)

	cache.insertItem(1)
	cache.insertItem(2)
	cache.insertItem(8)
	cache.insertItem(29)

	cache.insertItem(28)
	cache.insertItem(29)
	cache.insertItem(26)
	cache.insertItem(13)

	cache.insertItem(5)
	cache.insertItem(14)
	cache.insertItem(30)
	cache.insertItem(9)

	cache.insertItem(27)
	cache.insertItem(15)
	cache.insertItem(26)
	cache.insertItem(15)


	cache.insertItem(15)
	cache.insertItem(1)
	cache.insertItem(22)
	cache.insertItem(22)

	cache.insertItem(4)
	cache.insertItem(27)
	cache.insertItem(19)
	cache.insertItem(30)

	cache.insertItem(30)
	cache.insertItem(20)
	cache.insertItem(16)
	cache.insertItem(20)

	cache.insertItem(30)
	cache.insertItem(10)
	cache.insertItem(29)
	cache.insertItem(13)

	cache.insertItem(29)
	cache.insertItem(22)
	cache.insertItem(13)
	cache.insertItem(15)


	cache.insertItem(26)
	cache.insertItem(18)
	cache.insertItem(26)
	cache.insertItem(8)

	cache.insertItem(6)
	cache.insertItem(22)
	cache.insertItem(2)
	cache.insertItem(6)

	cache.insertItem(7)
	cache.insertItem(24)
	cache.insertItem(15)
	cache.insertItem(9)

	cache.insertItem(24)
	cache.insertItem(12)
	cache.insertItem(14)
	cache.insertItem(6)

	cache.insertItem(18)
	cache.insertItem(9)
	cache.insertItem(17)
	cache.insertItem(12)


	cache.insertItem(18)
	cache.insertItem(28)
	cache.insertItem(6)
	cache.insertItem(22)

	cache.insertItem(10)
	cache.insertItem(27)
	cache.insertItem(27)
	cache.insertItem(6)

	cache.insertItem(19)
	cache.insertItem(17)
	cache.insertItem(17)
	cache.insertItem(1)

	cache.insertItem(19)
	cache.insertItem(23)
	cache.insertItem(8)
	cache.insertItem(24)

	cache.insertItem(27)
	cache.insertItem(10)
	cache.insertItem(17)
	cache.insertItem(21)


	cache.insertItem(22)
	cache.insertItem(12)
	cache.insertItem(5)
	cache.insertItem(12)

	cache.insertItem(27)
	cache.insertItem(19)
	cache.insertItem(8)
	cache.insertItem(14)

	cache.insertItem(2)
	cache.insertItem(30)
	cache.insertItem(14)
	cache.insertItem(3)

	cache.insertItem(27)
	cache.insertItem(28)
	cache.insertItem(1)
	cache.insertItem(15)

	cache.insertItem(4)
	cache.insertItem(21)
	cache.insertItem(18)
	cache.insertItem(27)
	"""