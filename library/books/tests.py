from django.test import TestCase

from datetime import datetime,date

deadline = date(2022, 5, 22)
dead = date.today()
# if now > deadline:
#     print("Срок сдачи проекта прошел")
# elif now.day == deadline.day and now.month == deadline.month and now.year == deadline.year:
#     print("Срок сдачи проекта сегодня")
# else:
#     period = deadline - now
#     print("Осталось {} дней".format(period.days))
print(dead)
per = deadline - dead
print(f'Осталось {per.days}')