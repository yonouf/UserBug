# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.h(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("Invalid CMD...!!! Are u Blind ???")
    else:
        await event.edit(".h <module name> for Detail or .<module> Retrieves All Available CMD.")
        string = ""
        for i in CMD_HELP:
            string += "" + str(i)
            string += " ⊙ "
        await event.edit(string)

@register(outgoing=True, pattern="^.admin$")
async def dumper(dumber):
    await dumber.edit("⊙ 𝐀𝐃𝐌𝐈𝐍 ⊙\n
                      \n⊙ .k ⊙ .b ⊙ .ub ⊙ .pin ⊙ .m ⊙ .um ⊙ .lo ⊙\
                      \n⊙ .ul ⊙ .pro ⊙ .dem ⊙ .zo ⊙ .ads ⊙ .us ⊙\
                      \n⊙ Help : .h 𝐀𝐃𝐌𝐈𝐍 for Details ⊙")
    
CMD_HELP.update({
    "admin":
	"⊙ 𝐀𝐃𝐌𝐈𝐍 ⊙\n
	\n⊙ .ads .us : Admins & Users Lists ⊙ .b .ub : Ban & Unban ⊙\
	\n⊙ .k : Kick ⊙ .pin : Pin Messages ⊙ .m .um : Mute & Unmute ⊙\
	\n⊙ .pro .dem : Promote & Demote ⊙ .zo : Scan & Clean Zombies ⊙\
	\n⊙ .lo .ul : Lock & Unlock ⊙ Types : all, msg, media, sticker, gif,\
	\ngame, inline, poll, invite, pin, info ⊙"})

@register(outgoing=True, pattern="^.download$")
async def dumoer(dumocer):
    await dumocer.edit("⊙ 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃 ⊙\n
                       \n⊙ .ar ⊙ .aw ⊙ .dw ⊙ .upd ⊙ .up ⊙ .uas ⊙ .ra ⊙ .rv ⊙\
                       \n⊙ .gd ⊙ .li ⊙ .di ⊙ .am ⊙ .at ⊙ .sgd ⊙ .au ⊙ .ac ⊙ .ap ⊙\
                       \n⊙ Help : .h 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃 for Details ⊙")
    
CMD_HELP.update({
	"download":
	"⊙ 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃 ⊙\n
	\n⊙ .dw Download ⊙ .upd Uploadir ⊙ .up Upload ⊙ .uas Upload as ⊙ .at Torrent ⊙\
	\n⊙ .au URL ⊙ .am Magnet ⊙ .ac Clear ⊙ .ap Pause ⊙ .ar Resume ⊙ .aw Show ⊙\
	\n⊙ .gd Upload to GD ⊙ .li Files on GD ⊙ .sgd Set GD ⊙ .ra Rip Audio ⊙ .rv Rip Video ⊙\
	\n⊙ .di Direct URLs GDrive Mega CMail Yandex AFH Zippy MF SF OSDN GitHub ⊙"})

@register(outgoing=True, pattern="^.sgd$")
async def dumier(dumoler):
    await dumoler.edit("⊙ 𝐆𝐃𝐑𝐈𝐕𝐄 ⊙\n
		       \n⊙ .gd <file_path / reply / URL|file_name> ⊙\
		       \n⊙ Usage: Uploads the file in reply, URL or file path in server to your GDrive ⊙\
		       \n⊙ .li <query> ⊙\
		       \n⊙ Usage : Looks for files and folders in your GDrive ⊙\
		       \n⊙ .gsetf <GDrive Folder URL> ⊙\
		       \n⊙ Usage : Sets the folder to upload new files to ⊙\
		       \n⊙ .gsetclear ⊙\
		       \n⊙ Usage : Reverts to default upload destination ⊙\
		       \n⊙ .gfolder ⊙\
		       \n⊙ Usage : Shows your current upload destination/folder ⊙\
		       \n⊙ .ggd <path_to_folder_in_server> ⊙\
		       \n⊙ Usage : Uploads all the files in the directory to a folder in GDrive ⊙")

@register(outgoing=True, pattern="^.memes$")
async def dumeer(dumwer):
    await dumwer.edit("⊙ 𝐌𝐄𝐌𝐄𝐒 ⊙\n
                      \n⊙ .rpf ⊙ .acf ⊙ .rcf ⊙ .f ⊙ .ly ⊙ .ty ⊙\
                      \n⊙ .Oof ⊙ .hi ⊙ .str ⊙ .sl ⊙ .ka ⊙ .stk ⊙\
                      \n⊙ .rb ⊙ .ca ⊙ .oub ⊙ .shalom ⊙\
                      \n⊙ Help : .h 𝐌𝐄𝐌𝐄𝐒 for Details ⊙")

CMD_HELP.update({
    "memes":
	"⊙ 𝐌𝐄𝐌𝐄𝐒 ⊙\n
	\n⊙ .rpf Lydia reply ⊙ .acf Lydia add ⊙ .rcf Lydia Remove ⊙ .ly Fake Link ⊙\
	\n⊙ .ty Type ⊙ .sl Slaps ⊙ .str Stretch ⊙ .f Big f**k ⊙ .hi Say Hai ⊙\
	\n⊙ .ka Kang Stickers ⊙ .stk Stickers Info ⊙ .rb Remove BG ⊙ .ca Carbon ⊙\
	\n⊙ .oub OpenUserBot ⊙ .shalom Shalom ⊙"})

@register(outgoing=True, pattern="^.info$")
async def dumler(dumger):
    await dumger.edit("⊙ 𝐈𝐍𝐅𝐎 ⊙\n
                      \n⊙ .dc ⊙ .speed ⊙ .w ⊙ .sys ⊙ .pip ⊙ .who ⊙ .com ⊙\
                      \n⊙ .sup ⊙ .rp ⊙ .dvc  ⊙ .cn ⊙ .spc ⊙ .git ⊙ .co ⊙\
		      \n⊙ .u ⊙ .t ⊙ .bv ⊙ .sleep ⊙ .shutdown ⊙ .restart ⊙\
                      \n⊙ Help : .h 𝐈𝐍𝐅𝐎 for Details ⊙")

CMD_HELP.update({
    "info":
	"⊙ 𝐈𝐍𝐅𝐎 ⊙\n
	\n⊙ .dc Datacentre ⊙ .speed Test ⊙ .w Weather ⊙ .sys System ⊙\
	\n⊙ .bv Version ⊙ .who Whois ⊙ .co Count Username ⊙ .git Search ⊙\
	\n⊙ .pip Search ⊙ .cn Codename ⊙ .dvc Device ⊙ .spc Specs ⊙\
	\n⊙ .sleep Bot ⊙ .com Community ⊙ .sup Support ⊙ .u Update ⊙\
	\n⊙ .shutdown BOT ⊙ .restart BOT ⊙ .t Terminal ⊙"})

@register(outgoing=True, pattern="^.apps$")
async def dumcer(dumder):
    await dumder.edit("⊙ 𝐀𝐏𝐏𝐒 ⊙\n
                      \n⊙ .i ⊙ .g ⊙ .im ⊙ .wi ⊙ .cu ⊙ .ud ⊙\
                      \n⊙ .tt ⊙ .tr ⊙ .la ⊙ .y ⊙ .ss ⊙\
                      \n⊙ Help : .h 𝐀𝐏𝐏𝐒 for Details ⊙")

CMD_HELP.update({
	"apps":
	"⊙ 𝐀𝐏𝐏𝐒 ⊙\n
	\n⊙ .i Image ⊙ .g Google ⊙ .im Imdb ⊙ .wi Wikipedia ⊙\
	\n⊙ .y YouTube ⊙ .cu Currency ⊙ .ud Dictionary ⊙\
	\n⊙ .tt Text To Speech ⊙ .tr Translate ⊙ .la Language ⊙\
	\n⊙ .ss ScreenShot ⊙"})
                      
@register(outgoing=True, pattern="^.chats$")
async def dumver(dumyer):
    await dumyer.edit("⊙ 𝐂𝐇𝐀𝐓𝐒 ⊙\n
                      \n⊙ .pu ⊙ .purgeme ⊙ .d ⊙ .sd ⊙\
                      \n⊙ .app ⊙ .dap ⊙ .bl ⊙ .ubl ⊙\
                      \n⊙ Help : .h 𝐂𝐇𝐀𝐓𝐒 for Details ⊙")

CMD_HELP.update({
    "chats":
	"⊙ 𝐂𝐇𝐀𝐓𝐒 ⊙\n
	\n⊙ .pu Purge ⊙ .purgeme Purge Me\
	\n⊙ .d Delete ⊙ .sd Self Destruction ⊙\
	\n⊙ .app Approves PM ⊙ .dap Disapproves PM ⊙\
	\n⊙ .bl Blocks PM ⊙ .ubl Unblocks PM ⊙"})
                      
@register(outgoing=True, pattern="^.notes$")
async def dumqer(dumker):
    await dumker.edit("⊙ 𝐍𝐎𝐓𝐄𝐒 ⊙\n
		      \n⊙ .notes ⊙ .clear ⊙ .save ⊙ .rmn ⊙ .sw ⊙ .cw ⊙ .rw ⊙\
		      \n⊙ .fi ⊙ .st ⊙ .fs ⊙ .rmf ⊙ .sn ⊙ .si ⊙ .rs ⊙\
		      \n⊙ Help : .h 𝐍𝐎𝐓𝐄𝐒 for Details ⊙")

CMD_HELP.update({
    "notes":
    "⊙ 𝐍𝐎𝐓𝐄𝐒 ⊙\n
    \n⊙ .fi Filter ⊙ .st Stop Filter ⊙ .fs List Filters ⊙ .rmf Remove Bot Filters ⊙\
    \n⊙ .notes Notes ⊙ .clear Notes ⊙ .save Notes ⊙ .rmn Removes All Bot Notes ⊙\
    \n⊙ .sw Set Welcome ⊙ .cw Check Welcome ⊙ .rw Remove Welcome ⊙\
    \n⊙ .sn Snip ⊙ .si Snips ⊙ .rs Remove Snips ⊙"})
