import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from calculator_page import CalculatorPage


class TestCalculatorPage:

    @pytest.fixture(scope="class")
    def driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=chrome_options)
        yield driver
        driver.quit()

    def test_addition_with_page_object(self, driver):
        page = CalculatorPage(driver)
        page.load_page()

        page.enter_first_number(10)
        page.enter_second_number(5)
        page.select_operation("add")
        page.click_calculate()

        assert "Résultat: 15" in page.get_result()

    def test_subtraction_with_page_object(self, driver):
        page = CalculatorPage(driver)
        page.load_page()

        page.enter_first_number(10)
        page.enter_second_number(3)
        page.select_operation("subtract")
        page.click_calculate()

        assert "Résultat: 7" in page.get_result()

    def test_multiplication_with_page_object(self, driver):
        page = CalculatorPage(driver)
        page.load_page()

        page.enter_first_number(4)
        page.enter_second_number(2)
        page.select_operation("multiply")
        page.click_calculate()

        assert "Résultat: 8" in page.get_result()

    def test_division_with_page_object(self, driver):
        page = CalculatorPage(driver)
        page.load_page()

        page.enter_first_number(8)
        page.enter_second_number(2)
        page.select_operation("divide")
        page.click_calculate()

        assert "Résultat: 4" in page.get_result()