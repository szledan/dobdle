#! /usr/bin/python3 -B
# -*- coding: utf-8 -*-

import argparse
from bisect import bisect_left
import copy
import csv

def add_args(parser):
    """ Adds arguments to the parser. """
    parser.add_argument('--cards', '-c', action='store', type=int, default=55, help='Number of cards.')
    parser.add_argument('--elements', '-e', action='store', type=int, default=8, help='Number of elements on a card.')
    parser.add_argument('categories', action='store', help='List of categories')


def get_args():
    """ Parses input arguments. """
    parser = argparse.ArgumentParser()
    add_args(parser)

    return parser.parse_args()


def first_card(cats, es, strategy = 0):
    if strategy == 0:
        return [ x + 1 for x in range(es) ]


def criteria(dck, card):
    match = 0
    for e in card:
        for crd in dck:
            if bisect_left(crd, e):
                match += 1
                if match > 1:
                    return False
    return True


args = get_args()

num_cat = 0
Ks = args.cards
Es = args.elements
cats = {}
IDs = []
with open(args.categories) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        IDs.append(int(row[0]))
        cats[int(row[0])] = row[1]
        num_cat += 1

print(cats)

print("List of categories: {}, ({} rows)".format(args.categories, num_cat))
print("  IDs: {}".format(IDs))
print("Number of cards: {}".format(Ks))
print("Number of elements on a card: {}".format(Es))

card = first_card(cats, Es, 0)
print("First card: {}".format(card))
deck = [ card ]

while len(deck) < 2:#Ks:
    card = []
    ids = copy.deepcopy(IDs)

    while len(card) < Es:
        while len(ids) > 0:
                return True
            card.append(ids.pop(0))

    deck.append(card)

print("Deck: {}".format(deck))

print("Generate a set of cards...")
print("Done")
