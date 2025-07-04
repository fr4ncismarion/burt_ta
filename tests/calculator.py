from pages.main import CalculatorPage


# rendering test
def test_validate_buttons(browser_setup):
    page = browser_setup
    calc = CalculatorPage(page)
    assert calc.field_one.is_visible()
    assert calc.field_two.is_visible()
    assert calc.operator_selector.is_visible()
    assert calc.calculate_button.is_visible()

# rendering test 2
def test_validate_hyperlinks(browser_setup):
    page = browser_setup
    calc = CalculatorPage(page)
    assert calc.index_link.is_visible()
    assert calc.about_link.is_visible()

# functionality test
def test_calculate_operator(browser_setup):
    page = browser_setup
    calc = CalculatorPage(page)
    value_1 = 10
    value_2 = 10

    calc.fill_fields(value_1, value_2)

    for operator, expected in {
        "plus": value_1 + value_2,
        "minus": value_1 - value_2,
        "times": value_1 * value_2,
        "divide": value_1 / value_2
    }.items():
        calc.select_operator(operator)
        calc.calculate()
        assert calc.is_result_visible()
        assert float(calc.get_result_text()) == float(expected), f"{operator} failed"

# functionaltity test 2
def test_calculate_invalid_input(browser_setup):
    page = browser_setup
    calc = CalculatorPage(page)

    calc.fill_fields("abc", "xyz")
    calc.calculate()
    assert calc.is_result_visible()
    assert calc.get_result_text() == "ERR"
