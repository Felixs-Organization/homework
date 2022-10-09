# import pygal
lst = {('z',[1,2,3]),

       ('l',(2,3,4))}

import requests
#

# for ls in lst:

#     # 采用循环为雷达图添加数据

#     radar = pygal.Radar()

#

#     for l in lst[ls]:

#         print(l,lst[ls][l])

#         radar.add(l, lst[ls][l])

#

#     radar.x_labels = ['攻击', '防御', '速度']

#

#     radar.title = ls

#

#     # 控制各得分点的大小

#

#     radar.dots_size = 8

#

#     # 设置将图例放在底部

#

#     radar.legend_at_bottom = True

#

#     # 指定将数据图例输出到SVG文件中

#

#     radar.render_to_file(str(ls) + '.svg')

#

import pygal

radar_chart = pygal.Radar()

radar_chart.title = 'ewf'

radar_chart.x_labels = ['得分', '防守', '助攻', '失误', '篮板']

radar_chart.add('库里', [70, 98, 96, 85, 97])



radar_chart.render_in_browser()





'''

作业

每个英雄做出来自己独立的雷达图

'''