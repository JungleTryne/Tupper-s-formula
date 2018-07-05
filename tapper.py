#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
from argparse import ArgumentParser
import logging

_SIZE_WIDTH = 106
_SIZE_HEIGHT = 17
_SQ = _SIZE_HEIGHT * _SIZE_WIDTH


def get_image(chosen_k, chosen_image_path):
    def from_k_to_bin(k):
        k //= _SIZE_HEIGHT
        binary = bin(k)[2:].rjust(_SQ, '0')
        result = [[] for i in range(_SIZE_HEIGHT)]
        for x in range(_SQ):
            result[x % _SIZE_HEIGHT].append(binary[x])
        result.reverse()
        return result

    if chosen_k is None:
        logging.error('Undefined k')
        return

    lists = from_k_to_bin(chosen_k)

    #-----Drawing-----#
    image = Image.new("1", (_SIZE_WIDTH, _SIZE_HEIGHT), (0))
    for y in range(_SIZE_HEIGHT):
        for x in range(_SIZE_WIDTH):
            xy = (_SIZE_WIDTH - x - 1, _SIZE_HEIGHT - y - 1)
            image.putpixel(xy=xy, value=(int(lists[y][x]),))

    #-----Saving-----#
    if chosen_image_path is None:
        chosen_image_path = 'result.png'

    image.save(chosen_image_path)
    logging.debug('Image has generated')
    return chosen_image_path


def get_k(chosen_image_path):
    if chosen_image_path is None:
        logging.error('Undefined image path')
    try:
        image = Image.open(chosen_image_path)
    except:
        logging.error('Image error')
        return

    if image.size != (_SIZE_WIDTH, _SIZE_HEIGHT):
        logging.error("An image has to be 106х17")
        return

    #-----Counting-----#
    image = image.convert('1')
    byteset = ""
    for x in range(_SIZE_WIDTH - 1, -1, -1):
        for y in range(_SIZE_HEIGHT):
            byte = str(image.getpixel((x, y)))
            byteset += str(int(byte == '255'))
    k = int(byteset, 2) * 17

    logging.debug('k has counted')
    return k


def main():
    #-----Parsing arguments-----#
    parser = ArgumentParser(
        description='Script for generating image from \'k\' \
and getting \'k\' from image \
using Tapper\'s formula'
    )

    parser.add_argument(
        '--type',
        type=str,
        default=None,
        help="set type: 'gen' or 'count'",
    )
    parser.add_argument(
        '--k',
        type=int,
        default=None,
        help="set k to generate image",
    )
    parser.add_argument(
        '--path',
        type=str,
        default=None,
        help="set image path to get k",
    )
    parser.add_argument(
        '-o',
        type=str,
        default=None,
        help="set path for generated image",
    )
    chosen_type = parser.parse_args().type
    chosen_k = parser.parse_args().k

    #-----Setting logging level-----#
    logging.root.setLevel(logging.INFO)

    if not chosen_type:
        logging.info('Use --help')
        logging.error('Undefined type')
        return

    #-----Choose type-----#
    if chosen_type == 'count':
        chosen_image_path = parser.parse_args().path
        result = get_k(chosen_image_path)
    elif chosen_type == 'gen':
        chosen_image_path = parser.parse_args().o
        result = get_image(chosen_k, chosen_image_path)

    #-----Returning result-----#
    print(result)


if __name__ == '__main__':
    main()
