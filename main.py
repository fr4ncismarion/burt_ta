from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture(scope="module")
def browser_setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://testpages.eviltester.com/styled/calculator")
        yield page
        browser.close()
        print("Page loaded successfully")
        
#rendering test
def test_validate_buttons(browser_setup):
    page = browser_setup
    field_one = page.locator("id=number1")
    field_two = page.locator("id=number2")
    function = page.locator("id=function")
    calculate_button = page.locator("id=calculate")
    assert field_one.is_visible(), "Field one is not visible"
    assert field_two.is_visible(), "Field two is not visible"
    assert function.is_visible(), "Function dropdown is not visible"
    assert calculate_button.is_visible(), "Calculate button is not visible"
    
#rendering test 2    
def test_validate_hyperlinks(browser_setup):
    page = browser_setup
    index_links = page.locator('a[href="index.html"]')
    about_links = page.locator('a[href="page?app=simplecalculator&t=About"]')
    assert index_links.is_visible(), "Hyperlink to index.html is not visible"
    assert about_links.is_visible(), "Hyperlink to About page is not visible"
    
#functionality test
def test_calculate_operator(browser_setup):
    page = browser_setup
    field_one = page.locator("id=number1")
    field_two = page.locator("id=number2")
    function = page.locator("id=function")
    calculate_button = page.locator("id=calculate")
    operator_selector = page.locator("id=function")
    result_field = page.locator("#answer")
    
    
    if field_one.is_visible() and field_two.is_visible():
        value_1 = 10
        value_2 = 10

        page.fill("#number1", str(value_1))
        page.fill("#number2", str(value_2))

        # Loop through operators
        for operator, expected_result in {
            "times": value_1 * value_2,
            "plus": value_1 + value_2,
            "minus": value_1 - value_2,
            "divide": value_1 / value_2
        }.items():
            operator_selector.select_option(operator)
            calculate_button.click()

            # Wait and assert result
            assert result_field.is_visible()
            result_text = result_field.inner_text()
            assert result_text == str(expected_result), f"Expected {expected_result}, got {result_text}"
            

       
def test_calculate_invalid_input(browser_setup):
    page = browser_setup
    field_one = page.locator("id=number1")
    field_two = page.locator("id=number2")
    calculate_button = page.locator("id=calculate")
    result_field = page.locator("#answer")

    # Fill in invalid inputs
    page.fill("#number1", "abc")
    page.fill("#number2", "xyz")
    
    # Click calculate
    calculate_button.click()
    
    # Assert that the result field is empty or shows an error
    assert result_field.is_visible()
    result_text = result_field.inner_text()
    assert result_text == "ERR", f"Expected empty result for invalid input, got {result_text}"