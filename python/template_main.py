#!/usr/bin/env python3

import argparse


def run(input_fname):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='fill me')
    parser.add_argument(
        'input',
        type=str,
        metavar='FILE',
        help='input file')

    args = parser.parse_args()

    run(args.input)
