import math


def get_lists(file_name):
    table = []
    with open(file_name) as f:
        for line in f:
            index = line.strip().split("\t")
            index_named = {
                "INDEX_NAME": index[0],
                "INDEX_COPIES": index[1],
                "INDEX_YEAR": index[2],
                "INDEX_GENRE": index[3],
                "INDEX_COMPANY": index[4],
            }
            table.append(index_named)
    return table


def get_most_played(file_name):
    table = get_lists(file_name)
    copies = float(table[0]["INDEX_COPIES"])
    title = table[0]["INDEX_NAME"]
    for row in table:
        actual_copies = float(row["INDEX_COPIES"])
        if actual_copies > copies:
            copies = actual_copies
            title = row["INDEX_NAME"]
    return title


def sum_sold(file_name):
    return sum([float(row["INDEX_COPIES"]) for row in get_lists(file_name)])


def get_selling_avg(file_name):
    return sum_sold(file_name) / len(get_lists(file_name))


def count_longest_title(file_name):
    return max([len(row["INDEX_NAME"]) for row in get_lists(file_name)])


def get_date_avg(file_name):
    years_sum = sum(int(row["INDEX_YEAR"]) for row in get_lists(file_name))
    years_average = math.ceil(years_sum / len(get_lists(file_name)))
    return years_average


def get_game(file_name, title):
    properties = []
    for row in get_lists(file_name):
        if row["INDEX_NAME"] == title:
            properties.append(row["INDEX_NAME"])
            properties.append(float(row["INDEX_COPIES"]))
            properties.append(int(row["INDEX_YEAR"]))
            properties.append(row["INDEX_GENRE"])
            properties.append(row["INDEX_COMPANY"])
            return properties
    raise ValueError("This game does not exist")


def count_grouped_by_genre(file_name):
    cbg = {}
    for row in get_lists(file_name):
        cbg[row["INDEX_GENRE"]] = cbg.get(row["INDEX_GENRE"], 0) + 1
    return cbg


def get_date_ordered_A(file_name):
    table = get_lists(file_name)

    table.sort(key=lambda row: row["INDEX_NAME"])
    table.sort(key=lambda row: row["INDEX_YEAR"], reverse=True)

    return [row["INDEX_TITLE"] for row in table]


def get_date_ordered(file_name):
    table = get_lists(file_name)
    for row in table:
        for i in range(len(table) - 1):
            actual = int(table[i]["INDEX_YEAR"])
            next = int(table[i + 1]["INDEX_YEAR"])
            if actual < next or (actual == next and table[i]["INDEX_NAME"] > table[i+1]["INDEX_NAME"]):
                table[i], table[i + 1] = table[i + 1], table[i]
    return [row["INDEX_NAME"] for row in table]
