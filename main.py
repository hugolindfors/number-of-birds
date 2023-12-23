def main():
    while True:
        current_year = 0
        start_number_of_birds = number_of_birds = int(input("How many birds are there this year? "))
        change_rate = float(input("At what rate are they in/decreasing? "))

        if change_rate > 1:
            while (number_of_birds < 2 * start_number_of_birds):
                current_year += 1
                number_of_birds *= change_rate

            print(f"The number of birds is doubled after {current_year} years.")
            
        elif change_rate < 1:
            while (number_of_birds > 0.5 * start_number_of_birds):
                current_year += 1
                number_of_birds *= change_rate

            print(f"The number of birds is halved after {current_year} years.")


if __name__ == "__main__":
    main()