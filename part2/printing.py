import reports


def print_most_played(file_name):
    most_played = reports.get_most_played(file_name)
    print(
        f"What is the title of the most played game (i.e. sold the most copies)? {most_played}")


def print_sum_sold(file_name):
    sold = reports.sum_sold(file_name)
    print(f"How many copies have been sold total? {sold}")


def print_average_selling(file_name):
    average = reports.get_selling_avg(file_name)
    print(f"What is the average selling? {average}")


def print_count_longest_title(file_name):
    longest = reports.count_longest_title(file_name)
    print(f"How many characters long is the longest title? {longest}")


def print_date_average(file_name):
    date_average = reports.get_date_avg(file_name)
    print(f"What is the average of the release dates? {date_average}")


def print_game_properties(file_name):
    while True:
        title = input("Enter Title To See Game Properties: ")
        try:
            game_properties = reports.get_game(file_name, title)
            break
        except ValueError:
            print("No Title Found,please enter another one")
            continue
    print(f"What properties has this game? {title} \n {game_properties}")


def print_count_grouped_by_genre(file_name):
    count = reports.count_grouped_by_genre(file_name)
    print("How many games are there grouped by genre?")
    for k, v in count.items():
        print("{} : {}".format(k, v))


def print_ordered_by_date(file_name):
    ordered = "\n".join(reports.get_date_ordered(file_name))
    print(f"What is the date ordered list of the games? \n{ordered}")


def main():
    while True:
        file_name = input("Enter file name: ")
        try:
            print_most_played(file_name)
            print_sum_sold(file_name)
            print_average_selling(file_name)
            print_count_longest_title(file_name)
            print_date_average(file_name)
            print_game_properties(file_name)
            print_count_grouped_by_genre(file_name)
            print_ordered_by_date(file_name)

            break
        except FileNotFoundError:
            print("Wrong filename")
            continue


if __name__ == "__main__":
    main()
