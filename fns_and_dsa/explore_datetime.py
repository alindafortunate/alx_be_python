import datetime


def display_current_datetime():
    """prints the curremt date"""
    current_date = datetime.datetime.now()
    print(
        f"Current date and time: {current_date.year}-{current_date.month}-{current_date.day} {current_date.hour}:{current_date.minute}:{current_date.second}"
    )


display_current_datetime()

number_of_days = int(
    input("Enter the number of days to add to the current date: ").strip()
)


def calculate_future_date():
    future_date = datetime.datetime.now() + datetime.timedelta(days=number_of_days)
    print(f"Future date: {future_date.year}-{future_date.month}-{future_date.day}")


calculate_future_date()
