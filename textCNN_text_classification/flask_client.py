# -*- coding: utf-8 -*-
'''
@Time    : 2019
@Author  : ZHOU, YANG
@Contact : yzhou0000@gmail.com
'''

import requests


def get_pred_results(texts):
    """得到新闻文本的预测类别。

    Parameters
    ----------
        texts: list[str], 原始文本
    Returns
    -------
        res.text: str, 各个文本的类别，形式为"['体育', '娱乐', ...]"
    """
    target_url = 'http://xxx.xx.x.xx:5000/'  # ip address
    texts = texts.encode('utf-8')
    res = requests.post(target_url, data=texts)
    # res = requests.get(target_url)  # 将被拒绝
    return res.text


# example
texts = "['北京时间6月16日，荷兰的斯海尔托亨博斯传来好消息，2019年射箭世锦赛男子团体反曲弓决赛中，\
    由魏绍轩、冯浩、丁倚亮这三名年轻人组成的中国队发挥出色，以6-2战胜印度队夺得冠军！这是中国队首次摘\
    得射箭世锦赛的男团金牌，创造历史！此前，魏绍轩、冯浩和丁倚亮组成的中国队在1/4决赛中6-2战胜了\
    澳大利亚队。半决赛中国男队6-2战胜了实力强大的韩国队。印度队半决赛5-4战胜了东道主荷兰队。\
    在铜牌战中，韩国队5-3击败了荷兰，获得季军。此前的女团比赛，由郑怡钗、孟凡旭和安琦轩组\
    成的中国女队在铜牌战中4-5不敌英国，获得第四名。决赛中，中国台北队6-2力克韩国队，\
    历史首次夺得世锦赛女团冠军。通过此次世锦赛，中国男女队已经拿到了东京奥运会满额入场券。', \
    '北京时间6月17日，率领猛龙队夺得NBA总冠军后，尼克-纳斯\
    夏天的工作仍未结束。他透露，自己将率领加拿大男篮征战在中国进行的世界杯。51岁的纳斯自曝自己非常\
    期待这份工作，2012年的伦敦奥运会，他曾作为英国男篮的助教参加。纳斯说：“那次经历让我学到很多，我\
    期待这次执教也有这种结果。”目前在NBA征战的加拿大球员众多，贾马尔-穆雷、特里斯坦-汤普森、德怀特-鲍威\
    尔和今年的热门新秀RJ-巴雷特都来自加拿大。本文来自：NBA官网']"
print(get_pred_results(texts))
