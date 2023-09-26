from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from config import bot
from keyboards import inline_buttons
from database.sql_commands import Database


class ReportState(StatesGroup):
    report = State()


async def report_start_report(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text='Вы хотите пожаловаться на участника группы?',
        reply_markup=await inline_buttons.two_button_inline_markup(
            text=['Да', "Нет я передумал"],
            callback=['yeas', 'no'])
    )
