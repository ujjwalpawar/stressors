# Makefile for mac_stressor

CC = gcc
CFLAGS = -w
SRC = mac_stressor.c
OUT = mac_stressor

all: $(OUT)

$(OUT): $(SRC)
	$(CC) $< -o $@

clean:
	rm -f $(OUT)

.PHONY: all clean
