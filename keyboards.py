
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from callback import vibor_callback
clava = InlineKeyboardMarkup(row_width=5,)

buy_pear = InlineKeyboardButton(text="⬇️⬇️⬇️", callback_data=vibor_callback.new(ani_name="след",))
clava.insert(buy_pear)


btnurlchannel= InlineKeyboardButton(text='подписаться', url='https://t.me/Truetiktok')
btndonesub=InlineKeyboardButton(text='я подписан ', callback_data='subchanneldone')


checkSubm=InlineKeyboardMarkup(row_width=1)
checkSubm.insert(btnurlchannel)
checkSubm.insert(btndonesub)