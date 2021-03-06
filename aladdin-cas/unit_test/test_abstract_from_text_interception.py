#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
from analysis_package.abstract_from_text_interception import get_abstract_from_text_interception

s_content = '''
我与父亲不相见已二年余了，我最不能忘记的是他的背影 。
那年冬天，祖母死了，父亲的差使也交卸了，正是祸不单行的日子。我从北京到徐州，打算跟着父亲奔丧回家。到徐州见着父亲，看见满院狼籍的东西，又想起祖母，不禁簌簌地流下眼泪。父亲说：“事已如此，不必难过，好在天无绝人之路！”
回家变卖典质，父亲还了亏空；又借钱办了丧事。这些日子，家中光景很是惨淡，一半为了丧事，一半为了父亲赋闲。丧事完毕，父亲要到南京谋事，我也要回北京念书，我们便同行。
到南京时，有朋友约去游逛，勾留了一日；第二日上午便须渡江到浦口，下午上车北去。父亲因为事忙，本已说定不送我，叫旅馆里一个熟识的茶房陪我同去。他再三嘱咐茶房，甚是仔细。但他终于不放心，怕茶房不妥贴；颇踌躇了一会。其实我那年已二十岁，北京已来往过两三次，是没有什么要紧的了。他踌躇了一会，终于决定还是自己送我去。我再三劝他不必去；他只说：“不要紧，他们去不好！”
我们过了江，进了车站。我买票，他忙着照看行李。行李太多了，得向脚夫行些小费才可过去。他便又忙着和他们讲价钱。我那时真是聪明过分，总觉他说话不大漂亮，非自己插嘴不可，但他终于讲定了价钱；就送我上车。他给我拣定了靠车门的一张椅子；我将他给我做的紫毛大衣铺好座位。他嘱我路上小心，夜里要警醒些，不要受凉。又嘱托茶房好好照应我。我心里暗笑他的迂；他们只认得钱，托他们只是白托！而且我这样大年纪的人，难道还不能料理自己么？唉，我现在想想，那时真是太聪明了！
我说道：“爸爸，你走吧。”他往车外看了看说：“我买几个桔子去。你就在此地，不要走动。”我看那边月台的栅栏外有几个卖东西的等着顾客。走到那边月台，须穿过铁道，须跳下去又爬上去。父亲是一个胖子，走过去自然要费事些。我本来要去的，他不肯，只好让他去。我看见他戴着黑布小帽，穿着黑布大马褂，深青布棉袍，蹒跚地走到铁道边，慢慢探身下去，尚不大难。可是他穿过铁道，要爬上那边月台，就不容易了。他用两手攀着上面，两脚再向上缩；他肥胖的身子向左微倾，显出努力的样子，这时我看见他的背影，我的泪很快地流下来了。我赶紧拭干了泪。怕他看见，也怕别人看见。我再向外看时，他已抱了朱红的桔子往回走了。过铁道时，他先将桔子散放在地上，自己慢慢爬下，再抱起桔子走。到这边时，我赶紧去搀他。他和我走到车上，将桔子一股脑儿放在我的皮大衣上。于是扑扑衣上的泥土，心里很轻松似的。过一会说：“我走了，到那边来信！”我望着他走出去。他走了几步，回过头看见我，说：“进去吧，里边没人。”等他的背影混入来来往往的人里，再找不着了，我便进来坐下，我的眼泪又来了。
近几年来，父亲和我都是东奔西走，家中光景是一日不如一日。他少年出外谋生，独立支持，做了许多大事。哪知老境却如此颓唐！他触目伤怀，自然情不能自已。情郁于中，自然要发之于外；家庭琐屑便往往触他之怒。他待我渐渐不同往日。但最近两年不见，他终于忘却我的不好，只是惦记着我，惦记着我的儿子。我北来后，他写了一信给我，信中说道：“我身体平安，惟膀子疼痛厉害，举箸提笔，诸多不便，大约大去之期不远矣。”我读到此处，在晶莹的泪光中，又看见那肥胖的、青布棉袍黑布马褂的背影。唉！我不知何时再能与他相见！
'''
s_content2 = '''
我与父亲不相见已二年余了，我最不能忘记的是他的背影 。
那年冬天，祖母死了，父亲的差使也交卸了，正是祸不单行的日子。我从北京到徐州，打算跟着父亲奔丧回家。到徐州见着父亲，看见满院狼籍的东西，又想起祖母。我看那边月台的栅栏外有几个卖东西的等着顾客。走到那边月台，须穿过铁道，须跳下去又爬上去。父亲是一个>胖子，走过去自然要费事些。我本来要去的，他不肯，只好让他去。我看见他戴着黑布小帽，穿着黑布大马褂，深青布棉袍，蹒跚地走到铁道边，慢慢探身下去，尚不大难。可是他穿过铁道，要爬上那边月>台，就不容易了。他用两手攀着上面，两脚再向上缩；他肥胖的身子向左微倾，显出努力的样子，这时我看见他的背影，我的泪很快地流下来了。我赶紧拭干了泪。怕他看见，也怕别人看见。我再向外看时>，他已抱了朱红的桔子往回走了。过铁道时，他先将桔子散放在地上，自己慢慢爬下，再抱起桔子走。到这边时，我赶紧去搀他。他和我走到车上，将桔子一股脑儿放在我的皮大衣上。于是扑扑衣上的泥土>，心里很轻松似的。过一会说：“我走了，到那边来信！”我望着他走出去。他走了几步，回过头看见我，说：“进去吧，里边没人。”等他的背影混入来来往往的人里，再找不着了，我便进来坐下，我的眼泪>又来了。
近几年来，父亲和我都是东奔西走，家中光景是一日不如一日。他少年出外谋生，独立支持，做了许多大事。哪知老境却如此颓唐！他触目伤怀，自然情不能自已。情郁于中，自然要发之于外；家庭琐屑便>往往触他之怒。他待我渐渐不同往日。但最近两年不见，他终于忘却我的不好，只是惦记着我，惦记着我的儿子。我北来后，他写了一信给我，信中说道：“我身体平安，惟膀子疼痛厉害，举箸提笔，诸多不
'''
s_content3 = '''
我与父亲不相见已二年余了，我最不能忘记的是他的背影 。心里很轻松似的。过一会说：“我走了，到那边来信！”我望等他的背影混入来来往往的人里，再找不着了，我便进来坐下，我的眼泪又来了。
他触目伤怀，自然情不能自已。情郁于中，自然要发之于外；家庭琐屑便>往往触他之怒。
他待我渐渐不同往日。但最近两年不见，他终于忘却我的不好，只是惦记着我，惦记着我的儿子。我北来后，他写了一信给我，信中说道：“我身体平安，惟膀子疼痛厉害，举箸提笔，诸多不。近几年来，父亲和我都是东奔西走，家中光景是一日不如一日。他少年出外谋生，独立支持，做了许多大事。哪知老境却如此颓唐！他触目伤怀，自然情不能自已。情郁于中，自然要发之于外；家庭琐屑便往往触他之怒。
'''


