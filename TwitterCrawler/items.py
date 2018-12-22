# -*- coding: utf-8 -*-

# Define here the models for your scraped items
from scrapy import Item, Field


class Tweet(Item):
    ID = Field()
    url = Field()
    datetime = Field()
    text = Field()
    user_id = Field()
    usernameTweet = Field()

    nbr_retweet = Field()
    nbr_favorite = Field()
    nbr_reply = Field()

    is_reply = Field()
    is_retweet = Field()

    has_image = Field()
    images = Field()

    has_video = Field()
    videos = Field()

    has_media = Field()
    medias = Field()

