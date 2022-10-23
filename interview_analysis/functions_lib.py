def file_reader(file_name):
    file_contents = open(file_name, 'r')
    file_list = []
    for line in file_contents:
        file_list.append(line.rstrip().lower())
    file_contents.close()
    return file_list
    raise FileNotFoundError('file not found')
