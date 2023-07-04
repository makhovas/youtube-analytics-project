from src.channel import Channel


class Video:

    def __init__(self, video_id: str):
        self.__video_id = video_id
        self.__title = None
        self.__url = None
        self.__view_count = None
        self.__like_count = None
        self.video_data()

    def __str__(self):
        return self.__title

    def video_data(self):
        try:
            youtube = Channel.get_service().videos().list(
                part='snippet,statistics', id=self.video_id
            ).execute()
            video_data = youtube.get('items')[0]
            self.__title = video_data.get('snippet').get('title')
            self.__url = f'https://www.youtube.com/watch?v={self.video_id}'
            self.__view_count = int(video_data.get('statistics').get('viewCount'))
            self.__like_count = int(video_data.get('statistics').get('likeCount'))
        except IndexError:
            print('Неверная ссылка!')

    @property
    def video_id(self):
        return self.__video_id

    @video_id.setter
    def video_id(self, value):
        self.__video_id = value


class PLVideo(Video):

    def __init__(self, video_id: str, playlist_id: str):
        self.__playlist_id = playlist_id
        super().__init__(video_id)
