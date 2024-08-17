def test_check_women_sales_url(sales):
    sales.open_page()
    sales.items('https://magento.softwaretestingboard.com/promotions/women-sale.html')


def test_check_jackets_title(sales):
    sales.open_page()
    sales.jackets()


def test_add_to_compare_and_delete(sales):
    sales.open_page()
    sales.compare_delete()
