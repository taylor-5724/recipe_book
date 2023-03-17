import argparse
import sys

def add_recipe():
    print('adding')

def search_recipes():
    print(options.search_input)

def list_recipes():
    print('listing')

def set_dir():
    print(options.setdir_input)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

parser_add = subparsers.add_parser('add', help='add recipe to recipe book')
parser_add.set_defaults(func=add_recipe)
   
parser_search = subparsers.add_parser('search', help='search recipes')
parser_search.add_argument('search_input', type=str)
parser_search.set_defaults(func=search_recipes)

parser_search = subparsers.add_parser('list', help='list all recipes')
parser_search.set_defaults(func=list_recipes)

parser_set_dir = subparsers.add_parser('setdir', help='set save directory')
parser_set_dir.add_argument('setdir_input', type=str)
parser_set_dir.set_defaults(func=set_dir)

if len(sys.argv) <= 1:
    sys.argv.append('--help')

options = parser.parse_args()

options.func()
































































