import asyncio
import logging
import os

from aiogram import Bot, Dispatcher

from handlers.wizard import router

logging.basicConfig(level=logging.INFO)


async def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise SystemExit("set BOT_TOKEN (see .env.example)")

    bot = Bot(token)
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