class TestExtractMethod(unittest.TestCase):

    def setUp(self):
        self.content = (u"深蓝的天空中挂着一轮金黄的圆月，下面是海边的沙地，都种着一望无际的碧绿的西瓜。"
                        u"其间有一个十一二岁的少年，项带银圈，手捏一柄钢叉，向一匹猹尽力地刺去。那猹却将身一扭，"
                        u"反从他的胯下逃走了。  这少年便是闰土。我认识他时，也不过十多岁，离现在将有三十年了；"
                        u"那时我的父亲还在世，家景也好，我正是一个少爷。那一年，我家是一件大祭祀的值年。这祭祀，"
                        u"说是三十多年才能轮到一回，所以很郑重。正月里供像，供品很多，祭器很讲究，拜的人也很多，"
                        u"祭器也很要防偷去。我家只有一个忙月（我们这里给人做 工的分三种：整年给一定人家做工的叫长工；"
                        u"按日给人做工的叫短工；自己也种地，只在过年过节以及收租时候来给一定的人家做工的称忙月），"
                        u"忙不过来，他便对父亲说，可以叫他的儿子闰土来管祭器的。  我的父亲允许了；我也很高兴，"
                        u"因为我早听到闰土这名字，而且知道他和我仿佛年纪，闰月生的，五行缺土，所以他的父亲叫他闰土。"
                        u"他是能装弶捉小鸟雀的。  我于是日日盼望新 年，新年到，闰土也就到了。好容易到了年末，有一日，"
                        u"母亲告诉我，闰土来了，我便飞跑地去看。他正在厨房里，紫色的圆脸，头戴一顶小毡帽，"
                        u"颈上套一个明晃晃的银项圈，这可见他的父亲十分爱他，怕他死去，所以在神佛面前许下愿心，"
                        u"用圈子将他套住了。他见人很怕羞，只是不怕我，没有旁人的时候，便和我说话，于是不到半日，"
                        u"我们便熟识了。    我们那时候不知道谈些什么，只记得闰土很高兴，说是上城之后，见了许多没有"
                        u"见过的东西。  第二日，我便要他捕鸟。他说：“这不能。须大雪下了才好，我们沙地上，下了雪，"
                        u"我扫出一块空地来，用短棒支起一个大竹匾，撒下秕谷，看鸟雀来吃时，我远远地将缚在棒上的绳子"
                        u"只一拉，那鸟雀就罩在竹匾下了。什么都有：稻鸡，角鸡，鹁鸪，蓝背……”  我于是又很盼望下雪。  "
                        u"闰土又对我说：“现在太冷，你夏天到我们这里来。我们日里到海边捡贝壳去，红的绿的都有，鬼见怕"
                        u"也有，观音手也有。晚上我和爹管西瓜去，你也去。”  “管贼吗？”  “不是。走路的人口渴了摘"
                        u"一个瓜吃，我们这里是不算偷的。要管的是獾猪，刺猬，猹。月亮地下，你听，啦啦地响了，"
                        u"猹在咬瓜了。你便捏了胡叉，轻轻地走去……”  我那时并不知道这所谓猹的是怎么一件东西——"
                        u"便是现在也不知道——只是无端地觉得状如小狗而很凶猛。  “它不咬人吗？”  “有胡叉呢。"
                        u"走到了，看见猹了，你便刺。这畜生很伶俐，倒向你奔来，反从胯下窜了 。它的皮毛是油一般的滑"
                        u"……”  我素不知道天下有这许多新鲜事：海边有如许五色的贝壳；西瓜有这样危险的经历，"
                        u"我先前单知道它在水果店里出卖罢了。  “我们沙地里，潮汛要来的时候，就有许多跳鱼儿只是跳，"
                        u"都有青蛙似的两个脚……”    啊！闰土的心里有无穷无尽的稀奇的事，都是我往常的一朋友"
                        u"所不知道的。闰土在海边时，他们都和我一样，只看见院子里高墙上的四角的天空。  "
                        u"可惜正月过去了，闰土须回家里去。我急得大哭，他也躲到厨房里，哭着不肯出门，"
                        u"但终于被他父亲带走了。他后来还托他的父亲带给我一包贝壳和几支很好看的鸟毛，"
                        u"我也曾送他一两次东西，但从此没有再见面。 我在朦胧中，眼前又展开一片海边碧绿的沙地来，"
                        u"上面深蓝的天空中挂着一轮金黄的圆月。")

    def test_abstract(self):
        global s_content
        content = s_content
        print('============content length is %s'%len(content))
        abstract =get_abstract_from_text_interception(content)
        print(abstract)
        self.assertTrue(isinstance(abstract,str))
        self.assertTrue(len(abstract)>10)
    def test_abstract2(self):
        global s_content
        content = s_content2
        print('============content length is %s'%len(content))
        abstract =get_abstract_from_text_interception(content)
        print(abstract)
        self.assertTrue(isinstance(abstract,str))
        self.assertTrue(len(abstract)>10)
    def test_abstract_short_text(self):
        short_text = '我们人民中国中华人民共和国。人民。中国。'
        abstract = get_abstract_from_text_interception(short_text)
        print(abstract)
    def test_abstract3(self):
        global s_content
        content = s_content3
        print('============content length is %s'%len(content))
        abstract =get_abstract_from_text_interception(content)
        print(abstract)
        self.assertTrue(isinstance(abstract,str))
        self.assertTrue(len(abstract)>10)


if __name__ == "__main__":
    unittest.main()


