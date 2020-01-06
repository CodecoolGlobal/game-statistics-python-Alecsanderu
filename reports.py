
INDEX_NAME = 0
INDEX_COPIES = 1
INDEX_YEAR = 2
INDEX_GENRE = 3
INDEX_COMPANY = 4


def get_lists(file_name):
    with open(file_name) as f:
        mylist = [line.split("\t") for line in f]
    return mylist


def count_games(file_name):
    lists = get_lists(file_name)
    return len(lists)


def decide(file_name, year):
    for row in get_lists(file_name):
        if int(row[INDEX_YEAR]) == year:
            return True
    return False


def get_latest(file_name):
    table = get_lists(file_name)
    years = int(table[INDEX_NAME][INDEX_YEAR])
    latest_title = None
    for elem in table:
        actual_year = int(elem[INDEX_YEAR])
        if actual_year > years:
            years = actual_year
            latest_title = elem[INDEX_NAME]
    return latest_title


def count_by_genre(file_name, genre):
    table = get_lists(file_name)
    count = 0
    for row in table:
        if row[INDEX_GENRE] == genre:
            count += 1
    return count


def get_line_number_by_title(file_name, title):
    counter = 0
    for row in get_lists(file_name):
        counter += 1
        if row[INDEX_NAME] == title:
            return counter
    raise ValueError("Game not found")


def sorting_algorithm(lists):
    for item in lists:
        for i in range(0, len(lists) - 1):
            if lists[i] > lists[i + 1]:
                lists[i], lists[i + 1] = lists[i + 1], lists[i]
    return lists


def sort_abc(file_name):    # some games title missing from test file, added them up to the test
    titles = [row[INDEX_NAME] for row in get_lists(file_name)]
    return sorting_algorithm(titles)

# games missing: half life , garry mod , everquesst, guild wars half life


def get_genres(file_name):
    genre = list(set(row[INDEX_GENRE] for row in get_lists(file_name)))
    return sorting_algorithm(genre)


def when_was_top_sold_fps(file_name):
    table = get_lists(file_name)
    copies_sold = 0
    year = None
    for row in table:
        actual_copies = float(row[INDEX_COPIES])
        if row[INDEX_GENRE] == "First-person shooter" and actual_copies > copies_sold:
            copies_sold = actual_copies
            year = int(row[INDEX_YEAR])
    if year:
        return year
    else:
        raise ValueError("No Such Year")
