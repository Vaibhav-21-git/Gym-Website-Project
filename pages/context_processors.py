from django.contrib import messages
from datetime import date
from contact_us.models import Contact_Info
from marketing.utils import Mailchimp
from marketing.models import Marketing, GuestMarketing
from cart.models import Cart
from registers.models import Register
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

def info(request):


    info = Contact_Info.objects.all()
    if 'submit_footer_subscribe' in request.POST:
        
        subscribe_email = request.POST.get('eamil_subscribe',None)
        if len(subscribe_email) != 0:
            email = Marketing.objects.filter(user__email=subscribe_email).first()
            if email is not None:
                if subscribe_email != email.user.email: 
                    guest_email, guset_created = GuestMarketing.objects.get_or_create(guest_email=subscribe_email)
                    if guset_created:
                        Mailchimp().add_email(subscribe_email)
                        messages.success(request, 'ایمیل شما با موفقیت ثبت شد')                
                else:   
                    messages.error(request, 'ایمیل شما قبلا ثبت شده است')
            else:
                guest_email, guset_created = GuestMarketing.objects.get_or_create(guest_email=subscribe_email)
                if guset_created:
                    Mailchimp().add_email(subscribe_email)
                    messages.success(request, 'ایمیل شما با موفقیت ثبت شد')                
                else:   
                    messages.error(request, 'ایمیل شما قبلا ثبت شده است')
                    
    context = {
        'info' : info.first(),
        
    }

    all_users = User.objects.all()
    for user in all_users:
        active_registers , expired_registers = Register.objects.get_user_registers(user)
        for i in expired_registers:
            i.is_expired=True
            i.save()
        
    if request.user.is_authenticated:
        cart_obj, new_obj = Cart.objects.new_or_get(request.user)
        cart_count = cart_obj.selected_class.count() + cart_obj.online_selected_class.count()
        context.update({'cart_count' : cart_count})



    return(context)