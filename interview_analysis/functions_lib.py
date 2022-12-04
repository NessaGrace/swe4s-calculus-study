import string
import os


def file_reader(file_name):
    """Read a text file and add contents to list by line

    Parameters:
    ----------
    file_name : string
                Name of the file to be processed

    Returns:
    --------
    file_list : list of strings
                List of text file contents by line
   """

    if type(file_name) != str:
        raise TypeError("invalid input: must be string")

    # check if error raised for empty file
    if os.path.getsize(file_name) == 0:
        raise Exception('file is empty')

    file_contents = open(file_name, 'r')
    file_list = []
    for line in file_contents:
        file_list.append(line.rstrip().lower())
    file_contents.close()
    return file_list

    raise FileNotFoundError('file not found')


def filter_by_line(big_list, filter_list):
    """Filter list contents

    Parameters:
    -----------
    big_list : list (of any type of elements)
               List to filter contents out of

    filter_list : list
                  List of elements being filtered out

    Returns:
    --------
    filtered_list : list (of any type of elements)
                    Original list with list2 filtered out
    """

    if type(big_list) != list or type(filter_list) != list:
        raise TypeError('invalid input: must be two lists')

    filtered_list = []

    for element in big_list:
        if element not in filter_list:
            filtered_list.append(element)
    return filtered_list


def sentence_splitter(sentence_list):
    """Split list of multi-word strings into list of single-word strings

    Parameters:
    -----------
    sentence_list : list of strings
                    List of multi-word strings (sentences in this case)

    Returns:
    --------
    list_of_words : list of strings
                    List of individual words contained in list1
    """

    if type(sentence_list) != list:
        raise TypeError('invalid input: must be list of strings')

    for element in sentence_list:
        if type(element) != str:
            raise TypeError('invalid input: must be list of strings')

    list_of_words = []
    for sentence in sentence_list:
        for word in sentence.split():
            list_of_words.append(word)
    return list_of_words


def remove_punctuation(words_with_punc):
    """Removes punctuation from a list of strings

    Parameters:
    -----------
    words_with_punc : list of strings
                      list of strings with punctuation

    Returns:
    --------
    list_no_punc_all : list of strings
                   list of strings with punctuation removed
    """

    if type(words_with_punc) != list:
        raise TypeError("invalid input: must be list of strings")

    for element in words_with_punc:
        if type(element) != str:
            raise TypeError('invalid input: must be list of strings')

    list_no_punc = []
    list_no_punc_all = []

    for element in words_with_punc:
        # converts Codepage 1252 encoding to Unicode UTF-8 (some
        # apostrophes in wrong format)
        encoded = element.encode('cp1252')
        decoded = encoded.decode('utf-8')
        # removes punctuation from list elements
        list_no_punc.append(decoded.translate(str.maketrans('', '', string.punctuation)))  # nopep8
    # removes new UTF-8 apostrophes (just converted from Codepage 1252,
    # these were missed by translate method)
    for element in list_no_punc:
        list_no_punc_all.append(element.replace("’", ""))

    return list_no_punc_all


def word_counter(word_list, search_list):
    """Counts how many times words from a given list are repeated in
       another list

    Parameters:
    -----------
    word_list : list
                list of words to search for and count

    search_list : list
                  list of words being searched for word list words

    Returns:
    --------
    word_counter : dictionary
                   dictionary that gives the number of times each word_list
                   word is repeated in search_list, if present
    """

    if type(word_list) != list or type(search_list) != list:
        raise TypeError("invalid input: must be two lists")

    word_counter = {}

    for word1 in word_list:
        for word2 in search_list:
            if word1 == word2:
                try:
                    word_counter[word1] += 1
                except KeyError:
                    word_counter[word1] = 1
    return word_counter


# has not been fully implemented/tested yet, will be used in future
# may need functionality added for if len(list1) != len(list2)
def compare_files(list_no_errors, list_errors):
    """Compare file contents as stored in lists for similarity

    Parameters:
    -----------
    list_no_errors : list (of any type of elements)
                     list of first file's contents (first file is error free)

    list_errors: list (of any type of elements)
           list of second file's contents (second file has errors)

    Returns:
    --------
    percent_sim : float
                  percentage of same contents between files as measured
                  by exact matches (in this case), tells how accurate
                  list_errors is
    """

    if type(list_no_errors) != list or type(list_errors) != list:
        raise TypeError('invalid input: must be two lists')

    element_matches = 0

    for element1 in list_no_errors:
        for element2 in list_errors:
            if element1 == element2:
                element_matches += 1

    percent_sim = (element_matches / len(list_errors))*100

    return percent_sim
