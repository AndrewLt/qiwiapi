# -*- coding: utf-8 -*-

from telebot import *
from constants import *
import qiwi_lib
import random
import os

bot = TeleBot(token)

ADMIN_LOGIN = 0
ADD_MORE_GOODS = 0
EDIT_PRISE = 0
EDIT_NAME = 0

ADD_NEW_GOODS = 0

upd = bot.get_updates()  # запрос всех обновлений
last_upd = upd[-1]  # запрос последнего обновления
message_from_user = last_upd.message  # сообщение из последнего обновления

@bot.message_handler(commands=['start', 'admin'])
def handle_command(message):
    user_markup = types.ReplyKeyboardMarkup(True, True)
    user_markup.add('💎 Перейти к покупкам')
    user_markup.add('📱 Обратна связь')
    user_markup.add('❗️ Информация')
    bot.send_message(message.chat.id, "Добро пожаловать", reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def any_message(message):
    if message.text == '💎 Перейти к покупкам':
        global keybord_goods
        keybord_goods = types.InlineKeyboardMarkup()
        main_goods_keybord = [types.InlineKeyboardButton(text=NAME_OF_GOODS[0], callback_data='goods_key_0'),
                              types.InlineKeyboardButton(text=NAME_OF_GOODS[1], callback_data='goods_key_1'),
                              types.InlineKeyboardButton(text=NAME_OF_GOODS[2], callback_data='goods_key_2'),
                              types.InlineKeyboardButton(text=NAME_OF_GOODS[3], callback_data='goods_key_3'),
                              types.InlineKeyboardButton(text=NAME_OF_GOODS[4], callback_data='goods_key_4'),
                              types.InlineKeyboardButton(text=NAME_OF_GOODS[5], callback_data='goods_key_5'),
                              types.InlineKeyboardButton(text=NAME_OF_GOODS[6], callback_data='goods_key_6'),
                              types.InlineKeyboardButton(text=NAME_OF_GOODS[7], callback_data='goods_key_7'),
                              types.InlineKeyboardButton(text=NAME_OF_GOODS[8], callback_data='goods_key_8'),
                              types.InlineKeyboardButton(text=NAME_OF_GOODS[9], callback_data='goods_key_9'),
                              types.InlineKeyboardButton(text='🔙Назад', callback_data='nazad')]

        for i in range(0, 10):
            if os.stat(GOODS_LIST[i]).st_size > 0:
                keybord_goods.add(main_goods_keybord[i])
        keybord_goods.add(main_goods_keybord[10])


        bot.send_message(message.chat.id, '🔸   Выберите товар из списка   🔸', reply_markup=keybord_goods)

    if message.text == '📱 Обратна связь':
        bot.send_message(message.chat.id, '📱 для обратной связи напишите сюда @Operatordp')
    if message.text == '❗️ Информация':
        bot.send_message(message.chat.id, 'Бот для автоматических продаж, создан специально для  \n' + THE_CREATOR)
# --------------------------------------------------------------------------------------------------------
    if message.text == '✅Я оплатил':
        for i in range(0, 10):
            if qiwi_lib.last_upd['data'][i]['comment'] == comment_random():
                bot.send_message(message.chat.id, '😘Спасибо за покупку!')
                f = open(a_s, 'r+')
                line = f.readline()
                bot.send_message(message.chat.id, line)
        else:
            bot.send_message(message.chat.id, 'Если вы оплатили, а получить товар так и не получилось, то:\n'
                                              '1. Сделайте скрин выставленого счета\n'
                                              '2. Отпишите в обратную связь')
    if message.text == '❌Назад':
        user_markup = types.ReplyKeyboardMarkup(True, True)
        user_markup.add('💎 Перейти к покупкам')
        user_markup.add('📱 Обратна связь')
        user_markup.add('❗️ Информация')
        bot.send_message(message.chat.id, "Добро пожаловать", reply_markup=user_markup)
    if message.text == 'ADMIN':
        bot.send_message(message.chat.id, '⚠️Введите Ваш токен!')
    if message.text == str(BOT_TOKEN):
        global ADMIN_LOGIN
        ADMIN_LOGIN = 1
        global keyboard_adm
        keyboard_adm = types.InlineKeyboardMarkup()
        main_admin_button = [types.InlineKeyboardButton(text="🔨Редактрировать товар", callback_data='edit_t'),
                             types.InlineKeyboardButton(text='➕Добавить товар', callback_data='add_new_goods'),
                             types.InlineKeyboardButton(text='🔙Назад', callback_data='admin_back')]
        keyboard_adm.add(main_admin_button[0])
        keyboard_adm.add(main_admin_button[1])
        keyboard_adm.add(main_admin_button[2])
        bot.send_message(message.chat.id, "⚠️Внимание, Вы находитесь в режиме администратора⚠️", reply_markup=keyboard_adm)
#------------------------------------[ADD GOODS]--------------------------------------------
    if 'ID' in message.text and ADD_MORE_GOODS == 1:
        for i in range(0, 10):
            if ('ID' + str(i)) in message.text and ADMIN_LOGIN == 1:
                list_to_add = open(GOODS_LIST[i], 'a')
                list_to_add.write(message.text + '\n')
                list_to_add.close()
                bot.send_message(message.chat.id, '👍🏻Готово!')
    if 'ID' in message.text and EDIT_PRISE == 1:
        for i in range(0, 10):
            if ('ID'+str(i)) in message.text and ADMIN_LOGIN == 1:
                PRISE_OF_GOODS[i] = message.text.replace('ID' + str(i) + ':', '')
                bot.send_message(message.chat.id, '👍🏻Готово!')
    if 'ID' in message.text and EDIT_NAME == 1:
        for i in range(0, 10):
            if ('ID'+str(i)) in message.text and ADMIN_LOGIN == 1:
                NAME_OF_GOODS[i] = message.text.replace('ID' + str(i) + ':', '')
                bot.send_message(message.chat.id, '👍🏻Готово!')
    if 'ID' in message.text and ADD_NEW_GOODS == 1:
        for i in range(0, 10):
            if ('ID'+str(i)) in message.text and ADMIN_LOGIN == 1:
                NAME_OF_GOODS[i] = message.text.replace('ID' + str(i) + ':', '')
                bot.send_message(message.chat.id, '👍🏻Готово!')


@bot.callback_query_handler(func=lambda call: True)
def deff(call):
    if call.message:
#--------------------------------------------[РЕДАКТИРОВАНИЕ ТОВАРА]----------------------------------------------------
        if call.data == 'edit_t':
            keyboard = types.InlineKeyboardMarkup()
            edit_goods_button = [types.InlineKeyboardButton(text='🔧Изменить название товара', callback_data='edit_name'),
                          types.InlineKeyboardButton(text="💵Изменить цену товара", callback_data='edit_prise'),
                          types.InlineKeyboardButton(text='📦Пополнить товара', callback_data='add_goods'),
                          types.InlineKeyboardButton(text='🔙Вернутся назад', callback_data='edit_back')]
            keyboard.add(edit_goods_button[0], edit_goods_button[1])
            keyboard.add(edit_goods_button[2])
            keyboard.add(edit_goods_button[3])
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='🔹Редактрирование товара. Выберите нужное из списка🔹', reply_markup=keyboard)
        if call.data == 'edit_name':
            global EDIT_NAME
            EDIT_NAME = 1
            bot.send_message(call.message.chat.id, '▫️Введитt ID товара и новую цену'
                                                   'в формате "IDномер:название товара"▫️')
        if call.data == 'edit_prise':
            global EDIT_PRISE
            EDIT_PRISE = 1
            bot.send_message(call.message.chat.id, '▫️Введитt ID товара и новую цену'
                                                   'в формате "IDномер:цена товара"▫️')
        if call.data == 'add_goods':
            global ADD_MORE_GOODS
            ADD_MORE_GOODS = 1
            bot.send_message(call.message.chat.id, '▫️Введитt ID товара и строку которую хотите добавить'
                                                   'в формате "IDномер:строка которую нужно добавить"▫️')
        if call.data == 'edit_back':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="⚠️Внимание, Вы находитесь в режиме администратора⚠️", reply_markup=keyboard_adm)
