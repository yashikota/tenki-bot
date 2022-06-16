import datetime
import os

from playwright.sync_api import Playwright, sync_playwright


def check_dir():
    if not os.path.exists("./img"):
        os.mkdir("./img")


def run(playwright: Playwright, url: str) -> str:
    browser: Playwright = playwright.chromium.launch(headless=True)
    context: Playwright = browser.new_context()
    date: str = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=9), "JST")
    ).strftime("%Y_%m_%d_%H_%M_%S")
    img_path: str = "./img/" + date + ".png"

    # 新しいウィンドウを開く
    page: Playwright = context.new_page()

    # ページを開く
    page.goto(url, wait_until="load")

    # ページをスクショ
    page.screenshot(path=img_path)

    # 終了
    page.close()
    browser.close()
    context.close()

    return img_path


def playwright_main(url: str) -> str:
    with sync_playwright() as playwright:
        img_path: str = run(playwright, url)

    return img_path


def main() -> str:
    url: str = "https://www.google.com"

    check_dir()
    img_path: str = playwright_main(url)

    return img_path
