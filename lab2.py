def display_main_menu():
    print("Enter some numbers separated by commas(e.g. 5,67,32)")

def calc_average():
    print("calc_average")


def get_user_input():
    lists = input()
    lists = list(lists.split(","))
    return lists

def calc_average_temperature(num_list):
    y = 0
    for x in num_list:
        y = float(x) + float(y)
    average = y / len(num_list)
    print(average)

def calc_min_max_temperature(num_list):
    firstloop =0
    for x in num_list:
        if firstloop == 0:
            max = x
            min = x
            firstloop = 1
        if float(x) > float(max):
            max = x
        if float(x) < float(min):
            min = x
    list_min_max = [min,max]
    return(list_min_max)

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average_temperature(num_list)
    calc_min_max_temperature(num_list)

if __name__ == "__main__":
    main()
