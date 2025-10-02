def get_absolute_url(url, *args, **kwargs):

    if args:
        url += '/' + '/'.join(str(arg) for arg in args)

    if kwargs:
        url += '?'
        parameters = [f"{key}={value}" for key, value in kwargs.items()]
        url += '&'.join(parameters)

    return url


print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))
