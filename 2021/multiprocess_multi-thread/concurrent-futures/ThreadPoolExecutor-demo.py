# coding=utf-8
import concurrent.futures
import urllib.request


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    URLS = ['https://translate.google.cn/', 'https://www.google.com']
    future_to_url = {}
    for url in URLS:
        future = executor.submit(load_url, url, 60)
        future_to_url[future] = url

    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print("%r generated an exception: %s" % (url, exc))
        else:
            print("%r page is %d bytes" % (url, len(data)))
