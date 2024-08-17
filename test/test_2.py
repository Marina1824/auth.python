def test_filter(shop_luma):
    shop_luma.open_page()
    shop_luma.filter()


def test_add_to_compare(shop_luma):
    shop_luma.open_page()
    shop_luma.compare_luma()


def test_add_to_wishlist_without_registration(shop_luma):
    shop_luma.open_page()
    shop_luma.wishlist_luma('You must login or register to add items to your wishlist.')
