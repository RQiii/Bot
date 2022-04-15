import asyncio
import random
import glob
import re
import shutil
import urllib
import base64
import requests
import time
import shlex
import math
import os
import html
import io
import sys
import traceback
import cv2
from asyncio import sleep
import telethon.password as pwd_mod
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.events import CallbackQuery
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.errors import FloodWaitError
from telethon.tl import functions
from urlextract import URLExtract
from requests import get
from typing import Optional, Tuple
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events
from telethon.utils import pack_bot_file_id, get_input_location
from telethon.tl.custom import Dialog
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import Channel, Chat, User
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from asyncio.exceptions import TimeoutError as AsyncTimeout
from telethon.errors.rpcerrorlist import MessageTooLongError, YouBlockedUserError
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantsBots
from telethon.tl.types import DocumentAttributeVideo as video
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
from telethon.tl.types import InputMessagesFilterMusic
from telethon.tl.functions.messages import SaveDraftRequest
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from ..helpers.progress import humanbytes as hb
from userbot.utils import admin_cmd, sudo_cmd, eor
from telethon.utils import get_display_name
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from ..helpers.utils import reply_id as rd
from telethon.tl.types import Channel, Chat, InputPhoto, User
from userbot import iqthon
from userbot.core.logger import logging
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from . import ALIVE_NAME, AUTONAME, BOTLOG, BOTLOG_CHATID, DEFAULT_BIO, get_user_from_event
from ..helpers import get_user_from_event, reply_id
from ..sql_helper.locks_sql import *
from ..helpers.functions import deEmojify, hide_inlinebot, waifutxt
from userbot.utils.decorators import register
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format
from userbot.helpers.functions import convert_toimage,    deEmojify,    phcomment,    threats,    trap,    trash
from userbot.helpers.functions import convert_tosticker,    flip_image,    grayscale,    invert_colors,    mirror_file,    solarize
from ..sql_helper.global_list import add_to_list, get_collection_list, is_in_list, rm_from_list
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..sql_helper.locks_sql import *

