import asyncio
import logging
import os
import sys

import requests
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode, ContentType
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from dotenv import load_dotenv
from functions import get_info

load_dotenv()

TOKEN = os.getenv("RANDOMISE_TOKEN")
LINK = os.getenv('API_LINK')
WINNER_API = os.getenv('WINNER_API')
OPPONENT_API = os.getenv('OPPONENT_API')
LOOSER_API = os.getenv('LOOSER_API')
REWARD_API = os.getenv('REWARD_API')

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


class Opponent:
    opponents = []


class Tournament(StatesGroup):
    begin = State()


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    try:
        combats = get_info.find_opponents(LINK)
        Opponent.opponents = combats
        await message.answer('\n'.join(combats))
        begun = ReplyKeyboardMarkup(resize_keyboard=True,
                                    keyboard=[[KeyboardButton(text='Begin')]])
        await message.answer('👇🏻👇🏻', reply_markup=begun)
        await state.set_state(Tournament.begin)
    except:
        await message.answer('Tournament is over')
        response = requests.get(LINK).json()
        for i in response:
            await message.answer(f"{i['fullname']} -> {i['nickname']} -> {i['status']}")


@dp.message(F.content_type == ContentType.TEXT, Tournament.begin)
async def begin(message: Message) -> None:
    if message.text != 'Begin':
        await message.answer(f'Winner is {message.text}')
        get_info.choose_winner(message.text, LINK, WINNER_API, REWARD_API)
    if len(Opponent.opponents) > 0:
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
            [KeyboardButton(text=Opponent.opponents[0].split('-')[0]),
             KeyboardButton(text=Opponent.opponents[0].split('-')[1])]
        ])
        get_info.send_notification(Opponent.opponents[0].split('-')[0], Opponent.opponents[0].split('-')[1],
                                   OPPONENT_API, LINK)
        await choose_winner(keyboard)
    else:
        await message.answer('<b>This stage is over</b>', reply_markup=ReplyKeyboardRemove())
        get_info.delete_users(LINK, LOOSER_API, REWARD_API)


async def choose_winner(keyboard, state: FSMContext = None):
    await bot.send_message(1274378031, 'Choose the winner:', reply_markup=keyboard)
    Opponent.opponents.remove(Opponent.opponents[0])
    await state.set_state(Tournament.begin)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


