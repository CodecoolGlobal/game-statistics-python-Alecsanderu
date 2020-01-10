
import reports


def get_text_for_most_played(file_name):
    return str(reports.get_most_played(file_name))


def get_text_for_sum_sold(file_name):
    return str(reports.sum_sold(file_name))


def get_text_for_selling_avg(file_name):
    return str(reports.get_selling_avg(file_name))


def get_text_for_count_logest_title(file_name):
    return str(reports.count_longest_title(file_name))


def get_text_for_date_avg(file_name):
    return str(reports.get_date_avg(file_name))


def get_text_for_game_prop(file_name):
    title = input("Please Enter Game Title: ")
    try:
        return str(reports.get_game(file_name, title))
    except ValueError:
        return "No Game Found"


def get_text_for_game_prop_gui(file_name):
    with open("title.txt", 'r') as f:
        first_line = f.readline()
    title = first_line
    try:
        return str(reports.get_game(file_name, title))
    except ValueError:
        return "No Game Found"


def get_text_for_count_grouped_by_genre(file_name):
    return str(reports.count_grouped_by_genre(file_name))


def get_text_for_count_grouped_by_genre_gui(file_name):
    text = str(reports.count_grouped_by_genre(file_name))
    return text.strip("{}").replace(",", "\n")


def get_text_for_get_date_ordered(file_name):
    return str(reports.get_date_ordered(file_name))


def get_text_for_get_date_ordered_gui(file_name):
    text = str(reports.get_date_ordered(file_name))
    return text.strip("[]").replace(",", "\n")


def main():
    try:
        import_file = input("Please Enter Database File:")
        export = "export.txt"
        with open(export, "w") as f:
            f.write(get_text_for_most_played(import_file) + "\n")
            f.write(get_text_for_sum_sold(import_file) + "\n")
            f.write(get_text_for_selling_avg(import_file) + "\n")
            f.write(get_text_for_count_logest_title(import_file) + "\n")
            f.write(get_text_for_date_avg(import_file) + "\n")
            f.write(get_text_for_game_prop(import_file) + "\n")
            f.write(get_text_for_count_grouped_by_genre(import_file) + "\n")
            f.write(get_text_for_get_date_ordered(import_file) + "\n")
    except FileNotFoundError:
        print("Wrong FileName")


if __name__ == "__main__":
    main()
