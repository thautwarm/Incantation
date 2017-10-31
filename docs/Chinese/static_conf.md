
# 配置静态文件。

## 关于flowpython
Incantation使用[flowpython](https://github.com/thautwarm/flowpython)书写, 使用扩展的模式匹配和函数式写法来简化代码的逻辑。  
flowpython与CPython使用同一套字节码，所以，所有资源被编译成`pyc`文件来发布，以便于使用更少的依赖也可以工作在不同的操作系统上。

**P.S**  

    如果你希望查看Incantation的源代码，你需要安装flowpython，而它暂时只工作在windows和linux平台上。
    flowpython只是一个扩展了的Python解释器，支持Python-3.5.x和Python-3.6.1和Python-3.6.2。  
    使用flowpython的方法可以是`pip install flowpython&&python -m flowpython -m enable`。  
    但我更建议的是前往[flowpython release](https://github.com/thautwarm/flowpython/releases)下载对应系统的flowpython解释器，并用之替换标准CPython的解释器。  
    解释器的位置使用`which python`得知, 对Windows用户, 这个命令是`where python`.


## 配置静态文件
在Incantation项目主页下有一个static文件，你需要**保证它位于你web app(flask应用，或者django应用之类的)的根目录下**，项目结构应如下。
```
- your_app

    - index.py
    
    - static
        
        - jquery-3.2.1.min.js
        
        - materialize

            - css
                - materialize.css
                - materialize.min.css
                

            - js
                - materialize.js
                - materialize.min.js

            - fonts
                - roboto
                    ... # 一些字体

        
            - LICENSE # materialize-css 的license


```
最好的办法就是直接使用[Incantation](https://github.com/thautwarm/Incantation)项目根目录的那个static文件夹