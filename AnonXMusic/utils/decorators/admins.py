from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AnonXMusic import app
from AnonXMusic.misc import SUDOERS, db
from AnonXMusic.utils.database import (
    get_authuser_names,
    get_cmode,
    get_lang,
    get_upvote_count,
    is_active_chat,
    is_maintenance,
    is_nonadmin_chat,
    is_skipmode,
)
from config import SUPPORT_CHAT, adminlist, confirmer
from strings import get_string

from ..formatters import int_to_alpha


def AdminRightsCheck(mystic):
    async def wrapper(client, message):
    	
        _ = get_string("en")
        
        if message.command[0] == "تخطي" or message.command[0] == "skip":
        	return await mystic(client, message, _,message.chat.id)
        elif message.command[0] == "ايقاف" or message.command[0] == "stop":
        	return await mystic(client, message, _,message.chat.id)
        

    return wrapper


def AdminActual(mystic):
    async def wrapper(client, message):
        await message.delete()
        _ = get_string("en")
        if message.command == "تخطي" or message.command == "skip":
        	pass
        elif message.command == "ايقاف" or message.command == "stop":
        	return await mystic(client, message, _,message.chat.id)

    return wrapper


def ActualAdminCB(mystic):
    async def wrapper(client, CallbackQuery):
        if await is_maintenance() is False:
            if CallbackQuery.from_user.id not in SUDOERS:
                return await CallbackQuery.answer(
                    "Bot is under maintenance. Please wait for some time...",
                    show_alert=True,
                )
        try:
            language = await get_lang(CallbackQuery.message.chat.id)
            _ = get_string(language)
        except:
            _ = get_string("en")
        if CallbackQuery.message.chat.type == "private":
            return await mystic(client, CallbackQuery, _)
        is_non_admin = await is_nonadmin_chat(
            CallbackQuery.message.chat.id
        )
        if not is_non_admin:
            try:
                a = await app.get_chat_member(
                    CallbackQuery.message.chat.id,
                    CallbackQuery.from_user.id,
                )
            except:
                return await CallbackQuery.answer(
                    _["general_5"], show_alert=True
                )
            if not a.privileges.can_manage_video_chats:
                if CallbackQuery.from_user.id not in SUDOERS:
                    token = await int_to_alpha(
                        CallbackQuery.from_user.id
                    )
                    _check = await get_authuser_names(
                        CallbackQuery.from_user.id
                    )
                    if token not in _check:
                        try:
                            return await CallbackQuery.answer(
                                _["general_5"],
                                show_alert=True,
                            )
                        except:
                            return
        return await mystic(client, CallbackQuery, _)

    return wrapper