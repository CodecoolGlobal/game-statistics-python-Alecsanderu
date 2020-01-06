import reports


def handle_error(message):
    while True:
        try:
            result = int(input(message))
            return result
            pass
        except ValueError:
            print("Please enter a number. ")
            continue


def print_count_games(file_name):
    number_of_games = reports.count_games(file_name)
    print(f"How many games are in the file? {number_of_games}")


def print_decide(file_name):
    input_year = handle_error("Please enter Year: ")
    game_from_year = reports.decide(file_name, input_year)
    print(f"Is there a game from this year ({input_year}) ? {game_from_year}")


def print_latest(file_name):
    latest_title = reports.get_latest(file_name)
    print(f"Which was the lastest title? {latest_title}")


def print_count_by_genre(file_name):
    genre = input("Enter a genre: ")
    number_of_games = reports.count_by_genre(file_name, genre)
    print(f"How many Games do we have by genre? {genre}:{number_of_games}")


def print_line_number_by_title(file_name):
    while True:
        input_title = input("Please enter a title: ")
        try:
            line_number = reports.get_line_number_by_title(
                file_name, input_title)
            break
        except ValueError:
            print("Not existent, please enter another one!")
            continue
    print(
        f"What is the line number of the given game {input_title} ? {line_number} ")


def print_sorted_titles(file_name):
    sorted_titles = "\n".join(reports.sort_abc(file_name))
    print(
        f"What is the alphabetical ordered list of the titles?\n{sorted_titles}")


def print_sorted_genres(file_name):
    sorted_genres = "\n".join(reports.get_genres(file_name))
    print(f"What are the genres??\n{sorted_genres}")


def print_release_date(file_name):
    try:
        year_top_sold = reports.when_was_top_sold_fps(file_name)
    except ValueError:
        year_top_sold = "No FPS game in database"
    print(
        f"What is the release date of the top sold 'First-person shooter' game? {year_top_sold}")


def main():
    while True:
        file_name = input("Enter file name: ")
        try:
            print_count_games(file_name)
            print_decide(file_name)
            print_latest(file_name)
            print_count_by_genre(file_name)
            print_line_number_by_title(file_name)
            print_sorted_titles(file_name)
            print_sorted_genres(file_name)
            print_release_date(file_name)

            break
        except FileNotFoundError:
            print("Wrong filename")
            continue


if __name__ == "__main__":
    main()
