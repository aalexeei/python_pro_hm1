from urllib.parse import urlparse, parse_qs

def parse(query: str) -> dict:
    params = urlparse(query).query
    return dict(parse_qs(params))

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://test.com?test1=test&test2=test2&test3=test3') == {'test1': ['test'], 'test2': ['test2'],
                                                                            'test3': ['test3']}
    assert parse('https://test.com?test=1&test=2') == {'test': ['1', '2']}
    assert parse('https://test.com?test=1&test2') == {'test': ['1'], 'test2': ['']}
    assert parse('https://test.com?test=1&test=1') == {'test': ['1', '1']}
    assert parse('https://test.com') == {}
    assert parse('https://test.com?') == {}
    assert parse('https://test.com?test') == {'test': ['']}
    assert parse('https://test.com?test1=test&test2') == {'test1': ['test'], 'test2': ['']}
    assert parse('https://test.com?test1=test&test1=test2') == {'test1': ['test', 'test2']}
    assert parse('https://test.com?test1=&test2=test') == {'test1': [''], 'test2': ['test']}

def parse_cookie(query: str) -> dict:
    cookies = query.split(';')
    result = {}
    for cookie in cookies:
        if cookie:
            name, value = cookie.split('=')
            result[name.strip()] = value.strip()
    return result

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima;age=28;country=Russia;') == {'name': 'Dima', 'age': '28', 'country': 'Russia'}
    assert parse_cookie('name=Dima=;age=28;') == {'name': 'Dima=', 'age': '28'}
    assert parse_cookie('name=Dima;age=;') == {'name': 'Dima', 'age': ''}
    assert parse_cookie('name=Dima;age=28;name=Vasya') == {'name': 'Vasya', 'age': '28'}
    assert parse_cookie('name=Dima;age=28;name=Dima') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima;age=28;age=30') == {'name': 'Dima', 'age': '30'}
    assert parse_cookie('=Dima;age=28;') == {'': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima;=28;') == {'name': 'Dima', '': '28'}