import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.youtube = self.get_service()
        self.channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.subscriberCount = self.channel['items'][0]['statistics']['subscriberCount']
        self.url = f'https://www.youtube.com/channel/{self.channel_id}'
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.viewCount = self.channel['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)

    def to_json(self, filename):
        channel_data = {
            'channel_id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'subscriberCount': self.subscriberCount,
            'url': self.url,
            'videoCount': self.video_count,
            'viewCount': self.viewCount
        }
        with open(filename, 'w', encoding='UTF-8') as file:
            json.dump(channel_data, file, indent=2, ensure_ascii=False)
