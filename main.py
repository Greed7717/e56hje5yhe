from aiogram import executor
from config import dp
from handlers import start, chat_actions, fsm_form, report
from database import sql_commands
from scraper import my_scraper, asyn_scraper


async def onstart_up(_):
    db = sql_commands.Database()
    db.sql_create_tables()


start.register_start_handlers(dp=dp)
fsm_form.register_fsm_form_handlers(dp=dp)
# report.register_report_handler(dp=dp)
# my_scraper.register_scraper(dp=dp)
# asyn_scraper.register_scraper(dp=dp)
chat_actions.register_chat_actions_handlers(dp=dp)

if __name__ == '__main__':
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=onstart_up
    )