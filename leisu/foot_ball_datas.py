import time
import requests
import threading
from lxml import etree
from queue import Queue
from urllib import request
from pymongo import MongoClient
from url_list import ball_url_list

"""
足球数据库中，全世界一共有796场赛事，其中国家级的585场
此爬虫负责爬取这585个页面结构相同的赛事所有数据
"""


class Football_Spider(threading.Thread):
    def __init__(self, i, url_queue):
        threading.Thread.__init__(self)
        self.i = i
        self.url_queue = url_queue

    def run(self):
        while True:
            # 线程停止条件：
            if self.url_queue.empty():
                break
            else:
                url = self.url_queue.get()
                self.request_url(url=url)

    def request_url(self, url):

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Cookie': 'acw_tc=2f61f27715659367240011846e651b914ed0c7a99d76ef0c9d440ba21363a8; Hm_lvt_63b82ac6d9948bad5e14b1398610939a=1566046696,1566755927,1566915294,1566950414; PHPSESSID=674sldbst08r6uv7npah9ma150; SERVERID=4ab2f7c19b72630dd03ede01228e3e61|1567096735|1567093076; Hm_lpvt_63b82ac6d9948bad5e14b1398610939a=1567096740',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        }
        response = requests.get(url=url).content.decode('utf-8')
        tree = etree.HTML(response)

        # 联赛名
        league_matches_name = ''.join(tree.xpath('//div[@class="clearfix-row f-s-24"]/text()'))
        print(league_matches_name)
        data_lists = []
        datas_football = {'{}'.format(league_matches_name): data_lists}
        # 获取球队球员信息

        all_team = tree.xpath('//div[@id="select-team-one"]/div/ul/li[not(@class="active")]')

        for li in all_team:
            team_id = ''.join(li.xpath('./@data-id'))
            team_name = ''.join(li.xpath('./a/text()')).replace(".", "-")
            team_url = 'http://data.leisu.com/team-' + team_id
            team_response = requests.get(url=team_url, headers=headers).content.decode('utf-8')
            team_tree = etree.HTML(team_response)
            # 1、先获取球队信息
            # 球队市值
            team_price = ''.join(team_tree.xpath('//div[@ class="mask"]/span/text()'))
            # 所属联赛
            in_team = ''.join(team_tree.xpath('//ul[@class="info-data"]/li[1]/span[2]/text()'))
            # 成立时间
            create_time = ''.join(team_tree.xpath('//ul[@class="info-data"]/li[2]/span[2]/text()'))
            # 球场
            ball_park = ''.join(team_tree.xpath('//ul[@class="info-data"]/li[3]/span[2]/text()'))
            # 容量
            capacity = ''.join(team_tree.xpath('//ul[@class="info-data"]/li[4]/span[2]/text()'))
            # 更多
            more = ''.join(team_tree.xpath('//div[@class="trophy-list"]/a/@href'))

            # print(team_name,team_id,team_price,in_team,create_time,ball_park,capacity,more)

            # 2、赛程赛果：可以从历年的数据中获取到
            # 3、球队阵容
            # 主教练
            chief_coach = ''.join(team_tree.xpath('//div[@class="float-right m-t-9 m-r-12 color-999 f-s-12"]/text()'))
            team_data_list = []
            team_datas = {'{}球队信息'.format(team_name): team_data_list}

            aa_data = {
                'id': team_id,
                '主教练': chief_coach,
                '球队市值': team_price,
                '所属联赛': in_team,
                '成立时间': create_time,
                '球场': ball_park,
                '容量': capacity,
                '更多': more
            }

            team_data_list.append(aa_data)

            team_div_list = team_tree.xpath('//div[@class="clearfix-row bd-box m-t-16"]')
            for div in team_div_list:
                team_title = ''.join(div.xpath('.//div[@class="title-tip float-left m-t-16"]/text()'))
                # print(team_title)
                td_list = div.xpath('.//tr[not(@class="color-999")]')

                if team_title == '球队阵容':
                    for td in td_list:
                        # 号码
                        num = ''.join(td.xpath('./td[1]/text()')).strip()
                        # 球员
                        player = ''.join(td.xpath('./td[2]/a/span[1]/text()')).strip()
                        # 出生日
                        birthdy = ''.join(td.xpath('./td[3]/text()')).strip()
                        # 身高(cm)
                        height = ''.join(td.xpath('./td[4]/text()')).strip()
                        # 体重(kg)
                        weight = ''.join(td.xpath('./td[5]/text()')).strip()
                        # 位置
                        where = ''.join(td.xpath('./td[6]/text()')).strip()
                        # 国籍
                        national = ''.join(td.xpath('./td[7]/span/text()')).strip()
                        # 进球
                        goal = ''.join(td.xpath('./td[8]/text()')).strip()
                        # 助攻
                        assist = ''.join(td.xpath('./td[9]/text()')).strip()
                        # 红牌
                        red_card = ''.join(td.xpath('./td[10]/text()')).strip()
                        # 黄牌
                        yellow_card = ''.join(td.xpath('./td[11]/text()')).strip()
                        # 球员信息链接
                        player_url = ''.join(td.xpath('./td[2]/a/@href')).strip()

                        qiudui_zhenrong = {'球队阵容': {'号码': num, '球员': player, '出生日': birthdy, '身高(cm)': height,
                                                    '体重(kg)': weight, '位置': where, '国籍': national, '进球': goal,
                                                    '助攻': assist, '红牌': red_card, '黄牌': yellow_card, '球员链接': player_url
                                                    }}
                        team_data_list.append(qiudui_zhenrong)
                        # print(qiudui_zhenrong)

                elif team_title == '转入球员':
                    for td in td_list:
                        # 转入时间
                        come_time = ''.join(td.xpath('./td[1]/text()')).strip()
                        # 球员
                        come_player = ''.join(td.xpath('./td[2]/a/span[1]/text()')).strip()
                        # 位置
                        come_place = ''.join(td.xpath('./td[3]/text()')).strip()
                        # 来自
                        come_from = ''.join(td.xpath('./td[4]/span/text()')).strip()
                        # 类型
                        come_type = ''.join(td.xpath('./td[5]/text()')).strip()
                        # 球员链接
                        player_url = ''.join(td.xpath('./td[2]/a/@href')).strip()
                        zhuanru_qiuyuan = {"转入球员": {'转入时间': come_time, '球员': come_player, '位置': come_place,
                                                    '来自': come_from, '类型': come_type, '球员链接': player_url}}
                        team_data_list.append(zhuanru_qiuyuan)
                        # print(zhuanru_qiuyuan)

                elif team_title == '转出球员':
                    for td in td_list:
                        # 转出时间
                        go_time = ''.join(td.xpath('./td[1]/text()')).strip()
                        # 球员
                        go_player = ''.join(td.xpath('./td[2]/a/span[1]/text()')).strip()
                        # 位置
                        go_place = ''.join(td.xpath('./td[3]/text()')).strip()
                        # 来自
                        go_out = ''.join(td.xpath('./td[4]/span/text()')).strip()
                        # 类型
                        go_type = ''.join(td.xpath('./td[5]/text()')).strip()
                        # 球员链接
                        player_url = ''.join(td.xpath('./td[2]/a/@href')).strip()
                        zhuanchu_qiuyuan = {"转出球员": {'转出时间': go_time, '球员': go_player, '位置': go_place,
                                                     '去向': go_out, '类型': go_type, '球员链接': player_url}}
                        team_data_list.append(zhuanchu_qiuyuan)
                        # print(zhuanchu_qiuyuan)

                elif team_title == '进球分布':
                    # 总进球
                    all_title = ''.join(
                        div.xpath('.//div[@id="goal-all"]/div[@class="clearfix-row m-t-10 m-b-18"]/span/text()'))
                    min_15_goal = ''.join(
                        div.xpath('.//div[@id="goal-all"]//div[@class="s-count"]/div/div/span[1]/text()'))
                    min_30_goal = ''.join(
                        div.xpath('.//div[@id="goal-all"]//div[@class="s-count"]/div/div/span[2]/text()'))
                    min_45_goal = ''.join(
                        div.xpath('.//div[@id="goal-all"]//div[@class="s-count"]/div/div/span[3]/text()'))
                    min_60_goal = ''.join(
                        div.xpath('.//div[@id="goal-all"]//div[@class="s-count"]/div/div/span[4]/text()'))
                    min_75_goal = ''.join(
                        div.xpath('.//div[@id="goal-all"]//div[@class="s-count"]/div/div/span[5]/text()'))
                    min_90_goal = ''.join(
                        div.xpath('.//div[@id="goal-all"]//div[@class="s-count"]/div/div/span[6]/text()'))
                    # 总失球
                    min_15_fumble = ''.join(
                        div.xpath('.//div[@id="goal-all"]//div[@class="s-count m-t-4"]/div/div/span[1]/text()'))
                    min_30_fumble = ''.join(
                        div.xpath('.//div[@id="goal-all"]//div[@class="s-count m-t-4"]/div/div/span[2]/text()'))
                    min_45_fumble = ''.join(
                        div.xpath('.//div[@id="goal-all"]//div[@class="s-count m-t-4"]/div/div/span[3]/text()'))
                    min_60_fumble = ''.join(
                        div.xpath('.//div[@id="goal-all"]//div[@class="s-count m-t-4"]/div/div/span[4]/text()'))
                    min_75_fumble = ''.join(
                        div.xpath('.//div[@id="goal-all"]//div[@class="s-count m-t-4"]/div/div/span[5]/text()'))
                    min_90_fumble = ''.join(
                        div.xpath('.//div[@id="goal-all"]//div[@class="s-count m-t-4"]/div/div/span[6]/text()'))
                    # 主场
                    # 主场进球
                    home_title = ''.join(
                        div.xpath('.//div[@id="goal-home"]/div[@class="clearfix-row m-t-10 m-b-18"]/span/text()'))
                    min_15_home = ''.join(
                        div.xpath('.//div[@id="goal-home"]//div[@class="s-count"]/div/div/span[1]/text()'))
                    min_30_home = ''.join(
                        div.xpath('.//div[@id="goal-home"]//div[@class="s-count"]/div/div/span[2]/text()'))
                    min_45_home = ''.join(
                        div.xpath('.//div[@id="goal-home"]//div[@class="s-count"]/div/div/span[3]/text()'))
                    min_60_home = ''.join(
                        div.xpath('.//div[@id="goal-home"]//div[@class="s-count"]/div/div/span[4]/text()'))
                    min_75_home = ''.join(
                        div.xpath('.//div[@id="goal-home"]//div[@class="s-count"]/div/div/span[5]/text()'))
                    min_90_home = ''.join(
                        div.xpath('.//div[@id="goal-home"]//div[@class="s-count"]/div/div/span[6]/text()'))
                    # 主场失球
                    fumble_home = ''.join(div.xpath(
                        './/div[@id="goal-home"]/div[@class="s-count m-t-4"]//span[@class="count color-fdc487"]/text()'))
                    home_fumle_15 = ''.join(
                        div.xpath('.//div[@id="goal-home"]//div[@class="s-count m-t-4"]/div/div/span[1]/text()'))
                    home_fumle_30 = ''.join(
                        div.xpath('.//div[@id="goal-home"]//div[@class="s-count m-t-4"]/div/div/span[2]/text()'))
                    home_fumle_45 = ''.join(
                        div.xpath('.//div[@id="goal-home"]//div[@class="s-count m-t-4"]/div/div/span[3]/text()'))
                    home_fumle_60 = ''.join(
                        div.xpath('.//div[@id="goal-home"]//div[@class="s-count m-t-4"]/div/div/span[4]/text()'))
                    home_fumle_75 = ''.join(
                        div.xpath('.//div[@id="goal-home"]//div[@class="s-count m-t-4"]/div/div/span[5]/text()'))
                    home_fumle_90 = ''.join(
                        div.xpath('.//div[@id="goal-home"]//div[@class="s-count m-t-4"]/div/div/span[6]/text()'))
                    # 客场
                    #  客场进球
                    away_title = ''.join(
                        div.xpath('.//div[@id="goal-away"]/div[@class="clearfix-row m-t-10 m-b-18"]/span/text()'))
                    min_15_away = ''.join(
                        div.xpath('.//div[@id="goal-away"]//div[@class="s-count"]/div/div/span[1]/text()'))
                    min_30_away = ''.join(
                        div.xpath('.//div[@id="goal-away"]//div[@class="s-count"]/div/div/span[2]/text()'))
                    min_45_away = ''.join(
                        div.xpath('.//div[@id="goal-away"]//div[@class="s-count"]/div/div/span[3]/text()'))
                    min_60_away = ''.join(
                        div.xpath('.//div[@id="goal-away"]//div[@class="s-count"]/div/div/span[4]/text()'))
                    min_75_away = ''.join(
                        div.xpath('.//div[@id="goal-away"]//div[@class="s-count"]/div/div/span[5]/text()'))
                    min_90_away = ''.join(
                        div.xpath('.//div[@id="goal-away"]//div[@class="s-count"]/div/div/span[6]/text()'))
                    # 客场失球
                    fumble_away = ''.join(div.xpath(
                        './/div[@id="goal-away"]/div[@class="s-count m-t-4"]//span[@class="count color-fdc487"]/text()'))
                    away_fumle_15 = ''.join(
                        div.xpath('.//div[@id="goal-away"]//div[@class="s-count m-t-4"]/div/div/span[1]/text()'))
                    away_fumle_30 = ''.join(
                        div.xpath('.//div[@id="goal-away"]//div[@class="s-count m-t-4"]/div/div/span[2]/text()'))
                    away_fumle_45 = ''.join(
                        div.xpath('.//div[@id="goal-away"]//div[@class="s-count m-t-4"]/div/div/span[3]/text()'))
                    away_fumle_60 = ''.join(
                        div.xpath('.//div[@id="goal-away"]//div[@class="s-count m-t-4"]/div/div/span[4]/text()'))
                    away_fumle_75 = ''.join(
                        div.xpath('.//div[@id="goal-away"]//div[@class="s-count m-t-4"]/div/div/span[5]/text()'))
                    away_fumle_90 = ''.join(
                        div.xpath('.//div[@id="goal-away"]//div[@class="s-count m-t-4"]/div/div/span[6]/text()'))

                    jinqiu_fenbu = {'总进球{}'.format(all_title): [{'进球数': {'00-15': min_15_goal, '15-30': min_30_goal,
                                                                         '30-45': min_45_goal, '45-60': min_60_goal,
                                                                         '60-75': min_75_goal, '75-90': min_75_goal}},
                                                                {'失球数': {'00-15': min_15_fumble, '15-30': min_30_fumble,
                                                                         '30-45': min_45_fumble, '45-60': min_60_fumble,
                                                                         '60-75': min_75_fumble,
                                                                         '75-90': min_75_fumble}}],
                                    '主场{}'.format(home_title): [{'进球数': {'00-15': min_15_home, '15-30': min_30_home,
                                                                         '30-45': min_45_home, '45-60': min_60_home,
                                                                         '60-75': min_75_home, '75-90': min_90_home}},
                                                                {'失球数': {'00-15': home_fumle_15, '15-30': home_fumle_30,
                                                                         '30-45': home_fumle_45, '45-60': home_fumle_60,
                                                                         '60-75': home_fumle_75,
                                                                         '75-90': home_fumle_90}}],
                                    '客场{}'.format(away_title): [{'进球数': {'00-15': min_15_away, '15-30': min_30_away,
                                                                         '30-45': min_45_away, '45-60': min_60_away,
                                                                         '60-75': min_75_away, '75-90': min_90_away}},
                                                                {'失球数': {'00-15': away_fumle_15, '15-30': away_fumle_30,
                                                                         '30-45': away_fumle_45, '45-60': away_fumle_60,
                                                                         '60-75': away_fumle_75,
                                                                         '75-90': away_fumle_90}}],
                                    }

                    team_data_list.append(jinqiu_fenbu)

                    # print(jinqiu_fenbu)

                elif team_title == '球队简介':
                    team_intro = ''.join(div.xpath('.//div[@class="display-b p-l-16 p-r-16 p-b-8"]/text()'))
                    qiudui_jianjie = {'球队简介': team_intro}
                    team_data_list.append(qiudui_jianjie)
                    # print(qiudui_jianjie)
                else:
                    pass
            data_lists.append(team_datas)

        year_list = (tree.xpath('//div[@class="select-border"]/div[@class="down"]/ul[@class="max max-h-374"]/li'))
        for li in year_list:
            year = li.xpath('./a/text()')[0]  # 赛事年份
            href = li.xpath('./a/@href')[0]  # 对应年份的连接
            year_url = request.urljoin(base_url, href)  # 拼接url
            # print(year_url,year)
            # 1、获取到对应年份的赛事页面
            year_response = requests.get(url=year_url, headers=headers).content.decode('utf-8')
            year_tree = etree.HTML(year_response)

            # 2、获取对应年份赛事介绍
            cpt_tent = []
            cpt = {'{}年'.format(year): cpt_tent}
            competition = year_tree.xpath('//ul[@class="head-list"]/li[not(@class="clearfix-row")]')
            for li in competition:
                data_cpt = li.xpath('./text()')[0]
                cpt_tent.append(data_cpt)
            # print(cpt)#赛事介绍，球队联盟市值简介

            # 3、判断赛程不同的玩法，有的为空，有的有联赛，争霸赛
            stages = year_tree.xpath('//div[@id="stages-nav"]/a')
            if not stages:  # 如果没有标签，表示联赛没有打完
                # 4、获取赛程赛果
                year_table = year_tree.xpath('//table[@class="table-tow matches"]/tr[not(@class="th")]')
                for tr in year_table:
                    # 轮次
                    game_round = ''.join(tr.xpath('./td/span[@class="rank"]/text()'))
                    # 时间
                    game_time = '/'.join(tr.xpath('./td/span[@class="display-i-b text-a-l"]/text()'))
                    # 主队
                    home_team = ''.join(tr.xpath('./td[3]/a//text()'))
                    # 比分,未开始为VS
                    game_score = ''.join(tr.xpath('./td/a[@class="link-black"]//text()'))
                    # 客队
                    visiting_team = ''.join(tr.xpath('./td[5]/a//text()'))
                    # 让球(全场/半场)
                    concede_points = ''.join(tr.xpath('./td[6]/div//text()'))
                    # 进球数/(全场/半场)
                    goals_for = ''.join(tr.xpath('./td[7]/div//text()'))
                    # 数据分析
                    game_analyze = ''.join(tr.xpath('./td[8]/a[1]/@href'))
                    # 数据指数
                    game_index = ''.join(tr.xpath('./td[8]/a[2]/@href'))

                    cpt_01 = [{'联赛': [{'轮次': game_round}, {'时间': game_time}, {'主队': home_team}, {'比分(半场)': game_score},
                                      {'客队': visiting_team}, {'让球(全场/半场)': concede_points}, {'进球数/(全场/半场)': goals_for},
                                      {'数据分析': game_analyze}, {'数据指数': game_index}]}]
                    cpt_tent.append(cpt_01)
                    # print(cpt_01)
                    # my_football_set.insert(cpt_01)#入库

            else:
                for a in stages:
                    stage = ''.join(a.xpath('./text()')).replace(".", "-")
                    data_id = ''.join(a.xpath('./@data-id'))
                    # print(stage,data_id)
                    old_table = year_tree.xpath(
                        '//table[@class="table-tow matches"]/tr[@data-stage="{}"]'.format(data_id))
                    for tr in old_table:
                        # 轮次
                        game_round = ''.join(tr.xpath('./td/span[@class="rank"]/text()'))
                        # 时间
                        game_time = '/'.join(tr.xpath('./td/span[@class="display-i-b text-a-l"]/text()'))
                        # 主队
                        home_team = ''.join(tr.xpath('./td[3]/a//text()'))
                        # 比分,未开始为VS
                        game_score = ''.join(tr.xpath('./td/a[@class="link-black"]//text()'))
                        # 客队
                        visiting_team = ''.join(tr.xpath('./td[5]/a//text()'))
                        # 让球(全场/半场)
                        concede_points = ''.join(tr.xpath('./td[6]/div//text()'))
                        # 进球数/(全场/半场)
                        goals_for = ''.join(tr.xpath('./td[7]/div//text()'))
                        # 数据分析
                        game_analyze = ''.join(tr.xpath('./td[8]/a[1]/@href'))
                        # 数据指数
                        game_index = ''.join(tr.xpath('./td[8]/a[2]/@href'))
                        cpt_01 = [{'{}'.format(stage): [{'轮次': game_round}, {'时间': game_time}, {'主队': home_team},
                                                        {'比分(半场)': game_score},
                                                        {'客队': visiting_team}, {'让球(全场/半场)': concede_points},
                                                        {'进球数/(全场/半场)': goals_for},
                                                        {'数据分析': game_analyze}, {'数据指数': game_index}]}]
                        cpt_tent.append(cpt_01)
                        # print(cpt_01)
                        # my_football_set.insert(cpt_01)#入库

            # 5、获取总积分榜，每轮的积分榜可以通过上边赛程赛果求出
            league_list = year_tree.xpath('//tr[@class="data pd-8"]')
            for tr in league_list:
                # 球队排名
                team_ranking = ''.join(tr.xpath('./td[1]/span/text()'))
                # 球队名称
                team_name = ''.join(tr.xpath('./td[2]/a/span/text()'))
                # 场次
                session = ''.join(tr.xpath('./td[3]/text()'))
                # 胜
                success = ''.join(tr.xpath('./td[4]/text()'))
                # 平
                flat = ''.join(tr.xpath('./td[5]/text()'))
                # 负
                lose = ''.join(tr.xpath('./td[6]/text()'))
                # 进球
                goal = ''.join(tr.xpath('./td[7]/text()'))
                # 失球
                fumble = ''.join(tr.xpath('./td[8]/text()'))
                # 净胜球
                goal_dif = ''.join(tr.xpath('./td[9]/text()'))
                # 场均进球
                arg_goal = ''.join(tr.xpath('./td[10]/text()'))
                # 场均失球
                arg_fumble = ''.join(tr.xpath('./td[11]/text()'))
                # 场均净胜
                arg_gold_dif = ''.join(tr.xpath('./td[12]/text()'))
                # 积分
                integral = ''.join(tr.xpath('./td[13]/text()'))

                league_table = {
                    '总积分榜': [{'排名': team_ranking}, {'球队': team_name}, {'场次': session}, {'胜': success}, {'平': flat},
                             {'负': lose},
                             {'进球': goal}, {'失球': fumble}, {'净胜球': goal_dif}, {'场均进球': arg_goal}, {'场均失球': arg_fumble},
                             {'场均净胜': arg_gold_dif}, {'积分': integral}]}
                #
                cpt_tent.append(league_table)
                # print(league_table)

            # 获取球队球员数据（射手榜，助攻榜，球员防守，球队数据）
            # 射手榜
            shoot_list = year_tree.xpath('//div[@class="clearfix-row table-page goals"]/table/tr[@class="pd-8"]')
            if not shoot_list:
                shoot_data = {'射手榜': "暂无数据"}
                cpt_tent.append(shoot_data)
                # print(shoot_data)
            else:
                for tr in shoot_list:
                    player_ranking = ''.join(tr.xpath('./td[1]/span/text()'))
                    player = ''.join(tr.xpath('./td[2]/a/span/text()'))
                    player_team = ''.join(tr.xpath('./td[3]/a/span/text()'))
                    player_nationality = ''.join(tr.xpath('./td[4]/span/text()'))
                    session = ''.join(tr.xpath('./td[5]/text()'))
                    playing_time = ''.join(tr.xpath('./td[6]/text()'))
                    goal_penalty = ''.join(tr.xpath('./td[7]/text()'))
                    goal_time = ''.join(tr.xpath('./td[8]/text()'))
                    shoot_data = {'射手榜': [{'排名': player_ranking}, {'球员': player}, {'球队': player_team},
                                          {'国籍': player_nationality}, {'场次(替补)': session}, {'出场时间': playing_time},
                                          {'进球(点球)': goal_penalty}, {'进球耗时(分)': goal_time}]}
                    cpt_tent.append(shoot_data)

                    # print(shoot_data)

            # 助攻榜
            assist_list = year_tree.xpath(
                '//div[@class="clearfix-row table-page assists hide"]/table/tr[@class="pd-8"]')
            if not assist_list:
                assist_data = {'助攻榜': '暂无数据'}
                cpt_tent.append(assist_data)
                # print(assist_data)
            else:
                for tr in assist_list:
                    assist_ranking = ''.join(tr.xpath('./td[1]/span/text()'))
                    assist_player = ''.join(tr.xpath('./td[2]/a/span/text()'))
                    assist_team = ''.join(tr.xpath('./td[3]/a/span/text()'))
                    assist_nationality = ''.join(tr.xpath('./td[4]/span/text()'))
                    pass_num = ''.join(tr.xpath('./td[5]/text()'))
                    key_pass = ''.join(tr.xpath('./td[6]/text()'))
                    assist_num = ''.join(tr.xpath('./td[7]/text()'))
                    assist_data = {'助攻榜': [{'排名': assist_ranking}, {'球员': assist_player}, {'球队': assist_team},
                                           {'国籍': assist_nationality},
                                           {'传球次数': pass_num}, {'关键传球': key_pass}, {'助攻': assist_num}]}
                    cpt_tent.append(assist_data)
                    # print(assist_data)

            # 球员防守
            defend_list = year_tree.xpath(
                '//div[@class="clearfix-row table-page defences hide"]/table/tr[@class="pd-8"]')
            if not defend_list:
                defend_data = {'球员防守': '暂无数据'}
                cpt_tent.append(defend_data)
                # print(defend_data)
            else:
                for tr in defend_list:
                    defend_ranking = ''.join(tr.xpath('./td[1]/span/text()'))
                    defend_player = ''.join(tr.xpath('./td[2]/a/span/text()'))
                    defend_team = ''.join(tr.xpath('./td[3]/a/span/text()'))
                    defend_nationality = ''.join(tr.xpath('./td[4]/span/text()'))
                    playing_num = ''.join(tr.xpath('./td[5]/text()'))
                    defend_steal = ''.join(tr.xpath('./td[6]/text()'))
                    defend_jiewei = ''.join(tr.xpath('./td[7]/text()'))

                    defend_data = {'球员防守': [{'排名': defend_ranking}, {'球员': defend_player}, {'球队': defend_team},
                                            {'国籍': defend_nationality},
                                            {'出场(替补)': playing_num}, {'抢断': defend_steal}, {'解围': defend_jiewei}]}
                    cpt_tent.append(defend_data)
                    # print(defend_data)

            # 球队数据
            team_list = year_tree.xpath('//div[@class="clearfix-row table-page teams hide"]/table/tr')
            if not team_list:
                team_data = {'球队数据': '暂无数据'}
                cpt_tent.append(team_data)
            else:
                for tr in team_list[1::]:
                    data_ranking = ''.join(tr.xpath('./td[1]/span/text()'))
                    data_team = ''.join(tr.xpath('./td[2]/a/span/text()'))
                    data_session = ''.join(tr.xpath('./td[3]/text()'))
                    data_goal = ''.join(tr.xpath('./td[4]/text()'))
                    data_fumble = ''.join(tr.xpath('./td[5]/text()'))
                    data_shot = ''.join(tr.xpath('./td[6]/text()'))
                    data_shezheng = ''.join(tr.xpath('./td[7]/text()'))  # 射正
                    data_penalty = ''.join(tr.xpath('./td[8]/text()'))
                    data_key_pass = ''.join(tr.xpath('./td[9]/text()'))
                    data_steal = ''.join(tr.xpath('./td[10]/text()'))
                    data_jiewei = ''.join(tr.xpath('./td[11]/text()'))  # 结尾
                    data_foul = ''.join(tr.xpath('./td[12]/text()'))
                    data_card = ''.join(tr.xpath('./td[13]/text()'))

                    team_data = {
                        '球队数据': [{'排名': data_ranking}, {'球队': data_team}, {'场次': data_session}, {'进球': data_goal},
                                 {'失球': data_fumble},
                                 {'射门': data_shot}, {'射正': data_shezheng}, {'点球': data_penalty},
                                 {'关键传球': data_key_pass}, {'抢断': data_steal},
                                 {'解围': data_jiewei}, {'犯规': data_foul}, {'黄牌(红牌)': data_card}]}
                    cpt_tent.append(team_data)
                    # print(team_data)
            data_lists.append(cpt)

        if lock.acquire():
            my_football_set.insert(datas_football)

            print('完成个数+1')

            lock.release()


lock = threading.Lock()
if __name__ == '__main__':
    start_time = time.time()

    # 1、连接Mongodb数据库
    mc = MongoClient('127.0.0.1', 27017)
    db = mc.my_football  # 连接mydb数据库，没有则自动创建
    my_football_set = db.football_set  # 使用test_set集合，没有则自动创建

    # 2、创建队列
    url_queue = Queue()
    for football_url in ball_url_list:
        base_url = 'https://data.leisu.com/'
        url = request.urljoin(base_url, football_url)
        url_queue.put(url)
    # 3、生成10个线程
    crawl_thread = []
    for i in range(10):
        football_spider = Football_Spider(i, url_queue)
        football_spider.start()
        crawl_thread.append(football_spider)

    for thread in crawl_thread:
        thread.join()
    end_time = time.time()
    print('总耗时:', end_time - start_time)
