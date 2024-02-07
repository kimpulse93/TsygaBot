import asyncio
from aiogram import Dispatcher, Bot, types

TOKEN_API = '6628310306:AAGiOObvTTVswMYaKmVrhsNtMaO5EkLNPOk'

bot = Bot(TOKEN_API)
dp = Dispatcher()



@dp.message()
async def start_cmd(message: types.Message):
    await message.answer("hayuski")






async def main():
    await dp.start_polling(bot)


asyncio.run(main())







