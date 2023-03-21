from django.db import models
from datetime import datetime, date

THIEN_CAN = {
    0: 'Canh',
    1: 'Tân',
    2: 'Nhâm',
    3: 'Quý',
    4: 'Giáp',
    5: 'Ất',
    6: 'Bính',
    7: 'Đinh',
    8: 'Mậu',
    9: 'Kỷ'
}

DIA_CHI = {
    0: 'Thân',
    1: 'Dậu',
    2: 'Tuất',
    3: 'Hợi',
    4: 'Tý',
    5: 'Sửu',
    6: 'Dần',
    7: 'Mão',
    8: 'Thìn',
    9: 'Tỵ',
    10: 'Ngọ',
    11: 'Mùi'
}


class LaSoTuVi(models.Model):
    # id = models.IntegerField(primary_key=True)
    ho_ten = models.CharField(max_length=100)
    nam_sinh = models.IntegerField()
    thang_sinh = models.IntegerField()
    ngay_sinh = models.IntegerField()
    gio_sinh = models.IntegerField()
    gender = models.BooleanField()
    nam_xem_han = models.IntegerField()
    am_lich = models.DateField(null=True)

    @classmethod
    def insert_la_so_data(cls, user_info):
        return LaSoTuVi(ho_ten=user_info['ho_ten'], nam_sinh=user_info['nam_sinh'],
                        thang_sinh=user_info['thang_sinh'],
                        ngay_sinh=user_info['ngay_sinh'], gio_sinh=user_info['gio_sinh'],
                        gender=user_info['gender'],
                        nam_xem_han=user_info['nam_xem_han'],
                        am_lich=user_info['am_lich']).save()

    @classmethod
    def generate_thien_ban(cls, user_info):
        lunar_calendar = user_info.get('am_lich')
        nam_am, thang_am, ngay_am = lunar_calendar.year, lunar_calendar.month, lunar_calendar.day
        nam_thien_can = THIEN_CAN[nam_am % 10]
        nam_dia_chi = DIA_CHI[nam_am % 12]
        return {
            'ho_ten': user_info.get('ho_ten'),
            'nam_sinh': user_info.get('nam_sinh'),
            'nam_am': nam_thien_can + ' ' + nam_dia_chi,
            'thang_sinh': user_info.get('thang_sinh'),
            'thang_am': thang_am,
            'ngay_sinh': user_info.get('ngay_sinh'),
            'ngay_am': ngay_am,
            'gio_sinh': user_info.get('gio_sinh'),
            'gender': "Nam" if user_info['gender'] else "Nữ",
            'nam_thien_can': nam_thien_can,
            'nam_dia_chi': nam_dia_chi
        }
