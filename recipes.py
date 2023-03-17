import argparse
import sys

def add_recipe():
    print('adding')

def search_recipes():
    print(user_input.search_input)

def list_recipes():
    print('listing')

def set_dir():
    global directory
    directory = user_input.setdir_input
    print('save directory set to: ' + user_input.setdir_input)


def user_input_get():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_add = subparsers.add_parser('add', help='add recipe to recipe book')
    parser_add.set_defaults(command=add_recipe)
    
    parser_search = subparsers.add_parser('search', help='search recipes')
    parser_search.add_argument('search_input', type=str)
    parser_search.set_defaults(command=search_recipes)

    parser_search = subparsers.add_parser('list', help='list all recipes')
    parser_search.set_defaults(command=list_recipes)

    parser_set_dir = subparsers.add_parser('setdir', help='set save directory')
    parser_set_dir.add_argument('setdir_input', type=str)
    parser_set_dir.set_defaults(command=set_dir)

    #displays help if no arguments are added
    if len(sys.argv) <= 1:
        sys.argv.append('--help')

    global user_input

    user_input = parser.parse_args()


user_input_get()
user_input.command()



































































