#interview practise question hackerrank

import math
import os
import random
import re
import sys


class VendingMachine:
    def __init__(self, num_items, item_coins):
        self.num_items = num_items
        self.item_coins = item_coins

    def buy(self, req_items, num_coins):
        self.req_items = req_items
        self.num_coins = num_coins
        if self.req_items > self.num_items:
            return 'Not enough items in the machine'
        elif self.num_coins < (self.req_items * self.item_coins):
            return 'Not enough coins'
        elif self.req_items < self.num_items and self.num_coins > self.item_coins:
            self.num_items -= self.req_items
            self.num_coins = self.num_coins - (self.req_items * self.item_coins)
            return self.num_coins

            # Implement the VendingMachine here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')#set output path to avoid key error

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")

    fptr.close()