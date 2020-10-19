# coding:utf-8
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dangdang.settings")
django.setup()

from django.test import TestCase
from index.models import TBook, TCategory

# TBook.objects.create(book_name="高等数学同济版(上册)",author="",press="",public_time="",price="",discount="",
#                      picture="",vision="",page_num="", number="",printing_time="",paper="",isbn="",whether="",
#                      packing="",editor_recommend="",content_recommend="",about_author="",
#                      catalog="",comment="",content="",cate="",sale="",new_time="",money="")

# TCategory.objects.create(cate_name ="教育" , parent_id =None, level=1)
# TCategory.objects.create(cate_name ="教材" , parent_id =1, level=2)
# TCategory.objects.create(cate_name ="外语" , parent_id =1, level=2)
# TCategory.objects.create(cate_name ="考试" , parent_id =1, level=2)
# TCategory.objects.create(cate_name ="教辅书" , parent_id =1, level=2)
# TCategory.objects.create(cate_name ="小说" , parent_id =None, level=1)
# TCategory.objects.create(cate_name ="文艺" , parent_id =None, level=1)
# TCategory.objects.create(cate_name ="文学" , parent_id =8, level=2)
# TCategory.objects.create(cate_name ="传记" , parent_id =8, level=2)
# TCategory.objects.create(cate_name ="艺术" , parent_id =8, level=2)
# TCategory.objects.create(cate_name ="儿童" , parent_id =None, level=1)
# TCategory.objects.create(cate_name ="科普" , parent_id =12, level=2)
# TCategory.objects.create(cate_name ="绘本" , parent_id =12, level=2)
# TCategory.objects.create(cate_name ="生活" , parent_id =None, level=1)
# TCategory.objects.create(cate_name ="育儿" , parent_id =14, level=2)
# TCategory.objects.create(cate_name ="美食" , parent_id =14, level=2)
# TCategory.objects.create(cate_name ="美妆" , parent_id =14, level=2)

# book = TBook.objects.all()
# for i in book:
#     i.number=91023
#     i.vision=5
#     i.page_num=6666
#     i.printing_time="2012-5-23"
#     i.paper="胶状纸"
#     i.new_time="2012-5-9"
#     i.catalog="第1话 你好，我叫梅茜我们你快乐吗个子小就小吧，幸福就好小边牧的大飞盘番外：飞盘掉了！分家彪形大汉的玻璃心冬不拉的红糖纸后来……"
#     i.public_time="2012-2-10"
#     i.content="孩子自觉性差，父母一不看着就管不住自己。 别人家的孩子五岁会背一百首古诗，认识一千五百个字， 我的孩子是不是落后了？ 做作业拖拉，不肯上幼儿园，遇到困难就退缩…… 这些让中国家长普遍感到头痛的难题，是不是也在困扰着你？社会高速发展，今天培养的孩子，在二十年后才会成为建设社会的主力军。所以，清楚二十年之后世界的模样、职场的变化，并提前做出应对，是家长为孩子做出的重要的选择。 世界科幻大奖“雨果奖”得主郝景芳，兼具科幻作家对未来的前瞻思维与经济学家对社会的分析与洞见。她以学霸的钻研精神，深阅读学习了上百本经典的心理学和教育学书籍，对于儿童心理发展、脑科学和各流派教育理论都有深研习，并向各领域专家学习实践经验。同时她结合自己养育两个孩子的丰富经验，以及用作家的敏锐眼光积累的鲜活案例，为中国家长总结出关于社会发展趋势的分析，四种父母思维革新模型，五种孩子成长核心能力以及家庭启蒙的实用方法，帮你透过复杂的现象，抓住教育的本质，不走冤枉路<br/>【推荐语】<br/>1、一本给父母的科学认知养育指南，令人头痛的养育难题有办法了，治愈你的育儿焦虑病，找回教育的本质。 2、科技前瞻思维的教育家妈妈、第74届世界科幻大会“雨果奖”得主郝景芳，用丰富详细的亲身实践，带你提升家庭教育中的认知。 3、1份时代社会趋势分析，4种父母思维模型重塑，5大成长核心能力造，融合儿童心理发展、脑科学和世界各流派教育理论，提供在家就能用的启蒙方法。<br/>【作者】<br/>哈佛大学肯尼迪政府学院访问学者； 清华大学天体物理硕士、经济学博士； 第 74 届世界科幻大会“雨果奖”得主； 2018 年世界青年领袖； 《财富》杂志 2017 年 40 岁以下商界精英； “童行学院”创始人； 两个孩子的妈妈<br/>"
#     i.isbn="9787559642431"
#     i.whether=0
#     i.discount=6.8
#     i.packing="精装"
#     i.press="太原理工大学"
#     i.save()

