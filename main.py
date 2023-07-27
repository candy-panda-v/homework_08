import datetime

users = [
        {'name': 'Bill', 'birthday': datetime.datetime(1987,1,23)},
        {'name': 'Jill', 'birthday': datetime.datetime(1991,2,1)},
        {'name': 'Jack', 'birthday': datetime.datetime(1978,4,8)},
        {'name': 'Kevin', 'birthday': datetime.datetime(1986,4,21)},
        {'name': 'Victoria', 'birthday': datetime.datetime(1964,7,30)},
        {'name': 'Taylor', 'birthday': datetime.datetime(1989,5,1)},
        {'name': 'Bishop', 'birthday': datetime.datetime(1992,5,3)},
        {'name': 'Piter', 'birthday': datetime.datetime(1985,5,16)},
        {'name': 'James', 'birthday': datetime.datetime(1989,7,29)},
        {'name': 'Shanon', 'birthday': datetime.datetime(1989,7,29)}
          ]


WEEKDAYS = dict(Monday = [], 
                  Tuesday = [],
                  Wednesday = [],
                  Thursday = [],
                  Friday = [],
                  Saturday = [],
                  Sunday = [])


week_after = (datetime.datetime.now() + datetime.timedelta(days=7)).date()


def get_birthday_day(user):
    dt = user['birthday']
    new_dt = datetime.datetime(datetime.datetime.now().year, dt.month, dt.day)
    return new_dt


def get_weekday(user):
    return user['birthday'].strftime("%A")


def get_birthdays_per_week(users):
    for user in users:
        if get_birthday_day(user) > datetime.datetime.now() and get_birthday_day(user).date() < week_after:
            if get_weekday(user) in ['Saturday', 'Sunday']:
                WEEKDAYS['Monday'].append(user['name'])
            else:
                WEEKDAYS[get_weekday(user)].append(user['name'])
    for day, value in WEEKDAYS.items():
        if len(value)>0:
            print('{:<15} : {:<100} '.format(day, ', '.join(value)))


if __name__ == '__main__':
    get_birthdays_per_week(users)