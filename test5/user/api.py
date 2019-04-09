from django.http import HttpResponse
from lib.sms import send_sms


def submit_phone(request):
    """
    取短信验证码
    """
    if not request.method == "POST":
        return HttpResponse('request method error')

    phone = request.POST.get('phone')
    print(phone)
    result, msg = send_sms(phone)
    print(msg)
    print(result)
    return HttpResponse("submit phone")

def submit_vcode(request):
    """过短信验证码登录注册
    pass
    """
def get_profile(request):
    """取个人资料"""
    pass

def set_profile(request):
    """改个人资料"""
    pass

def upload_avter(request):
    """像上传"""
    pass


