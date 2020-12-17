from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count

import json

from ..models import Hospital, Device


def map(request):
    """
    지도 검색창 출력
    """
    # 입력 파라미터
    kw = request.GET.get('kw', '')  # 검색어
    hospital = Hospital.objects.all()
    device = Device.objects.all()

    # 검색
    if kw:
        hospital = hospital.filter(
            Q(hospital_name__icontains=kw)
        ).distinct()

        # device = device.filter(
        #     Q(hospital_name__icontains=kw)
        # ).distinct()
        # temp_device = device[0]  # 확인: 각 병원의 디바이스 하나만 불러짐 (수정 요)

        temp_name = hospital[0]  # 검색 후 첫번째 병원 - todo
        hospital_id = temp_name.encoded_id
        device = device.filter(encoded_id=hospital_id)  # list of devices for each hospital

        # device_dict = dict()
        # for d in device:  # d.device_code, d.device_name, d.device_num
        #     device_dict[d.device_code] = [d.device_name, d.device_num]

        device_code_list = []
        device_name_list = []
        device_num_list = []
        for d in device:
            device_code_list.append(d.device_code)
            device_name_list.append(d.device_name)
            device_num_list.append(d.device_num)

        context = {
            'encoded_id': temp_name.encoded_id,
            'zipcode': temp_name.zipcode,
            'address': temp_name.address,
            'phone': temp_name.phone,
            'url': temp_name.url,
            'hospital_name': temp_name.hospital_name,
            'latitude': temp_name.latitude,
            'longitude': temp_name.longitude,
            'total_doctor_num': temp_name.total_doctor_num,
            'doctor_num': temp_name.doctor_num,
            'intern_num': temp_name.intern_num,
            'resi_num': temp_name.resi_num,
            'board_num': temp_name.board_num,
            'device_code': device_code_list,
            'device_name': device_name_list,
            'device_num': device_num_list,
            'kw': kw}

        # context = {
        #     'encoded_id': temp_name.encoded_id,
        #     'zipcode': temp_name.zipcode,
        #     'address': temp_name.address,
        #     'phone': temp_name.phone,
        #     'url': temp_name.url,
        #     'hospital_name': temp_name.hospital_name,
        #     'latitude': temp_name.latitude,
        #     'longitude': temp_name.longitude,
        #     'total_doctor_num': temp_name.total_doctor_num,
        #     'doctor_num': temp_name.doctor_num,
        #     'intern_num': temp_name.intern_num,
        #     'resi_num': temp_name.resi_num,
        #     'board_num': temp_name.board_num,
        #     'device_name': temp_device.device_name,
        #     'device_num': temp_device.device_num,
        #     'kw': kw}


    else:
        temp_name = hospital.filter(
            Q(hospital_name__icontains='카이스트')
        ).distinct()
        context = {
            'hospital_name': '카이스트병원',
            'latitude': 36.371613355884065,
            'longitude': 127.36190815365813,
            'kw': kw}

    context_json = json.dumps(context)

    return render(request, 'map/map_search.html', {'context_json': context_json})
