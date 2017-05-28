"""An implementation of Huffman's algorithm."""

import bitarray
import collections
import heapq

################################################################################

class huffman_tree():

	def __init__(self, symbol, weight, left=None, right=None):
		self.symbol = symbol
		self.weight = weight
		self.left   = left
		self.right  = right

	def __lt__(self, right):
		return self.weight < right.weight

	def symbol_to_bitarray(self, symbol):
		if symbol == self.symbol:
			return bitarray.bitarray()
		elif self.left is not None and symbol in self.left.symbol:
			return bitarray.bitarray([0]) + \
			       self.left.symbol_to_bitarray(symbol)
		elif self.right is not None and symbol in self.right.symbol:
			return bitarray.bitarray([1]) + \
			self.right.symbol_to_bitarray(symbol)
		else:
			raise ValueError("symbol %s not in tree" % symbol)

################################################################################

def huffman(text):

	"""
	Computes the optimal variable-length encoding of the input text using
	Huffman's algorithm and returns the obtained encoding as a dictionary
	(symbol -> bitstring).
	"""

	if len(text) == 0:
		return dict()

	# count the number of occurrences of each character on text
	W = collections.Counter(text)

	if len(W) == 1:
		return huffman_tree(symbols[0], weights[0])

	# initial step: if we have n symbols, create n single-node trees
	trees = []
	for symbol,weight in W.items():
		trees.append(huffman_tree(symbol,weight))

	# turn the list trees into a min-heap
	heapq.heapify(trees)

	# at each step, merge the two trees with smallest weights
	while len(trees) > 1:
		# merge t1 and t2, insert merged tree on trees
		t1 = heapq.heappop(trees)
		t2 = heapq.heappop(trees)
		symbol = t1.symbol + t2.symbol
		weight = t1.weight + t2.weight
		tm = huffman_tree(symbol, weight, t1, t2)
		heapq.heappush(trees, tm)

	# return the optimal symbol -> bitarray mapping
	return { c:trees[0].symbol_to_bitarray(c) for c in W.keys() }
