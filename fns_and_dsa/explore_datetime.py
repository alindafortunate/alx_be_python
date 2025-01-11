from datetime import datetime, timedelta


def display_current_datetime():
    """prints the curremt date"""
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(
        # f"Current date and time: {current_date.year}-{current_date.month}-{current_date.day} {current_date.hour}:{current_date.minute}:{current_date.second}"
    )
    print(f"Current date and time: {current_date}")


display_current_datetime()

number_of_days = int(
    input("Enter the number of days to add to the current date: ").strip()
)


def calculate_future_date():
    future_date = datetime.now() + timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")


calculate_future_date()
