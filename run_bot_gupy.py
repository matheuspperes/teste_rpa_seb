from playwright.sync_api import sync_playwright
from pathlib import Path
import logging, uuid

from bot_gupy.start_robot import Bot


log_path = str(Path(__file__).parent / "bot_gupy" / "bot_gupy.log")
logging.basicConfig(filename=log_path, level=logging.INFO, format='%(asctime)s| [%(levelname)s]: %(message)s')

if __name__ == '__main__':
    bot = Bot()
    with sync_playwright() as playwright:
        bot.run(playwright, uuid.uuid4())