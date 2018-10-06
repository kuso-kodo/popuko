import math

import pendulum
from none import *


@on_command('yearprogress')
async def year_progress(session: CommandSession):
    await session.send(get_year_progress())


def get_year_progress():
    dt = pendulum.now()
    percent = year_progress(dt)
    year = dt.year
    return f'你的 {year} 使用进度：%{percent}\n' \
           f'\n\n' \
           f'{make_progress_string(percent)}'


def year_progress(dt):
    year_days = 366 if dt.is_leap_year() else 365
    passed_days = dt.timetuple().tm_yday
    percent = math.floor((passed_days / year_days) * 100)
    return percent


def make_progress_string(percent):
    blocks = 15
    percent = percent * blocks / 100
    return ''.join(["▓" if i < percent else "░" for i in range(blocks)])
