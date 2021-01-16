# myrandom.py with default and custom random functions
import random

def random_1d():
   """This function get a random number between 0 and 9"""
   return random.randint(0,9)

def random_2d():
   """This function get a random number between 10 and 99"""
   return random.randint(10,99)

def get_random(lower, upper):
   """This function get a random number between lower and upper"""
   return random.randint(lower,upper)