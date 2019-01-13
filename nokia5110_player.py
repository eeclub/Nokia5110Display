#!/usr/bin/env python
# -*- coding: utf-8 -*-
import imageio
import argparse

import numpy as np
import serial
from PIL import Image
from time import time

WIDTH = 84
HEIGHT = 48
BAUDRATE = 115200


def img_to_bytes(img: Image):
    thumbnail = img.resize((WIDTH, HEIGHT)).convert('1')
    matrix = np.array(thumbnail)
    data = bytes()
    for h in range(0, HEIGHT, 8):
        for w in range(WIDTH):
            bit = 0x00
            for i in range(8):
                dot = matrix[h + i, w]
                if dot:
                    continue
                bit |= 0x01 << i
            data += bit.to_bytes(1, 'big')
    assert(len(data) == WIDTH * HEIGHT / 8)
    return data


def image_bitmap(filename: str):
    img = Image.open(filename)
    data = img_to_bytes(img)
    output = ','.join(['0x{:x}'.format(b) for b in data])
    print(output)


def send_wait(conn: serial.Serial, data: bytes):
    conn.write(data)
    # read ont byte from arduino response
    conn.read()


def paly_video(port: str, filename: str):
    # open seral port
    conn = serial.Serial(port, BAUDRATE)
    # open video file
    reader = imageio.get_reader(filename, 'ffmpeg')
    start_time = time()
    for i, frame in enumerate(reader):
        if i % 4:
            continue
        frame_img = Image.fromarray(frame, 'RGB')
        send_wait(conn, img_to_bytes(frame_img))
        print('\rplay {} frame, every {:0.2f} frame per second.'.format(i, i / (time() - start_time)), end='')
    conn.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', '-t', required=True, help='[video|bitmap]')
    parser.add_argument('--port', '-p')
    parser.add_argument('--filename', '-f', required=True)
    args = parser.parse_args()
    if args.target == 'bitmap':
        return image_bitmap(args.filename)
    if args.target == 'video':
        return paly_video(args.port, args.filename)


if __name__ == "__main__":
    main()
