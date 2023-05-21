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
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age'