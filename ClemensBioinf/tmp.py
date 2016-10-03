# #!/usr/bin/python
#
# from argparse import ArgumentParser
#
# parser = ArgumentParser(epilog='This is the epilog.', description='This is the description.', prog='PROG', usage=('USAGE'))
# #parser.epilog('This is the epilog.')
# #parser.description('This is the description.')
# #paser.prog('PROG')
# #parser.usage('USAGE')
#
# parser.add_argument('-o','--option', dest='opt', help='Option')
# parser.add_argument('input', help='User input')
#
# args = parser.parse_args()
#
# opt = args.opt
# input = args.input
#
# print(opt)
# print(input)
#
#
# parser = argparse.ArgumentParser(prog='PROG')
# parser.add_argument('--foo', action='store_true', help='foo help')
# subparsers = parser.add_subparsers(help='sub-command help')
# # create the parser for the "a" command
# parser_a = subparsers.add_parser('a', help='a help')
# parser_a.add_argument('bar', type=int, help='bar help')
# # create the parser for the "b" command
# parser_b = subparsers.add_parser('b', help='b help')
# parser_b.add_argument('--baz', choices='XYZ', help='baz help')
# # parse some argument lists
# parser.parse_args(['-h'])
# parser.parse_args(['a', '12'])
# parser.parse_args(['b', '-h'])

import re
__name__
print(re.__name__)
print(re.__file__)
print(re.__builtins__)