from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from datetime import date
from lasotuvi.models import LaSoTuVi
from lunardate import LunarDate
from dateutil.relativedelta import relativedelta


def get_lunar_calendar(solar_year, solar_month, solar_day, solar_hour):
    solar_date = date(solar_year, solar_month, solar_day) + relativedelta(days=(not solar_hour % 12))
    solar_date = (solar_date.year, solar_date.month, solar_date.day)
    lunar_date = LunarDate.fromSolarDate(*solar_date)
    return lunar_date


def homepage(request):
    if request.method == 'POST':
        user_info = {
            'ho_ten': request.POST.get('ho_ten'),
            'nam_sinh': int(request.POST.get('nam_sinh')),
            'thang_sinh': int(request.POST.get('thang_sinh')),
            'ngay_sinh': int(request.POST.get('ngay_sinh')),
            'gio_sinh': int(request.POST.get('gio_sinh')),
            'gender': bool(request.POST.get('gioi_tinh')),
            'nam_xem_han': int(request.POST.get('nam_xem_han')),
        }
        lunar_calendar = get_lunar_calendar(user_info['nam_sinh'], user_info['thang_sinh'],
                                            user_info['ngay_sinh'], user_info['gio_sinh'])
        user_info.update({'am_lich': date(lunar_calendar.year, lunar_calendar.month, lunar_calendar.day)})
        LaSoTuVi.insert_la_so_data(user_info)
        return redirect('lasotuvi/')
    else:
        context = {
            'year_range': [i for i in range(1900, date.today().year + 1)],
            'month_range': ["%02d" % i for i in range(1, 13)],
            'end_of_january': [i for i in range(1, 32)],
            'born_hour_range': {
                1: '1h-3h',
                2: '3h-5h',
                3: '5h-7h',
                4: '7h-9h',
                5: '9h-11h',
                6: '11h-13h',
                7: '13h-15h',
                8: '15h-17h',
                9: '17h-19h',
                10: '19h-21h',
                11: '21h-23h',
                12: '23h-1h',
            },
        }
    template_name = loader.get_template('homepage.html')
    return HttpResponse(template_name.render(context, request))


def laso(request):
    lasotuvi = LaSoTuVi.objects.last()
    user_info = {
        'ho_ten': lasotuvi.ho_ten,
        'nam_sinh': lasotuvi.nam_sinh,
        'thang_sinh': lasotuvi.thang_sinh,
        'ngay_sinh': lasotuvi.ngay_sinh,
        'gio_sinh': lasotuvi.gio_sinh,
        'gender': lasotuvi.gender,
        'am_lich': lasotuvi.am_lich,
        'gioi_tinh': lasotuvi.gender,
        'nam_xem_han': lasotuvi.nam_xem_han,
    }
    context = LaSoTuVi.generate_thien_ban(user_info)
    template_name = loader.get_template('laso.html')
    return HttpResponse(template_name.render(context, request))
