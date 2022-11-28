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

    file_contents = open(file_name, 'r')
    file_list = []
    for line in file_contents:
        file_list.append(line.rstrip().lower())
    file_contents.close()
    return file_list
    raise FileNotFoundError('file not found')

def filter_by_line(list1, list2):
    """Filter list contents

    Parameters:
    -----------
    list1 : list (of any type of elements)
            List to filter contents out of

    list2 : list
           List of elements being filtered out

    Returns:
    --------
    filtered_list : list (of any type of elements)
                    Original list with list2 filtered out
    """

    if type(list1) != list or type(list2) != list:
        raise TypeError('invalid input: must be two lists')

    filtered_list = []

    for element in list1:
        if element not in list2:
            filtered_list.append(element)
    return filtered_list

def sentence_splitter(list1):
    """Split list of multi-word strings into list of single-word strings

    Parameters:
    -----------
    list1 : list of strings
            List of multi-word strings (sentences in this case)

    Returns:
    --------
    list_of_words : list of strings
                    List of individual words contained in list1
    """

    if type(list1) != list:
        raise TypeError('invalid input: must be list of strings')

    for element in list1:
        if type(element) != str:
            raise TypeError('invalid input: must be list of strings')

    list_of_words = []
    for sentence in list1:
        for word in sentence.split():
            list_of_words.append(word)
    return list_of_words

def compare_files(list1, list2):
    """Compare file contents as stored in lists for similarity

    Parameters:
    -----------
    list1 : list (of any type of elements)
            list of first file's contents (first file is error free)

    list2: list (of any type of elements)
           list of second file's contents (second file has errors)

    Returns:
    --------
    percent_sim : float
                  percentage of same contents between files as measured
                  by exact matches (in this case)
    """

    if type(list1) != list or type(list2) != list:
        raise TypeError('invalid input: must be two lists')

    element_matches = 0

    for element1 in list1:
        for element2 in list2:
            if element1 == element2:
                element_matches += 1

    percent_sim = (element_matches / len(list2))*100

    return percent_sim
