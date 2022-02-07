import os
import shutil
import subprocess
import time
from datetime import date, timedelta

import ffmpeg
from selenium.webdriver import Chrome


def take_screenshot(driver, url, img_path):
    driver.get(url)
    print(url)
    time.sleep(10)
    return driver.save_screenshot(img_path)


def date_to_url(day):
    if isinstance(day, date):
        return f"https://smellpgh.org/visualization?share=true&date={day.strftime('%Y%m%d')}&zoom=11&latLng=40.394,-79.914&city_id=1"

    return f"https://smellpgh.org/visualization?share=true&date={day}&zoom=11&latLng=40.394,-79.914&city_id=1"


def take_screenshots_smellpgh():
    driver = Chrome("Driver/chromedriver.exe")
    start_date = date(2021, 1, 1)
    end_date = date(2021, 12, 31)
    while start_date <= end_date:
        url = date_to_url(start_date)
        take_screenshot(driver, url, f'Imgs/{start_date.strftime("%Y%m%d")}.png')
        start_date += timedelta(days=1)
    # ffmpeg.input('Imgs/202112%02d.png', pattern_type='sequence', framerate=1).output('movie.mp4').run(cmd='ffmpeg/bin/ffmpeg')


def create_video():
    start_date = date(2021, 1, 1)
    end_date = date(2021, 12, 31)
    file_names = []
    i = 0
    while start_date <= end_date:
        shutil.copy(f'Imgs/{start_date.strftime("%Y%m%d")}.png', f'{i}.png')
        i = i + 1
        start_date += timedelta(days=1)
    try:
        os.unlink('movie.mp4')
    except:
        pass

    subprocess.check_call([
        "ffmpeg\\bin\\ffmpeg.exe",
        "-framerate",
        "3",
        "-i",
        "%d.png",
        "-vf",
        "scale=1280x800",
        "-pix_fmt",
        "yuv420p",
        "movie.mp4"
    ])
    # ffmpeg.input("%d.png").output('movie.mp4').run(cmd='ffmpeg/bin/ffmpeg')

start_date = date(2021, 12, 31,)