#--------------------------------------------------[ДОБАВИТЬ ТОВАР]-----------------------------------------------------
        if call.data == 'add_new_goods':
            global ADD_NEW_GOODS
            ADD_NEW_GOODS = 1
            bot.send_message(call.message.chat.id, '▫️Для добавления нового товара введите не зайнятый ID (от 0 до 9)'
                                                   'и название товара в формате "IDномер:НАЗВАНИЕ ТОВАРА"'
                                                   'Пополнение товара и выставление цены осуществляется в разделе'
                                                   '"Редактировать товар"▫️')
#--------------------------------------------------[ПОКУПКА ТОВАРА]-----------------------------------------------------
        for i in range(0, 10):
            if call.data == 'goods_key_'+str(i):
                forming_check(PRISE_OF_GOODS[i], call.message, NAME_OF_GOODS[i])
                global a_s
                a_s = GOODS_LIST[i]
                keyboard_pay = types.ReplyKeyboardMarkup(True, True)
                keyboard_pay.row('✅Я оплатил')
                keyboard_pay.row('❌Назад')
                bot.send_message(call.message.chat.id, 'Если передумали покупать, нажмите "Назад"',
                                 reply_markup=keyboard_pay)
#-----------------------------------------------------------------------------------------------------------------------
        if call.data == 'admin_back':
            user_markup = types.ReplyKeyboardMarkup(True, True)
            user_markup.add('💎 Перейти к покупкам')
            user_markup.add('📱 Обратна связь')
            user_markup.add('❗️ Информация')
            bot.send_message(call.message.chat.id, "Добро пожаловать", reply_markup=user_markup)
#-----------------------------------------------------------------------------------------------------------------------
        if call.data == 'nazad':
            user_markup = types.ReplyKeyboardMarkup(True, True)
            user_markup.add('💎 Перейти к покупкам')
            user_markup.add('📱 Обратна связь')
            user_markup.add('❗️ Информация')
            bot.send_message(call.message.chat.id, "Добро пожаловать", reply_markup=user_markup)



def forming_check(sum_of_pay, def_mes, value):
    bot.send_message(def_mes.chat.id, '!Выставленый счет!\n Вы покупаете товар ' + value +
"""\n➖➖➖➖➖➖➖➖➖➖
Совершите платеж на QIWI в течение 5 минут
➖➖➖➖➖➖➖➖➖➖
Кошелек: +380685124286
Сумма: """ + str(sum_of_pay) + """ рублей
Комментарий: """ + str(comment_random()) + """
➖➖➖➖➖➖➖➖➖➖
БЕЗ КОММЕНТАРИЯ ДЕНЬГИ НЕ ЗАЧИСЛЯЮТСЯ""")


def comment_random():
    value = random.randint(100000, 999999)
    return value


bot.polling(none_stop=True, interval=1)