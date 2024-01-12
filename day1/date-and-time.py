from datetime import datetime
from datetime import date
from datetime import timedelta


def main():
    todaydate = date.today()
    christmas = date(2024, 12, 25)

    if todaydate == christmas:
        print ("Yey, it's Christmas")
    else:
        print(f"Time left to Christmas: {str((christmas - todaydate).days)}")

    today = datetime.today()
    eta = timedelta(hours=16)
    future_time = today + eta
    formatted_future_time = future_time.strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_future_time)

if __name__ == "__main__":
    main()
