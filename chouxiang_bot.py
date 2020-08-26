#!/usr/bin/python3

from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters

import os
import random
import eyed3
import json
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def help(update, context):
    update.message.reply_text(
        '/artist - 显示歌手列表\n'
        '/playlist - 显示歌曲列表\n'
        '/song - 随机播放音乐\n'
        '/song 歌曲名 - 点歌'
    )


def artist(update, context):
    artist_name = ""
    artist_dict = load()
    for key in artist_dict:
        artist_name += "/playlist\t" + str(key) + "\n"
    update.message.reply_text(artist_name)


def playlist(update, context):
    # artist_name = update.message.text[len("/playlist "):]
    playlist_name = ""
    path = '/home/i/telegram/assets/'
    if not update.message.text.count(' '):
        update.message.reply_text('用法: /playlist 歌手名 (如 /playlist 麻扣)')
    else:
        artist_name = update.message.text.split(" ", 1)[1]
        for file_name in os.listdir(path):
            file_name = file_name[:-4]
            if artist_name in file_name:
                playlist_name += "/song\t" + file_name + "\n"
        update.message.reply_text(playlist_name)


def song(update, context):
    # song_name = update.message.text[len("/song "):]
    path = '/home/i/telegram/assets/'
    if not update.message.text.count(' '):
        file = os.path.join(path, random.choice(os.listdir(path)))
        update.message.reply_audio(open(file, 'rb'))
    else:
        song_name = update.message.text.split(" ", 1)[1]
        for file_name in os.listdir(path):
            if song_name in file_name:
                file = os.path.join(path, file_name)
                update.message.reply_audio(open(file, 'rb'))
                break


def load():
    with open('/home/i/telegram/artist.json', 'r', encoding='utf-8') as fp:
        return json.load(fp)


def main():
    updater = Updater(
        '1348814435:AAHZqQ5pFhwM3_eIOJCf_TdI79XqeUnxYFg', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('artist', artist))
    dp.add_handler(CommandHandler('playlist', playlist))
    dp.add_handler(CommandHandler('song', song))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
