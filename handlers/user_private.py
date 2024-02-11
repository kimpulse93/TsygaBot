from aiogram import types, Router
from aiogram.filters import CommandStart, Command

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("hayuski")


@user_private_router.message()
async def start_cmd(message: types.Message):
    text = message.text

    if text in ['Привет', 'hi', 'Hello']:
        await message.answer('Хаюшки')
    elif text in ['Bye', 'Пока']:
        await message.answer('Покусики')
    else:
        await message.answer(message.text)
