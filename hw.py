from incantation.template import Page
from incantation.Module.abst import Seq

from incantation.Module.CSS.Grid import container, col, row, grid, divider
from incantation.Module import blockquote
from incantation.Module.CSS.Table import table
from incantation.Module.Component.Badges import collections, badge

from flask import Flask, g, request, render_template, url_for, redirect


def myPage(name):
    main = container()

    welcome = blockquote(f"Welcome to Incantation, {name}!")

    title = blockquote("Incantation使用者的评价反馈")
    users = table(["姓名", "评价", "日期"],
                  [["Misakawa", "我自己做的，还能不给自己好评吗？完美的抽象！10/10分！", "2017-10-28"],
                   ["Thautwarm", "上面那个是我小号...", "2017-10-28"],
                   ["Ruikowa", "十分 and 我是被小号的。", "2017-10-29"]
                   ])

    side = collections([badge(new=True, href='#!', num=1, name='关注'),
                        badge(new=True, href='#!', num=4, name='评论'),
                        badge(href='#!', name='私信'),
                        badge(new=False, href='#!', num=6, name='你的组织'),
                        badge(href='#!', name='用户设置'),
                        badge(href='#!', name='帮助反馈'),
                        ])

    main.contains(Seq(
        welcome,
        divider(),
        "<br>",
        row(Seq(
            col(side, grid(l=3, s=3, m=3)),
            col(Seq(title, users), grid(l=8, s=8, m=8)),
        )
        )
    ))
    page = Page(main)
    return page.gen()


app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET'])
def index():
    return myPage("萌新")


app.run('localhost')
