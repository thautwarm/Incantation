from ..abst import Tag, Attribute, traits_class, ITraitsAttribute
from ..utils import doc_printer, default_initializer


class Img(Tag):
    @default_initializer
    def __init__(self, *components, src: str, alt: str = None):
        if alt:
            Tag.__init__(self, 'img',
                         Attribute('src', src),
                         Attribute('alt', alt),
                         *components)
        else:
            Tag.__init__(self, 'img',
                         Attribute('src', src),
                         *components)


@traits_class('class', 'responsive-img', inherit_from=Attribute)
class IsResponsiveImg(ITraitsAttribute):
    pass


class ResponsiveImg(Tag):
    @default_initializer
    def __init__(self, src: str, alt: str = None):
        if alt:
            Tag.__init__(self, 'img',
                         Attribute('class', 'responsive-img'),
                         Attribute('src', src),
                         Attribute('alt', alt))
        else:
            Tag.__init__(self, 'img', Attribute('class', 'responsive-img'), Attribute('src', src))

    @property
    def circle(self):
        return self.append(Attribute('class', 'circle'))

    @doc_printer
    def help(self):
        """
        >>> import incantation as inc
        >>> inc.ResponsiveImg(src='xxx.png')
        >>> inc.Img(inc.IsResponsiveImg(), src='xxx.png')
        """


class Video(Tag):
    @default_initializer
    def __init__(self, src: str, width=853, height=480, allow_full_screen: bool = True):
        Tag.__init__(self, 'div', Attribute('class', 'video-container'), IFrame(src, width, height, allow_full_screen))

    @doc_printer
    def help(self):
        """
        >>> import incantation as inc
        >>> inc.Video(src='//www.youtube.com/embed/Q8TXgCzxEnw?rel=0')
        """


class IFrame(Tag):
    @default_initializer
    def __init__(self, src: str, width: int, height: int, allow_full_screen: bool):
        arg_list = [Attribute('src', src),
                    Attribute('width', width),
                    Attribute('height', height)]
        if allow_full_screen:
            arg_list.append(Attribute('allowfullscreen'))

        Tag.__init__(self, 'iframe', *arg_list)


class ResponseVideo(Tag):
    @default_initializer
    def __init__(self, src: str, type: str = 'video/mp4'):
        Tag.__init__(self, 'video',
                     Attribute('class', 'responsive-video'), Attribute('controls'),
                     Tag('source',
                         Attribute('src', src), Attribute('type', type)))
