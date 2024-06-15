from django.contrib.auth.decorators import user_passes_test

def group_required(group_name):
    def decorator(view_func):
        @user_passes_test(lambda user: user.is_authenticated and user.groups.filter(name=group_name).exists())
        def _wrapped_view(request, *args, **kwargs):
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
