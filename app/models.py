
class News:
    '''
    news class objects
    '''

    def __init__(self,title,description,author,publishedAt,url):
        self.title = title
        self.description = description
        self.author = author
        self.publishedAt = '2001-01-02'
        self.url ='https://www.theverge.com/2020/4/24/21233468/facebook-messenger-rooms-live-instagram-live-igtv-video-chat'



class Source:
    '''
    source class to define source objects
    '''


    def __init__(self,name,description):
        self.name = name
        self.description = description

