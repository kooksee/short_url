def short_url(*url):
    """
    短链接
    :param url:
    :return:
    """
    import requests
    import ujson as json
    URL = "http://tool.chinaz.com/AjaxSeo.aspx?t=sinadwz"
    res = requests.post(URL, data={"url": "^".join(url)})
    return json.loads(res.text)


if __name__ == '__main__':
    su = short_url("https://gocn.io/question/740",
                   "https://gocn.io/question/741",
                   "https://gocn.io/question/742")
    print(su)
