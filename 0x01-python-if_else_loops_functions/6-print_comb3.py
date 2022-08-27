#!/usr/bin/python3
for d1 in range(0, 9):
	for d2 in range(d1 + 1, 10):
		if d1 == 8:
			print(f"{d1:d}{d2:d}")
			break
		print(f"{d1:d}{d2:d}", end=", ")
