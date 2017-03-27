replayer: replay.c
	gcc -g replay.c -o replay -lrt
clean:
	rm -f replay
