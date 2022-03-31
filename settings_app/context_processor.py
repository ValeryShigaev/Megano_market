from dynamic_preferences.registries import global_preferences_registry
from config.settings import CREATE_PRODUCT_ERROR, SUCCESS_DEL_STORE, SUCCESS_DEL_PRODUCT, SUCCESS_OPTIONS_ACTIVATE, \
    SEND_PRODUCT_REQUEST
from orders_app.services import CartService
from orders_app.views import CompareView
from stores_app.forms import ImportForm
from stores_app.models import ProductImportFile


def custom_context(request):

    OPTIONS = global_preferences_registry.manager().by_name()
    cart = CartService(request)
    total = CompareView().get_quantity(request)
    return {
        'SUCCESS_OPTIONS_ACTIVATE': SUCCESS_OPTIONS_ACTIVATE,
        'SEND_PRODUCT_REQUEST': SEND_PRODUCT_REQUEST,
        'CREATE_PRODUCT_ERROR': CREATE_PRODUCT_ERROR,
        'SUCCESS_DEL_STORE': SUCCESS_DEL_STORE,
        'SUCCESS_DEL_PRODUCT': SUCCESS_DEL_PRODUCT,
        'cart': cart,
        'total_compared': total,
        'banners_time_expire': OPTIONS['banners_time_expire']
    }


def stores_context(request):
    """
    Контекст-процессор файлов импорта
    """

    if request.user.is_authenticated:
        import_form = ImportForm()
        import_files = ProductImportFile.objects.filter(user=request.user).order_by('-created_at')
    else:
        import_form = None
        import_files = None
    return {'import_form': import_form, 'imports': import_files}
