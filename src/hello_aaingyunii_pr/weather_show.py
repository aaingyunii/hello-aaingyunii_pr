def weather_show():

    import requests
    from bs4 import BeautifulSoup

    url = 'https://weather.naver.com/'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            weather_info = soup.find('div', class_='weather_now')

            temperature_element = weather_info.find('strong', class_='current')
            # 요소에서 <span class="blind"> 부분 삭제
            for span in temperature_element('span'):
                span.decompose()
                
            temperature = temperature_element.text.strip()
            weather_condition = weather_condition = weather_info.find('span', class_='weather').text
            
            print(f"\n현재 날씨: {weather_condition}")
            print(f"현재 온도: {temperature}°")
        else:
            print('날씨 정보를 가져올 수 없습니다.')
    except Exception as e:
        print(f'오류 발생: {str(e)}')