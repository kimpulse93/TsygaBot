import asyncio
from aiogram import F, Dispatcher, Bot, types

from config import TOKEN_API
from handlers.user_private import user_private_router
from common.bot_cmds_list import private

bot = Bot(TOKEN_API)
dp = Dispatcher()

dp.include_router(user_private_router)
ALLOWED_UPDATES = ['message, edited_message']



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())
