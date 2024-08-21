def test_select_new_in_filter(shop_luma):
    shop_luma.open_page()
    shop_luma.add_item_to_filter()


def test_add_clothes_to_compare(shop_luma):
    shop_luma.open_page()
    shop_luma.add_item_to_compare()


def test_add_to_wishlist_without_registration(shop_luma):
    shop_luma.open_page()
    shop_luma.add_to_wishlis('You must login or register to add items to your wishlist.')
