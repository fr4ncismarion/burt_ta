class CalculatorPage:
    def __init__(self, page):
        self.page = page
        self.field_one = page.locator("#number1")
        self.field_two = page.locator("#number2")
        self.operator_selector = page.locator("#function")
        self.calculate_button = page.locator("#calculate")
        self.result_field = page.locator("#answer")
        self.index_link = page.locator('a[href="index.html"]')
        self.about_link = page.locator('a[href="page?app=simplecalculator&t=About"]')

    def goto(self):
        self.page.goto("https://testpages.eviltester.com/styled/calculator")

    def fill_fields(self, val1, val2):
        self.field_one.fill(str(val1))
        self.field_two.fill(str(val2))

    def select_operator(self, operator):
        self.operator_selector.select_option(operator)

    def calculate(self):
        self.calculate_button.click()

    def get_result_text(self):
        return self.result_field.inner_text()

    def is_result_visible(self):
        return self.result_field.is_visible()
