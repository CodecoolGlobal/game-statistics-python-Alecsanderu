import sys
import reports


def get_text_for_count_games(file_name):
    return str(reports.count_games(file_name))


def get_text_for_decide(file_name, year):
    return str(reports.decide(file_name, year))


def get_text_for_latest(file_name):
    return str(reports.get_latest(file_name))


def get_text_for_count_by_genre(file_name, genre):
    return str(reports.count_by_genre(file_name, genre))


def get_text_line_number_by_title(file_name, title):
    try:
        return str(reports.get_line_number_by_title(
            file_name, title))

    except ValueError:
        return "No game title"


def get_text_for_sorted_titles(file_name):
    return ",".join(reports.sort_abc(file_name))


def get_text_for_sorted_genres(file_name):
    return ",".join(reports.get_genres(file_name))


def get_text_for_release_date(file_name):
    try:
        return str(reports.when_was_top_sold_fps(file_name))
    except ValueError:
        return "No FPS game in database"


def get_cli_args():
    cli_args = {}
    if len(sys.argv) != 6:
        print("Please look at arguments. It should be 5")
        exit()

    cli_args["file_name_input"] = sys.argv[1]
    cli_args["target_file_name"] = sys.argv[2]
    try:
        cli_args["input_year"] = int(sys.argv[3])
    except KeyError:
        print("It should be a number")
    cli_args["input_genre"] = sys.argv[4]
    cli_args["input_title"] = sys.argv[5]

    return cli_args


def main():
    cli_args = get_cli_args()
    try:
        with open(cli_args["target_file_name"], "w") as f:
            f.write(get_text_for_count_games(
                cli_args["file_name_input"]) + "\n")
            f.write(get_text_for_decide(
                cli_args["file_name_input"], cli_args["input_year"]) + "\n")
            f.write(get_text_for_latest(cli_args["file_name_input"]) + "\n")
            f.write(get_text_for_count_by_genre(
                cli_args["file_name_input"], cli_args["input_genre"]) + "\n")
            f.write(get_text_line_number_by_title(
                cli_args["file_name_input"], cli_args["input_title"]) + "\n")
            f.write(get_text_for_sorted_titles(
                cli_args["file_name_input"]) + "\n")
            f.write(get_text_for_sorted_genres(
                cli_args["file_name_input"]) + "\n")
            f.write(get_text_for_release_date(cli_args["file_name_input"]))
    except FileNotFoundError:
        print("Wrong file name")


if __name__ == "__main__":
    main()
