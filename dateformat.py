# Function reformat_date converts a date into a standard date format
# Eg: Converts 28/02/2021 to 28th February 2021

def reformat_date(date_to_be_formatted):
    dates_as_list = date_to_be_formatted.split('/')
    dates_as_list = [int(a) for i, a in enumerate(dates_as_list)]
    if dates_as_list[0] % 10 == 1:
        new_date = str(dates_as_list[0]) + "st "
    elif dates_as_list[0] % 10 == 2:
        new_date = str(dates_as_list[0]) + "nd "
    elif dates_as_list[0] % 10 == 3:
        new_date = str(dates_as_list[0]) + "rd "
    else:
        new_date = str(dates_as_list[0]) + "th "
    d = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
         9: "September", 10: "October", 11: "November", 12: "December"}
    new_date = new_date + d[dates_as_list[1]] + " "
    new_date = new_date + str(dates_as_list[2])
    return new_date


if __name__ == '__main__':
    x = input("Enter a date : ")
    print(reformat_date(x))
