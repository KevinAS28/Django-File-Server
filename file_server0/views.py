import json, os
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.conf import settings


files_dirs = json.load(open(os.path.join(settings.BASE_DIR, 'files_dirs.json')))

# Create your views here.
def download(request, filename):
    print('requested file: ' + filename)
    for file_path in files_dirs['files']:
        file = os.path.basename(file_path)
        # if os.path.isfile(file):
        if True:
            if file==filename:
                with open(file_path, 'rb') as file_fd:
                    response = HttpResponse(file_fd.read(), content_type='application/octet-stream')
                    response['Content-Disposition'] = 'inline; filename='+file
                    return response
            # else:
            #     print(f'file {file_path} not match')
        else:
            print(f'file {file_path} not exist!')

    for dir_path in files_dirs['dirs']:
        # if os.path.isdir(dir_path):
        if True:
            for root, dirs, files in os.walk(dir_path, topdown=False):
                for file in files:
                    file_path = os.path.join(root, file)
                    # if os.path.isfile(file):
                    if True:
                        if file==filename:
                            with open(file_path, 'rb') as file_fd:
                                response = HttpResponse(file_fd.read(), content_type='application/octet-stream')
                                response['Content-Disposition'] = 'inline; filename='+file
                                return response     
                        # else:
                        #     print(f'file {file_path} not match!')
                    else:
                        print(f'file {file_path} not exist!')          
        # else:
        #     print(f'dir {dir_path} not exist!')     

            
    return HttpResponseNotFound(f'file {filename} not exist!')
