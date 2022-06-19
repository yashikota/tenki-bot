import datetime
import os

from playwright.sync_api import Playwright, sync_playwright


class Screenshot:
    def __init__(self) -> None:
        self.url: str = (
            "https://www.data.jma.go.jp/multi/yoho/yoho_detail.html?code=270000&lang=jp"
        )
        self.date: str = datetime.datetime.now(
            datetime.timezone(datetime.timedelta(hours=9), "JST")
        ).strftime("%Y_%m_%d_%H_%M_%S")
        self.img_path: str = "./img/" + self.date + ".png"
        self.main()

    def check_dir(self) -> None:
        if not os.path.exists("./img"):
            os.mkdir("./img")

    def playwright_main(self) -> None:
        with sync_playwright() as playwright:
            self.ss(playwright)

    def ss(self, playwright: Playwright) -> None:
        browser: Playwright = playwright.chromium.launch(headless=True)
        context: Playwright = browser.new_context()

        # 新しいウィンドウを開く
        page: Playwright = context.new_page()

        # ページを開く
        page.goto(self.url, wait_until="load")

        # ページをスクショ
        page.screenshot(path=self.img_path)

        # 終了
        page.close()
        browser.close()
        context.close()

    def main(self) -> str:
        self.check_dir()
        self.playwright_main()

        return self.img_path


if __name__ == "__main__":
    Screenshot().main()
    print("image path: {}".format(Screenshot().img_path))
