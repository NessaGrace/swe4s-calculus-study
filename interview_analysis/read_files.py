"""Run linear or binary search (based on user input) with toy data
    * utils.linear_search - performs linear search on data
    * utils.index_list - returns list of indices
    * utils.binary_search - performs binary search on data
"""

import argparse
import statistics

import utils


def main():

    parser = argparse.ArgumentParser(
                    description='run linear or binary search based on type',
                    prog='search')

    parser.add_argument('--search_type',
                        type=str,
                        help='Type of search (linear or binary)',
                        required=True)

    args = parser.parse_args()

    toy_data = ['A', 'B', 'C', 'D', 'E']

    toy_search_key = 'A'

    test_list = []
    for i in range(20):
        test_list.extend([[1, 2, 3, 4], [5, 6, 7, 8]])

    L1 = statistics.mean([1, 2, 3, 4])
    L2 = statistics.mean([5, 6, 7, 8])
    t = min(L1, L2)
    groups = []
    for i in range(40):
        groups.append("Group " + str(i))

    try:
        if args.search_type == 'linear'.lower():
            index = utils.linear_search(toy_search_key, toy_data)

        elif args.search_type == 'binary'.lower():
            struc_list = utils.index_list(toy_data)
            index = utils.binary_search(toy_search_key, struc_list)

        print(index)

        test_lst_trim, groups = utils.mean_threshold(test_list, t, groups)

        print(test_lst_trim, groups)

    except Exception as e:
        print('Error of type ' + type(e) + ' occurred')
        sys.exit(1)


if __name__ == '__main__':
    main()
