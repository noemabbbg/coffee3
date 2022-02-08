from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton



topup=InlineKeyboardMarkup(row_width=1)
pop=InlineKeyboardButton(text="top up", callback_data="popolnit")
subscribechapters=InlineKeyboardButton(text="subcribe to 500+ new videos", callback_data="subscribeALL")
topup.insert(pop)
topup.insert(subscribechapters)
btnreturnmenu=InlineKeyboardButton(text='back to menu', callback_data='returnMenu')


def buy_menu(isUrl=True, url="", bill=""):
    qiwiMenu=InlineKeyboardMarkup(row_width=1)
    if isUrl:
        btnurlqiwi=InlineKeyboardButton(text="pay link", url=url)
        qiwiMenu.insert(btnurlqiwi)
    btncheckqiwi = InlineKeyboardButton(text="check my topup", callback_data="check_"+bill)
    qiwiMenu.insert(btncheckqiwi)
    qiwiMenu.insert(btnreturnmenu)
    return qiwiMenu

confirmkb=InlineKeyboardMarkup(row_width=1)
confirmbtn=InlineKeyboardButton(text="yes", callback_data="confirmpay")
confirmkb.insert(confirmbtn)
confirmkb.insert(btnreturnmenu)
