from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, Http404
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from .api_ocr import ocr_api
import json
import os

from django.db.models import Q, Count


def index(request):
    """
    처방전 업로드 사이트 홈

    이 사이트에서 버튼을 누르면 upload하는 사이트로 이동
    """

    return render(request, 'prescription/pre_home.html')


# Create your views here.

def presc_upload(request):
    content = {"exist": False}
    
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        res_dict = ocr_api('./prescDir/' + filename)

        # res_dict = json.load(res_dict_str)
        # print(uploaded_file_url)
        res_dict['uploaded_file_url'] = uploaded_file_url

        print(res_dict['images'][0])
        with open('./prescDir/' + 'presc.json', 'w') as fp:
            json.dump(res_dict, fp, indent=4)

        idx = 0
        for i in range(len(res_dict['images'][0]['fields'])):
            if res_dict['images'][0]['fields'][i]['inferText'] == "":
                idx = i
                break
        res_dict['images'][0]['fields'] = res_dict['images'][0]['fields'][:idx]

        content = res_dict['images'][0]
        content['exist'] = True

        return render(request, 'prescription/presc_upload.html', content)

    return render(request, 'prescription/presc_upload.html', content)