from requests_html import AsyncHTMLSession
from requests_html import HTMLSession




async def get_weather():
    r = await asession.get('https://www.wunderground.com/history/daily/KLAW/date/2023-6-13')
    print(r.html)
    data = r.html.find('tbody', first=True)
    print(data)

    r = asession.get('https://www.wunderground.com/history/daily/KLAW/date/2023-6-13')

    await r.html.arender()

if __name__=='__main__':

    url = 'https://www.wunderground.com/history/daily/KLAW/date/2023-6-13'
    s  = HTMLSession()
    response = s.get(url)
    response.html.render()

    print(response)

