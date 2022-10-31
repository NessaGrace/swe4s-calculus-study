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

    file_contents = open(file_name, 'r')
    file_list = []
    for line in file_contents:
        file_list.append(line.rstrip().lower())
    file_contents.close()
    return file_list
    raise FileNotFoundError('file not found')
