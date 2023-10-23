def weather_show():

    import requests
    from bs4 import BeautifulSoup

    url = 'https://weather.naver.com/'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            # 접속한 웹 페이지 전체 html 코드
            soup = BeautifulSoup(response.text, 'html.parser')

            # 날씨 정보
            weather_info = soup.find('div', class_='weather_now')
            # 위치 정보
            location_info = soup.find("div", class_="location_area")

            # 현재 기온관련 정보가 담긴 태그
            temperature_element = weather_info.find('strong', class_='current')

            # 요소에서 <span class="blind"> 부분 삭제
            for span in temperature_element('span'):
                span.decompose()
            
            # 기온 정보만 추출
            temperature = temperature_element.text.strip()
            # 날씨 정보만 추출
            weather_condition = weather_condition = weather_info.find('span', class_='weather').text
            # 위치 정보만 추출
            location = location_info.find("strong", class_="location_name").text

            print(f"\n현재 위치: {location}")
            print(f"현재 날씨: {weather_condition}")
            print(f"현재 온도: {temperature}°")
        else:
            print('날씨 정보를 가져올 수 없습니다.')
    except Exception as e:
        print(f'오류 발생: {str(e)}')