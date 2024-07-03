
from pyrogram.types import InlineKeyboardButton


def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text="• تحمـيل صـوت •",
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text="• تحمـيل فيـديو •",
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="• أغـلاق •", callback_data="close"
            ),
        ],
    ]
    return buttons
