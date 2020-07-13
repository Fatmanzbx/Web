import os
import asyncio
from pyppeteer import launch


async def save_pdf(url, pdf_path):
    browser = await launch(
        {'headless': True, 'dumpio': True, 'autoClose': False, 'args': ['--no-sandbox', '--window-size=1366,850']})
    page = await browser.newPage()
    # 加载指定的网页url
    await page.goto(url)
    # 设置网页显示尺寸
    await page.setViewport({'width': 1920, 'height': 1080})
    await page.pdf({'path': pdf_path})
    await browser.close()


if __name__ == '__main__':
    url = "https://www.google.com"
    pdf_path = os.path.join(os.getcwd(), "example.pdf")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(save_pdf(url, pdf_path))
