from .models import Profile
from django.shortcuts import redirect

def check_profile_middleware(get_response):
    def middleware(request):
        user_profile = Profile.objects.filter(user=request.user)
        print(f"user: {request.user['username']} : Checking profile existing...")
        if not user_profile:
            redirect('MyProfile/create')
        response = get_response(request)
        return  response

    return middleware


