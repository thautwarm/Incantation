# 媒体

## 包含的组件

```python
from incantation.Module.CSS.Media import responsive_video, img, video_container
```

`img`用来创建一个图片。
我想我可以照搬`img`的`docstring`。
当你在`ipython`中输入如下代码
``` 
In [1]: from incantation.Module.CSS.Media import responsive_video, img, video_container
In [2]: img?
Init signature: img(*args, **kwargs)
Docstring:     
See http://materializecss.com/media-css.html
user help : >> help (img.init)
------------------------------
    Guide:
        >> im = img(src = "cool_pic.jpg")
        >> im.append_class("responsive-img")
        >> im.append_class("class")
    which equals:
        >> im = img(**{'src': 'cool_pic.jpg', 'class':'responsive-img class'})
File:           c:\users\misaka-wa\software\conda\envs\dev\lib\site-packages\incantation-0.1.2-py3.6.egg\incantation\module\css\media.py
Type:           type
```

[![help](./help.PNG)](./help.PNG)

## Img

docstring:
```
Guide:
        >> im = img(src = "cool_pic.jpg")
        >> im.append_class("responsive-img")
        >> im.append_class("class")
    which equals:
        >> im = img(**{'src': 'cool_pic.jpg', 'class':'responsive-img class'})
```

## ResponsiveVideo

docstring:
```
See http://materializecss.com/media-css.html
user help : >> help (video_container.init)
------------------------------
    Guide:
        >> video = responsive_video(src = "movie.mp4")
    which equals:
        >> video = responsive_video(src = "movie.mp4", type = "video/mp4")
```

## VideoContainer

docstring:
```
See http://materializecss.com/media-css.html
user help : >> help (video_container.init)
------------------------------
    Guide:
        >> video = video_container(src = "//www.youtube.com/embed/Q8TXgCzxEnw?rel=0")
        
    Take care that `video_container` takes some default arguments:
        
        video = video_container(src = "//www.youtube.com/embed/Q8TXgCzxEnw?rel=0")
    equals 
        video = video_container(src   = "//www.youtube.com/embed/Q8TXgCzxEnw?rel=0",
                                width = 853,
                                height= 480,
                                frameborder = 0)
```
