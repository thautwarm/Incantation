from pprint import pprint

import incantation as inc
import incantation.Frequently as incf  # 提供一些常用的html标签

# print(str(
#     inc.Container(color,
#                   "123",
#                   inc.Grid(s=2),
#                   inc.Push(s=2)
#                   ).set_indent(1).append(color)
# ))

# print(inc.Align.vertical)
# print(inc.Video('//www.youtube.com/embed/Q8TXgCzxEnw?rel=0').set_indent(1))

# print(inc.ResponseVideo('//www.youtube.com/embed/Q8TXgCzxEnw?rel=0').append(inc.ZDepth(2).rise(2)).set_indent(1))

# print(inc.Th())


# inc.DropdownButton.help()


# print(dropdown)
# print(dropdown.link())
# inc.Dropdown.help()

# print(card)
img_url = './sample-1.jpg'
贪玩蓝月 = 'http://baidu.code.xuxiyx.com/htmlcode/13085.html'
贪玩蓝月百度百科 = "《贪玩蓝月》是一款集经典与创新的传奇游戏，采用2.5D图像技术，通过即时的光影成像技术，营造亦真亦幻的游戏世界。突破以往传奇游戏的桎梏，再度重现英雄合击的经典版本。"

SubmitPage = 'tanwansubmit.html'
IndexPage = 'tanwan.html'

navbar = inc.NavBar(inc.BrandLogo('贪玩鬼',
                                  inc.Align.force_center,  # 强制中心
                                  incf.Href(贪玩蓝月),
                                  ),
                    inc.Tag('ul',
                            inc.Align.force_right,  # 强制向右
                            inc.Tag('li') << inc.Tag('a', inc.Attribute('href', 贪玩蓝月), "点击就送"),
                            inc.Tag('li') << inc.Tag('a', inc.Attribute('href', SubmitPage), '是兄弟就来干我')),
                    # << 表示向目标方向添加元素

                    inc.Color('teal'))  # 设定颜色

dropdown = inc.Dropdown(
    inc.Attribute('id', '贪玩dropdown'),
    inc.Tag('li', inc.Tag('a',
                          incf.Href(SubmitPage),
                          "屠龙宝刀",
                          inc.Badge("!", new=True))),
    inc.Tag('li', inc.Tag('a',
                          incf.Href(SubmitPage),
                          inc.Badge("go!"),
                          '荷官发牌')))

inc.Page(inc.Container(

    navbar,

    '<br>',  # 支持手写html

    inc.C(  # C 其实就是div，一个块
        inc.Grid(s=2, m=2, l=2),  # 给这个块加颜色
        inc.Align.right,  # 让这个块右对齐

        dropdown,
        # 将dropdown显示在此处
        dropdown.link("点击注册",
                      inc.Attribute('href', SubmitPage),
                      inc.Icon('arrow_drop_down', inc.Attribute('class', 'right'))),
    ),

    # 渲染一个表格，index可以省略
    inc.Table(
        data_source=[
            ["腰酸背痛", "合理", "只需体验三分钟"],
            ["头皮发麻", "一颗赛艇", "爱上介款游戏"]
        ],
        columns=['没玩贪玩蓝月', '玩玩贪玩蓝月', '装备真能赚钱?'],
        index=['同学1', '同学2']),

    # 三个小短文。 IconBlock可以用来写短文
    inc.Row(
        inc.C(
            inc.C(inc.Grid(s=12, m=4), inc.Align.center)
            << inc.IconTextBlock('blue', "今晚八点", "贪玩蓝月，找回年秀时贪玩的你", inc.Icon('flash_on')),

            inc.C(inc.Grid(s=12, m=4), inc.Align.center)
            << inc.IconTextBlock(icon_color='orange', title='贪玩气球', text='玩玩一年，原来装备真能赚钱', icon=inc.Icon('edit')),

            inc.C(inc.Grid(s=12, m=4), inc.Align.center)
            << inc.IconTextBlock(icon_color='green', title='一人我渣渣辉', text='刚好遇见渣渣辉', icon=inc.Icon('ac_unit'))

        )
    ),

    # 卡片
    inc.C(
        inc.IsCard(),  # 声明这是个卡片

        # 在一行内分割文字图片
        inc.Row(

            # 声明背景色
            inc.Color('brown').lighten.lighten_by(2),  # 选择棕色，选择亮色区域，亮度+2

            inc.CardImage(inc.Img(inc.Grid(s=12, m=6, l=6), src=img_url, alt='贪玩挂了？'))
                .append(inc.Align.left, inc.Hover()),  # 添加一个卡片的图，并且左对其+悬浮特效

            # 写一个卡片
            inc.C(inc.Grid(s=12, m=6, l=6),
                  inc.CardContent(
                      # 卡片标题
                      inc.CardTitle('贪玩卡').append(inc.Align.left),

                      # 增加卡片文字描述
                      inc.Paragraph(
                          inc.Paragraph("<h3>来玩</h3>"),
                          incf.NewLine,  # 加新行
                          "古天乐，陈小春，渣渣辉，都在玩这个游戏，你还在等什么？",
                          incf.NewLine,
                          inc.Paragraph("百科:",
                                        incf.NewLine,
                                        贪玩蓝月百度百科
                                        ).append(inc.Align.left)
                      ).append(inc.IsHover()),  # 增加悬浮属性
                      inc.TextColor('white')),

                  ).append(inc.Align.right, inc.Hover()),
        ).append(inc.Pulse()),  # 增加pulse，闪闪发光

        inc.Row(

            inc.Color('teal').lighten.lighten_by(2),

            inc.C(inc.Grid(s=12, m=6, l=6),
                  inc.CardContent(
                      inc.CardTitle('贪玩卡').append(inc.Align.right),

                      inc.Paragraph("<h2>来玩</h2>",
                                    incf.NewLine,
                                    "古天乐，陈小春，渣渣辉，都在玩这个游戏，你还在等什么？",
                                    incf.NewLine,
                                    "百科",
                                    incf.NewLine,
                                    贪玩蓝月百度百科),
                      inc.TextColor('white')).append(inc.IsHover()),

                  ).append(inc.Align.left),

            inc.CardImage(inc.Img(inc.Grid(s=12, m=6, l=6), src=img_url, alt='贪玩挂了？')).append(inc.Align.right),

        ).append(inc.Pulse()),
    ),
    # 卡片动作（链接
    inc.CardAction(inc.Tag('a', inc.Attribute(SubmitPage, '#!'), '船新版本'),
                   inc.Tag('a', inc.Attribute(SubmitPage, '#!'), '古天乐绿了'),
                   inc.Tag('a', incf.Href(SubmitPage), '登录游戏').append(inc.Align.force_right)),

)).write(to='test/tanwan.html')  # 写入html

