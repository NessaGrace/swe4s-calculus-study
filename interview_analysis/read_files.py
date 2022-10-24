"""Processes a file as a list
    * functions_lib.file_reader - reads file contents and returns list
      of file lines
"""

import argparse

import functions_lib as fl


def main():

    parser = argparse.ArgumentParser(
                    description='process file contents, convert to list',
                    prog='read_files')

    parser.add_argument('--file_name',
                        type=str,
                        help='Name of file to be processed',
                        required=True)

    args = parser.parse_args()

    try:
        test_list = fl.file_reader(args.file_name)
    except Exception as e:
        print('Error of type ' + str(type(e)) + ' occurred')
        sys.exit(1)

    print(test_list)
    print(type(test_list))

if __name__ == '__main__':
    main()
