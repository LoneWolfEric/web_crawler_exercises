class DoubanSpider:

    def __init__(self):
        self.temp_url = 'https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288&_=1527613360520'




    def run(self):
        num = 0
        # start_url
        url = self.temp_url.format(num)
        # 发送请求
        # 获取相应
        # 保存数据
        # 换下一个url
