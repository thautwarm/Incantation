# 媒体

## 包含的组件

```python
from incantation.Module.CSS.Media import responsive_video, img, video_container
```

我想我可以照搬`docstring`, 因为这方面我做得太过完善:)
当你在`ipython`中输入如下代码

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
