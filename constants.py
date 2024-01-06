import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), "config/config.local"))

YOUTUBE_API_KEY = parser.get("youtube", "API_KEY")
YOUTUBE_PLAYLIST_REQUEST_URL = parser.get("youtube", "YOUTUBE_PLAYLIST_REQUEST_URL")
YOUTUBE_VIDEO_REQUEST_URL = parser.get("youtube", "YOUTUBE_VIDEO_REQUEST_URL")
YOUTUBE_PLAYLIST_ID = parser.get("youtube", "YOUTUBE_PLAYLIST_ID")

KAFKA_BROKER_URL = parser.get("kafka", "KAFKA_BROKER_URL")