@iqthon.on(admin_cmd(outgoing=True, pattern="ص1$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois1:
        await vois.client.send_file(vois.chat_id, iqvois1, reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص2$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois2:
        await vois.client.send_file(vois.chat_id, iqvois2, reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص3$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois3:
        await vois.client.send_file(vois.chat_id, iqvois3, reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص5$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois5:
        await vois.client.send_file(vois.chat_id, iqvois5, reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص6$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois6:
        await vois.client.send_file(vois.chat_id, iqvois6, reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص7$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois7:
        await vois.client.send_file(vois.chat_id, iqvois7, reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص8$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois:
        await vois.client.send_file(vois.chat_id, iqvois, reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص9$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois9 :
        await vois.client.send_file(vois.chat_id, iqvois9 , reply_to=Ti)
        await vois.delete()

@iqthon.on(admin_cmd(outgoing=True, pattern="ص10$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois10:
        await vois.client.send_file(vois.chat_id, iqvois10 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص11$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois11 :
        await vois.client.send_file(vois.chat_id, iqvois11 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص12$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois12:
        await vois.client.send_file(vois.chat_id, iqvois12 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص13$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois13:
        await vois.client.send_file(vois.chat_id, iqvois13 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص14$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois14:
        await vois.client.send_file(vois.chat_id, iqvois14 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص15$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois15:
        await vois.client.send_file(vois.chat_id, iqvois15 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص16$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois16:
        await vois.client.send_file(vois.chat_id, iqvois16 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص17$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois17:
        await vois.client.send_file(vois.chat_id, iqvois17 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص18$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois18:
        await vois.client.send_file(vois.chat_id, iqvois18 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص19$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois19:
        await vois.client.send_file(vois.chat_id, iqvois19 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص20$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois20:
        await vois.client.send_file(vois.chat_id, iqvois20 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص21$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois21:
        await vois.client.send_file(vois.chat_id, iqvois21 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص22$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois22:
        await vois.client.send_file(vois.chat_id, iqvois22 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص23$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois23:
        await vois.client.send_file(vois.chat_id, iqvois23 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص24$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois24:
        await vois.client.send_file(vois.chat_id, iqvois24 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص25$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois25:
        await vois.client.send_file(vois.chat_id, iqvois25 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص26$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois26:
        await vois.client.send_file(vois.chat_id, iqvois26 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص27$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois27:
        await vois.client.send_file(vois.chat_id, iqvois27 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص28$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois28:
        await vois.client.send_file(vois.chat_id, iqvois28 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص29$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois29:
        await vois.client.send_file(vois.chat_id, iqvois29 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص30$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois30:
        await vois.client.send_file(vois.chat_id, iqvois30 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص31$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois31:
        await vois.client.send_file(vois.chat_id, iqvois31 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص32$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois32:
        await vois.client.send_file(vois.chat_id, iqvois32 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص33$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois33:
        await vois.client.send_file(vois.chat_id, iqvois33 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص34$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois34:
        await vois.client.send_file(vois.chat_id, iqvois34 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص35$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois35:
        await vois.client.send_file(vois.chat_id, iqvois35 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص36$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois36:
        await vois.client.send_file(vois.chat_id, iqvois36 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص37$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois37:
        await vois.client.send_file(vois.chat_id, iqvois37 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص38$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois38:
        await vois.client.send_file(vois.chat_id, iqvois38 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص39$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois39:
        await vois.client.send_file(vois.chat_id, iqvois39 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص40$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois40:
        await vois.client.send_file(vois.chat_id, iqvois40 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص41$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois41:
        await vois.client.send_file(vois.chat_id, iqvois41 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص42$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois42:
        await vois.client.send_file(vois.chat_id, iqvois42 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص43$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois43:
        await vois.client.send_file(vois.chat_id, iqvois43 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص44$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois44:
        await vois.client.send_file(vois.chat_id, iqvois44 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص45$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois45:
        await vois.client.send_file(vois.chat_id, iqvois45 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص46$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois46:
        await vois.client.send_file(vois.chat_id, iqvois46 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص47$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois47:
        await vois.client.send_file(vois.chat_id, iqvois47 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص48$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois48:
        await vois.client.send_file(vois.chat_id, iqvois48 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص49$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois49:
        await vois.client.send_file(vois.chat_id, iqvois49 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص50$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois50:
        await vois.client.send_file(vois.chat_id, iqvois50 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص51$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois51:
        await vois.client.send_file(vois.chat_id, iqvois51 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص52$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois52:
        await vois.client.send_file(vois.chat_id, iqvois52 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص55$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois55:
        await vois.client.send_file(vois.chat_id, iqvois55 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص54$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois54:
        await vois.client.send_file(vois.chat_id, iqvois54 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص56$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois56:
        await vois.client.send_file(vois.chat_id, iqvois56 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص53$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois53:
        await vois.client.send_file(vois.chat_id, iqvois53 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص57$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois57:
        await vois.client.send_file(vois.chat_id, iqvois57 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص58$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois58:
        await vois.client.send_file(vois.chat_id, iqvois58 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص59$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois59:
        await vois.client.send_file(vois.chat_id, iqvois59 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص60$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois60:
        await vois.client.send_file(vois.chat_id, iqvois60 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص61$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois61:
        await vois.client.send_file(vois.chat_id, iqvois61 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص62$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois62:
        await vois.client.send_file(vois.chat_id, iqvois62 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص63$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois63:
        await vois.client.send_file(vois.chat_id, iqvois63 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص64$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois64:
        await vois.client.send_file(vois.chat_id, iqvois64 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص65$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois65:
        await vois.client.send_file(vois.chat_id, iqvois65 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص66$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois66:
        await vois.client.send_file(vois.chat_id, iqvois66 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص67$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois67:
        await vois.client.send_file(vois.chat_id, iqvois67 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص68$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois68:
        await vois.client.send_file(vois.chat_id, iqvois68 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص69$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois69:
        await vois.client.send_file(vois.chat_id, iqvois69 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص70$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois70:
        await vois.client.send_file(vois.chat_id, iqvois70 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص71$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois71:
        await vois.client.send_file(vois.chat_id, iqvois71 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص72$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois72:
        await vois.client.send_file(vois.chat_id, iqvois72 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص73$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois73:
        await vois.client.send_file(vois.chat_id, iqvois73 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص74$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois74:
        await vois.client.send_file(vois.chat_id, iqvois74 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص75$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois75:
        await vois.client.send_file(vois.chat_id, iqvois75 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص76$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois76:
        await vois.client.send_file(vois.chat_id, iqvois76 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص77$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois77:
        await vois.client.send_file(vois.chat_id, iqvois77 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص78$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois78:
        await vois.client.send_file(vois.chat_id, iqvois78 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص79$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois79:
        await vois.client.send_file(vois.chat_id, iqvois79 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص80$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois80:
        await vois.client.send_file(vois.chat_id, iqvois80 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص81$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois81:
        await vois.client.send_file(vois.chat_id, iqvois81 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص82$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois82:
        await vois.client.send_file(vois.chat_id, iqvois82 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص83$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois83:
        await vois.client.send_file(vois.chat_id, iqvois83 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص84$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois84:
        await vois.client.send_file(vois.chat_id, iqvois84 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص85$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois85:
        await vois.client.send_file(vois.chat_id, iqvois85 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص86$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois86:
        await vois.client.send_file(vois.chat_id, iqvois86 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص87$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois87:
        await vois.client.send_file(vois.chat_id, iqvois87 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص88$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois88:
        await vois.client.send_file(vois.chat_id, iqvois88 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص89$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois89:
        await vois.client.send_file(vois.chat_id, iqvois89 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص90$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois90:
        await vois.client.send_file(vois.chat_id, iqvois90 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص91$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois92:
        await vois.client.send_file(vois.chat_id, iqvois93 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص92$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois92:
        await vois.client.send_file(vois.chat_id, iqvois92 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص93$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois93:
        await vois.client.send_file(vois.chat_id, iqvois93 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص94$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois94:
        await vois.client.send_file(vois.chat_id, iqvois94 , reply_to=Ti)
        await vois.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="ص95$"))
async def iqvois(vois):
    if vois.fwd_from:
        return
    Ti = await rd(vois)
    if iqvois95:
        await vois.client.send_file(vois.chat_id, iqvois95 , reply_to=Ti)
        await vois.delete()
        