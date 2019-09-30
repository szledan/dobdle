#! /usr/bin/python3 -B
# -*- coding: utf-8 -*-

import argparse
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


args = get_args()

num_cat = 0
Ks = args.cards
Es = args.elements
cats = {}
with open(args.categories) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        cats[row[0]] = row[1]
        num_cat += 1

print(cats)

print("List of categories: {}, ({} rows)".format(args.categories, num_cat))
print("Number of cards: {}".format(Ks))
print("Number of elements on a card: {}".format(Es))

card = first_card(cats, Es, 0)
print("First card: {}".format(card))
deck = [ card ]

while len(deck) < Ks:
    card = []
    for x in range(1, num_cat + 1):
        for y in range(x, num_cat + 1):
            card.append(y)
                while len(card) < Es:


    deck.append(card)

print("Deck: {}".format(deck))

print("Generate a set of cards...")
print("Done")
