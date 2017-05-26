[![Build Status](https://travis-ci.org/dassencio/huffman.svg?branch=master)](https://travis-ci.org/dassencio/huffman)

Description
===========

`huffman` is a script (written in Python 3) which compresses/decompresses
text files using
[Huffman's algorithm](http://diego.assencio.com/?index=36c4c02124a10282d8a0f92277a43ec4).


License
=======

All code from this project is licensed under the GPLv3. See the
[`LICENSE`](https://github.com/dassencio/huffman/tree/master/LICENSE)
file for more information.


Required modules
================

The `bitarray` module is used. On Ubuntu/Debian, you can install it with the
following command:

	sudo apt-get install python3-bitarray


Usage instructions
==================

Run:

	./huffman -c file.txt > file.bin

to compress a file called `file.txt` and store the compressed data (in binary
format) into `file.bin`. To decompress a compressed file generated with this
script, run:

	./huffman -d file.bin > file_original.txt


Contributors & contact information
==================================

Diego Assencio / diego@assencio.com

