class GuestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            request.session['is_guest'] = True
        response = self.get_response(request)
        return response