################################################################################
#
#    Copyright (c) 2015, Diego Assencio (http://diego.assencio.com)
#    All rights reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################


"""An implementation of Huffman's algorithm."""


import heapq
from bitarray import bitarray
from collections import Counter


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
			return bitarray()
		elif self.left is not None and symbol in self.left.symbol:
			return bitarray([0]) + self.left.symbol_to_bitarray(symbol)
		elif self.right is not None and symbol in self.right.symbol:
			return bitarray([1]) + self.right.symbol_to_bitarray(symbol)
		else:
			raise ValueError("symbol %s not in tree" % symbol)


def huffman(text):

	"""
	Computes the optimal variable-length encoding of the input text using
	Huffman's algorithm and returns the obtained encoding as a dictionary
	(symbol -> bitstring).
	"""

	if len(text) == 0:
		return dict()

	# count the number of occurrences of each character on text
	W = Counter(text)

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
