import argparse
import sys

def add_recipe():
    print('Type recipe title')

def search_recipes():
    print('searching')

def list_recipes():
    print('listing')

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

parser_add = subparsers.add_parser('add', help='add recipe to recipe book')
parser_add.set_defaults(func=add_recipe)
   
parser_search = subparsers.add_parser('search', help='search recipes')
parser_search.set_defaults(func=search_recipes)

parser_search = subparsers.add_parser('list', help='list all recipes')
parser_search.set_defaults(func=list_recipes)

if len(sys.argv) <= 1:
    sys.argv.append('--help')

options = parser.parse_args()

options.func()
































































