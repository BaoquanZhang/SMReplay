replayer: replay.c
	gcc replay.c -o replay -lrt -lzbc
clean:
	rm -f replay
