from AnonXMusic import app
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import SUPPORT_GROUP, SUPPORT_CHANNEL, OWNER, START_IMG_URL, BOT_USERNAME

# دالة وهمية add_served_user لتجنب الخطأ
async def add_served_user(user_id: int):
   # يمكنك إضافة منطق تخزين المستخدم هنا إذا لزم الأمر
   pass

@app.on_message(
   filters.command(["start", "help"]) & filters.private
)
async def start_(c: Client, message: Message):
   user_id = message.from_user.id
   await add_served_user(user_id)
   await message.reply_photo(
       photo=START_IMG_URL,
       caption=f"""اهلا بك انا بۅت اسميي سيري .
يمڪنني تشغيل الموسيقى في الاتصال .
ادعم التشغيل في الكروبات والقنوات .
⎯ ⎯ ⎯ ⎯""",
       reply_markup=InlineKeyboardMarkup(
           [
               [
                   InlineKeyboardButton(text="‹ : الاوامر : ›", callback_data="command_list")
               ],[
                   InlineKeyboardButton(text="‹ : سورس سيري : ›", url=SUPPORT_CHANNEL),
                   InlineKeyboardButton(text="‹ : مطور البوت : ›", user_id=int(OWNER)),
               ],
               [
                   InlineKeyboardButton(text="‹ : اضف البوت الى مجموعتك : ›", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
               ],
           ]
       )
   )


@app.on_callback_query(filters.regex("home_start"))
async def start_set(_, query: CallbackQuery):
   await query.answer("الرئيسية")
   await query.edit_message_text(
       f"""اهلا بك انا بۅت اسميي سيري .
يمڪنني تشغيل الموسيقى في الاتصال .
ادعم التشغيل في الكروبات والقنوات .
⎯ ⎯ ⎯ ⎯""",
       reply_markup=InlineKeyboardMarkup(
           [
               [
                   InlineKeyboardButton(text="‹ : الاوامر : ›", callback_data="command_list")
               ],
               [
                   InlineKeyboardButton(text="‹ : سورس سيري : ›", url=SUPPORT_CHANNEL),
                   InlineKeyboardButton(text="‹ : مطور البوت : ›", user_id=int(OWNER)),
               ],
               [
                   InlineKeyboardButton(text="‹ : اضف البوت الى مجموعتك : ›", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
               ],
           ]
       )
   )


@app.on_callback_query(filters.regex("command_list"))
async def commands_set(_, query: CallbackQuery):
   user_id = query.from_user.id
   await query.answer("الاوامر")
   await query.edit_message_text(
       f"""اهلا بك عـزيـزي اليك قائمة التحكم .
استخـدم الازرار بالاسفـل لـ تصفـح اوامـر البوت .
يمكنك التصال بالمطور اذا كنت تواجه مشكله .
⎯ ⎯ ⎯ ⎯""",
       reply_markup=InlineKeyboardMarkup(
           [
               [
                   InlineKeyboardButton("‹ اوامر  التشغيل ›", callback_data="user_command"),
               ],
               [
                   InlineKeyboardButton("‹ اوامر مطوري ›", callback_data="developer_commands"),
                   InlineKeyboardButton("‹ اوامر المالك ›", callback_data="admin_commands"),
               ],
               [
                   InlineKeyboardButton(" رجوع ", callback_data="home_start"),
               ],
           ]
       )
   )

@app.on_callback_query(filters.regex("user_command"))
async def guide_set(_, query: CallbackQuery):
   await query.answer("قائمــة اوامــر الـتشغـيـل")
   await query.edit_message_text(
       f"""طريقة التشغيل ، تابع في الاسفل ↓

شغل + اسم الاغنية او رابط الاغنية
- لــ تـشـغـيل اغـنـيـة فـي الـمكـالـمـة الـصـوتـيـة .

فيديو + اسم المقـطـع او رابط المقـطـع
- لــ تـشـغـيل فيـديـو فـي الـمكـالـمـة المـرئيـة .

يوت + الاسـم
- لـ تحميـل الاغانـي والمقـاطـع الصوتيـه مـن اليوتيـوب .
⎯ ⎯ ⎯ ⎯
""",
       reply_markup=InlineKeyboardMarkup(
           [
               [
                   InlineKeyboardButton("رجوع", callback_data="command_list")
               ],
           ]
       ),
   )

@app.on_callback_query(filters.regex("admin_commands"))
async def guide_set(_, query: CallbackQuery):
   await query.answer("  قائمــة اوامــر الادمــن")
   await query.edit_message_text(
       f"""
-  قائمــة اوامــر الادمــن .

ايقاف / انهاء / اسكت
- لـ إيقـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة

تخطي
- لـ تخطـي الاغنيـة وتشغيـل الاغنيـة التاليـه

⎯ ⎯ ⎯ ⎯
""",
       reply_markup=InlineKeyboardMarkup(
           [
               [
                   InlineKeyboardButton("رجوع", callback_data="command_list")
               ],
           ]
       ),
   )

@app.on_callback_query(filters.regex("developer_commands"))
async def guide_set(_, query: CallbackQuery):
   if query.from_user.id == int(OWNER):
       await query.answer("اوامر المطورين")
       await query.edit_message_text(
           f"""اوامر المطورين ↓

/addsudo - اضافة مطور
/delsudo - حذف مطور
/reboot - إعادة تشغيل البوت
/update - للتحديث الملفات
/speedtest - سرعة الخادم
/logger [disable | enable] معرفة من يستخدم البوت
/blacklistchat + معرف القناة او المجموعة لحظرها
/whitelistchat + معرف القناة او المجموعة لرفع حظرها
/blacklistedchat - المجموعات والقنوات المحظورة
/block + معرف الشخص لحظره
/unblock + معرف الشخص لرفع حظره
/blockedusers - المحظورين
/gban + معرف الشخص لحظره عام
/ungban + معرف الشخص لالغاء حظره عام
/gbannedusers - المحظورين عام
/broadcast -user -assistant -pin + الرسالة لأذاعتها
⎯ ⎯ ⎯ ⎯
""",
           reply_markup=InlineKeyboardMarkup(
               [
                   [
                       InlineKeyboardButton("رجوع", callback_data="command_list")
                   ],
               ]
           ),
       )
   else:

       await query.answer("لا يمكنك الوصول إلى هذا الزر لأنك لست المطور الرئيسي للبوت.", show_alert=True)
