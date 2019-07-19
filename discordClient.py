#!/usr/bin/env python3

import os
import sys
import traceback
import discord
from sentence2vec import Sentence2Vec

client = discord.Client()

docsFile = sys.argv[2]

mecabOpt = "-d /usr/lib/mecab/dic/mecab-ipadic-neologd"
if 3 < len(sys.argv):
    mecabOpt = sys.argv[3]

s2v = Sentence2Vec(sys.argv[1], mecabOpt)
s2v.loadDocsFile(docsFile)


def get_channel_by_name(name):
    for channel in client.get_all_channels():
        if str(channel) == name:
            return channel

def answerText(ans):
    txt = ans[0]["a"] + "\n"
    txt += "```"
    for i in range(3 if 3 < len(ans) else len(ans)):
        txt += str(ans[i]["cos"])[:6] + "    " + ans[i]["a"] + "\n"
        txt += "          " + ans[i]["q"] + "\n"
    txt += "```"
    return txt

def genResponse(text):
    res = ""
    lines = text.split("\n")
    cmd = lines[0].split()
    if "/学習" in cmd and 2 < len(lines):
        q = lines[1].strip()
        a = lines[2].strip()
        s2v.qaDic[q] = a
        s2v.saveDocsFile(docsFile)
        s2v.loadDocsFile(docsFile)
        res += "辞書再構築完了\n\n"
        res += answerText(s2v.answers(q))
    else:
        res += answerText(s2v.answers(lines[0].strip()))
    return res

@client.event
async def on_message(message):
    if message.type != discord.MessageType.default:
        return
    if message.author.bot:
        return
    # if message.channel.name == channel_name and message.content.startswith("<@" + str(client.user.id) + ">"):
    replyFlag = "<@" + str(client.user.id) + ">"
    if message.content.startswith(replyFlag):
        text = message.content[len(replyFlag):]
        try:
            res = genResponse(text)
        except Exception as e:
            res = str(e)
            print(traceback.format_exc())
        await message.channel.send(res)


client.run(os.environ["DISCORD_BOT_TOKEN"])
