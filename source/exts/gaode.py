import requests
# 从高德地图网页挖出来的API
GD_API = 'https://restapi.amap.com/v3/place/text?s=rsv3&key=8325164e247e15eea68b59e89200988b&keywords='


class GDError(Exception):
    pass


class Gaode():
    @staticmethod
    def address2dest(name):
        resp = requests.get(GD_API + name)
        pois = resp.json().get('pois', [])
        if not len(pois):
            raise GDError('unknown address')
        return pois[0].get('location')
