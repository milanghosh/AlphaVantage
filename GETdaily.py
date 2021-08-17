import requests
import unittest
import HtmlTestRunner


class Daily(unittest.TestCase):
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    def test_daily_IBM(cls):
        cls.url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=7G49VBO74SV846YD'
        cls.r = requests.get(cls.url)
        cls.data = cls.r.json()
        cls.code = cls.r.status_code

        print(cls.code)
        assert cls.code == 200, "response code doesn't match"
        assert cls.data['Meta Data']['2. Symbol'] == 'IBM'

    def test_daily_Tesco(cls):
        cls.url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSCO.LON&apikey=7G49VBO74SV846YD'
        cls.r = requests.get(cls.url)
        cls.data = cls.r.json()
        cls.code = cls.r.status_code

        print(cls.code)
        assert cls.code == 200, "response code doesn't match"
        assert cls.data['Meta Data']['2. Symbol'] == 'TSCO.LON'

    def test_daily_Shopify(cls):
        cls.url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SHOP.TRT&apikey=7G49VBO74SV846YD'
        cls.r = requests.get(cls.url)
        cls.data = cls.r.json()
        cls.code = cls.r.status_code

        print(cls.code)
        assert cls.code == 200, "response code doesn't match"
        assert cls.data['Meta Data']['2. Symbol'] == 'SHOP.TRT'

    def test_daily_GreenPower(cls):
        cls.url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GPV.TRV&apikey=7G49VBO74SV846YD'
        cls.r = requests.get(cls.url)
        cls.data = cls.r.json()
        cls.code = cls.r.status_code

        print(cls.code)
        assert cls.code == 200, "response code doesn't match"
        assert cls.data['Meta Data']['2. Symbol'] == 'GPV.TRV'

    def test_daily_invalidsymbol(cls):
        cls.url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=CarTrade&apikey=7G49VBO74SV846YD'
        cls.r = requests.get(cls.url)
        cls.data = cls.r.json()

        print(cls.data)
        assert cls.data['Error Message'] == 'Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY.', "error message doesn't match"

    def test_daily_invalidkey(cls):
        cls.url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey='
        cls.r = requests.get(cls.url)
        cls.data = cls.r.json()

        print(cls.data)
        assert cls.data['Error Message'] == 'the parameter apikey is invalid or missing. Please claim your free API key on (https://www.alphavantage.co/support/#api-key). It should take less than 20 seconds.', "error message doesn't match"


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
