import os
import sys
import urllib.request
import pygame
from urllib.request import urlopen
import urllib.parse
import pandas as pd
from bs4 import BeautifulSoup


def get_page(url):
    html_string = url
    soup = BeautifulSoup(urlopen(html_string), 'lxml')  # Parse the HTML as a string
    return soup

def get_text():
    url = "http://weather.naver.com/rgn/townWetr.nhn?naverRgnCd=02131107"
    soup = get_page(url)
    w_now = soup.findAll("div", {"class": "w_now2"})  # 날짜별 url
    wether = w_now[0].find_all('li')

    li = w_now[0].find_all('li')[0]
    current_time = li.find('h5').get_text() #'20시 현재'
    temperature = li.find('em').get_text().replace("\n", "").replace("\t", "").replace("\r", "") #'6℃맑음'
    temperature = "온도는 " + temperature.replace("℃", "도입니다. 날씨는 ") + "이며,"

    weather = wether[0].getText().replace("\n", "").replace("\t", "").replace("\r", "").split("미세먼지")[0]
    weather  = weather .replace("℃", "도").replace("|", "").replace("도", "도 ").replace("-", "마이너스").replace("mm", "미리")

    pm10 = wether[0].find_all('a')[0]
    pm10 = pm10.get_text().replace("\n", "").replace("도움말", "")
    dust = pm10.split("오존")[0].replace("미세먼지", " 미세먼지는 ")

    text = current_time + temperature + dust + " 입니다."

    return text


def convert_textTomp3(txt):
    client_id = "Zeo_nwjkCps3cGq_0LSa"
    client_secret = "jRbn4kxYMw"


    encText = urllib.parse.quote(txt)
    data = "speaker=jinho&speed=0&text=" + encText;
    url = "https://openapi.naver.com/v1/voice/tts.bin"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()

    if(rescode==200):
        print("TTS mp3 저장")
        response_body = response.read()
        with open('대기.mp3', 'wb') as f:
            f.write(response_body)
    else:
        print("Error Code:" + rescode)


def play_mp3():
    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load('/home/pi/Desktop/대기.mp3')
    clock = pygame.time.Clock()
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        clock.tick(1000)


