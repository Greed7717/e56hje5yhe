# from aiogram import types, Dispatcher
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.dispatcher import FSMContext
# from config import bot
# from keyboards import inline_buttons
# from database.sql_commands import Database
#
#
# class ReportState(StatesGroup):
#     report = State()
#
#
# async def report_start_report(message: types.Message):
#     bot.send_message(
#         chat_id=message.chat.id,
#         text='Вы хотите пожаловаться на участника группы?',
#         reply_markup=await inline_buttons.two_button_inline_markup(
#             text=['Да', "Нет я передумал"],
#             callback=['yeas', 'no'])
#     )
#
#
# async def report_message(call: types.CallbackQuery):
#     await bot.send_message(
#         chat_id=call.message.chat.id,
#         text='напишите username или first_name участника:')
#     await ReportState.report.set()
#
#
# async def choice_report(call: types.CallbackQuery):
#     await bot.send_message(
#         chat_id=call.message.chat.id,
#         text='ok'
#     )
#
#
# async def load_report(message: types.Message, state: FSMContext):
#     async with state .proxy() as data:
#         report = message.text
#         if report:
#             username = await Database().select_username(username=report.replace(("@", "")))
#         if username:
#             await bot.send_message(
#                 chat_id=username[1],
#                 text='На вас поступила жалоба!'
#             )
#         first_name = await Database().async_select_first_name(first_name=report)
#         if first_name:
#             await bot.send_message(
#                 chat_id=username[1],
#                 text='На вас поступила жалоба!')
#         if not username and not first_name:
#             await bot.send_message(
#                 chat_id=message.chat.id,
#                 text='Пользаватель не найден!')
#     await state.finish()
#
#
# def register_report_handler(dp: Dispatcher):
#     dp.register_message_handler(report_start_report, commands=['report'])
#     dp.register_message_handler(report_message, lambda call: call.data == 'yeas')
#     dp.register_message_handler(choice_report, lambda call: call.data == 'no')
#     dp.register_message_handler(load_report, state=ReportState.report)
