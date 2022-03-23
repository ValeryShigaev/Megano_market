from dynamic_preferences.registries import global_preferences_registry


# Custom messages codes
SUCCESS_OPTIONS_ACTIVATE = 200
SEND_PRODUCT_REQUEST = 160
CREATE_PRODUCT_ERROR = 150
SUCCESS_DEL_STORE = 110
SUCCESS_DEL_PRODUCT = 100

# Dynamic preferences control
OPTIONS = global_preferences_registry.manager()
