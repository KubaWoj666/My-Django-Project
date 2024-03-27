from django.contrib.auth.decorators import user_passes_test

def admin_required(view_func):
    function_decorator = user_passes_test(
        lambda user: user.is_superuser,
        login_url="shop/",
    )(view_func)
    return function_decorator

