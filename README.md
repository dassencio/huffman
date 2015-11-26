Description
===========

huffman is a small python script that compresses/decompresses text files using
Huffman's algorithm.


License
=======

All code from this project is licensed under the GPLv3. See 'LICENSE' for more.


Instructions
============

On Linux, just run:

	./huffman -c FILE.txt > FILE.bin

to compress a file and store the compressed data into FILE.bin. To decompress
a compressed file generated with this script, just run:

	./huffman -d FILE.bin > FILE_ORIG.txt


Required Libraries
==================

The bitarray library is used. On Ubuntu/Debian, you can install it with:

	sudo apt-get install python3-bitarray


Contributors & Contact Information
==================================

Diego Assencio / diego@assencio.com

