from covid_news_handling import news_API_request
from covid_news_handling import update_news

def test_news_API_request():
    assert news_API_request()
    assert news_API_request('Covid COVID-19 coronavirus') == news_API_request()
    data=news_API_request()
    assert isinstance(data,list)
    data=news_API_request("udghuisghdfhgfrhghujhhurghtrgbgyhurebhyrg")
    assert len(data)==0

def test_update_news():
    update_news('test')
    news1={'title':'title1',
           'content':'nice content'}
    news2={'title':'title2',
           'content':'content'}
    add=[news1,news2]
    removed=[news2]
    data=update_news(add,removed)
    assert len(data)==1
    assert data[0]== news1
