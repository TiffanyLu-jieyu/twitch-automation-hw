from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.streamer_page import StreamerPage
import time


def test_search_starcraft_ii(driver):
    home_page = HomePage(driver)
    search_page = SearchPage(driver)
    streamer_page = StreamerPage(driver)

    home_page.open()
    home_page.click_browse()

    search_page.enter_search_keyword("StarCraft II")
    search_page.submit_search()
    time.sleep(2)
    search_page.scroll_down(times=2)
    search_page.select_streamer()

    streamer_page.wait_until_loaded()
    streamer_page.save_screenshot("screenshots/streamer_page.png")

    assert True