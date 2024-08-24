import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode, ContentType
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from dotenv import load_dotenv
from functions import exist

load_dotenv()

TOKEN = os.getenv("REGISTRATION_TOKEN")
LINK = os.getenv('API_LINK')

dp = Dispatcher()


class GettingInfo(StatesGroup):
    user_id = State()
    fullname = State()
    nickname = State()
    phone_number = State()


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    if exist.is_exist(message.from_user.id, LINK):
        await message.answer(f'Salom {message.from_user.full_name}')
        await message.answer(f'<b>Muhim</b> \n'
                             f"Iltimos ism va familiyangizni to'liq kiriting (g'olib bo'lsangiz u sertifikatga yoziladi)",
                             reply_markup=ReplyKeyboardRemove())
        await state.update_data(user_id=message.from_user.id)
        await state.set_state(GettingInfo.fullname)
    else:
        await message.answer("Siz allaqachon ruyxatdan o'tib bo'lgansiz")
        await message.answer("Iltimos sabrli bo'ling va musobaqani kuting", reply_markup=ReplyKeyboardRemove())


@dp.message(F.content_type == ContentType.TEXT, GettingInfo.fullname)
async def get_fullname(message: Message, state: FSMContext) -> None:
    await message.answer("Endi nickname kiriting (siz uni musobaqa davomida ko'rasiz)",
                         reply_markup=ReplyKeyboardRemove())
    await state.update_data(fullname=message.text)
    await state.set_state(GettingInfo.nickname)


@dp.message(F.content_type == ContentType.TEXT, GettingInfo.nickname)
async def get_nickname(message: Message, state: FSMContext) -> None:
    if exist.check_nickname(message.text, LINK):
        phone = ReplyKeyboardMarkup(resize_keyboard=True,
                                    keyboard=[[KeyboardButton(text='Raqamni ulashish', request_contact=True)]])
        await message.answer("Endi raqamizni ulashing 👇🏻👇🏻 (u kerak bo'lib qolishi mumkin)", reply_markup=phone)
        await state.update_data(nickname=message.text)
        await state.set_state(GettingInfo.phone_number)
    else:
        await message.answer('Bu nickname allaqachon ishlatilgan iltimos boshqasini tanlang')


@dp.message(F.content_type == ContentType.CONTACT, GettingInfo.phone_number)
async def get_nickname(message: Message, state: FSMContext) -> None:
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()
    if exist.save_data(data['user_id'], data['fullname'], data['nickname'], data['phone_number'], LINK):
        await message.answer("Sizning barcha ma'lumotlariz saqlandi. Musobaqani kuting. Omad!",
                             reply_markup=ReplyKeyboardRemove())
        await state.clear()
    else:
        await message.answer("Xatolik ro'y berdi iltimos qayta o'rinib ko'ring /start", reply_markup=ReplyKeyboardRemove())
        await state.clear()


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