side_nav = inc.SideNav.new(
    id='sda',
    profile_background_img='b1.jpg',
    user_info=[

        inc.SideNavItem(inc.Img(
            inc.Attribute('class', 'circle'),
            src='avatar.jpg'),
            incf.Href('#user!')),

        inc.SideNavItem(inc.Span(inc.Attribute('class', 'email'),
                                 inc.TextColor('black'),
                                 "<h4>xxx@lll</h4>"),
                        incf.Href('#user')),
    ]

)

inc.Page(
    side_nav,
    side_nav.link(inc.Icon('menu')).append(inc.Align.left),
    side_nav.active(),

    inc.NavBar(inc.BrandLogo('贪玩鬼',
                             inc.Align.force_center,  # 强制中心
                             incf.Href(贪玩蓝月),
                             ),
               inc.Tag('ul',
                       inc.Align.force_right,  # 强制向右
                       inc.Tag('li') << inc.Tag('a', inc.Attribute('href', 贪玩蓝月), "点击就送"),
                       inc.Tag('li') << inc.Tag('a', inc.Attribute('href', SubmitPage), '是兄弟就来干我')),
               # << 表示向目标方向添加元素

               inc.Color('teal')),  # 设定颜色
    inc.Container(

        inc.Row(
            inc.Grid(s=12, m=12, l=12),
        ),
        *(incf.NewLine,) * 5,

        inc.Row(
            inc.C(

                inc.Tag('a',
                        incf.Href(贪玩蓝月),
                        inc.Img(inc.Grid(s=12, m=6), inc.IsHover(), src='pm.jpg', alt='贪玩揽约'),
                        )),
            inc.C(
                inc.Grid(s=12, m=6),
                inc.Form(
                    inc.Attribute('action', IndexPage),
                    inc.Attribute('method', 'post'),

                    inc.InputField(inc.Input(inc.Input.Enum.text,
                                             inc.Attribute('id', 'username'),
                                             inc.Attribute('name', 'username')),

                                   inc.Label(inc.Attribute('for', 'username'),
                                             "渣渣名")
                                   ),

                    inc.InputField(inc.Input(inc.Input.Enum.password,
                                             inc.Attribute('id', 'password'),
                                             inc.Attribute('name', 'password')),

                                   inc.Label(inc.Attribute('for', 'password'),
                                             "渣渣码")
                                   ),

                    inc.C(
                        inc.Submit(inc.C("渣渣交").append(inc.Align.center),
                                   inc.Grid(s=4, m=2, l=2),
                                   inc.Icon("submit"),
                                   inc.Attribute('id', 'submit'),
                                   inc.IsRaised(),
                                   inc.Align.force_right
                                   ),
                    ),
                    *(incf.NewLine,) * 2,
                    inc.Collapsible(
                        inc.Tag('li',
                                inc.CollapsibleHeader(
                                    inc.Icon('filter_drama'),
                                    "遇见渣渣",
                                    inc.Badge('就是渣渣',
                                              inc.Attribute('id', '在这里用js动态修改'),
                                              new=True)),

                                inc.CollapsibleBody(
                                    inc.Icon('place'),
                                    inc.Tag('a',
                                            incf.Href(贪玩蓝月),
                                            "点击就送"
                                            ),
                                    inc.Paragraph(贪玩蓝月百度百科)

                                ))
                    ),
                ),
            ),
        ),
        inc.Slider(
            inc.Slide(img='./static/images/index1.jpg', big_text='贪玩蓝月', tiny_text='你没有玩过的全新版本', align='right'),
            inc.Slide(img='./static/images/index1.jpg', big_text='贪玩蓝月', tiny_text='你没有玩过的全新版本', align='right'),
            inc.DoSliderActivate()
        )
    )).write(to='test/tanwansubmit.html')
