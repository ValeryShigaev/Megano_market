# Корзина

Добавление товара в корзину происходит с любой страницы, где есть товары, по нажатию на иконку с сумкой
В корзину добавляется 1 шт. этого товара. Если в корзине уже есть этот товар, то его количество увеличивается на 1 шт.
При этом количество товара в магазине уменьшается на 1 шт. Если товара в магазине нет, он не добавляется в корзину и не списывается
из магазина.

На странице самой корзины можно изменить количество товара. Например была 1 шт, а мы хотим купить 3.
При нахажатии на udate количество меняется с 1 на 3. При этом из магазина списывается 2 единицы товара.
Если товара в магазине не достаточно, в корзине остается старое количество товара.

Если этот товар продается в другом магазине, то в корзине можно выбрать другой магазин. При обновлении
(update) количество товара в старом магазине увеличится, в новом - спишется, при условии, что товара
в новом магазине длстаточно.

Если в корзине лежит один и тот же товар, но из разных магазинов и мы меняем один из магазинов на другой,
то количество складывается, а вторая позиция удаляется из корзины.

Также при удалении товара из корзины, количество этого товара возвращается в магазин.

При логине анонимного пользователя товары из корзины "сливаются" с корзиной пользователя,
если до этого он был залогинен и собирал корзину.

При регистрации анонима, корзина также "перетекает" в корзину залогиненного пользователя.

Демонстрация добавления, удаления и изменения количества товара в корзине, а также демонстраиция
слияния корзин.