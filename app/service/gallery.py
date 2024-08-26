
import os
from datetime import datetime

from app.schema.gallery import NewGallery

def get_gallery_data( title: str = Form(...), userid: str = Form(...),
                      contents: str = Form(...)):
    pass


import os
from datetime import datetime
from typing import List
from fastapi import UploadFile
from typing import List

class ProcessUpload:
    UPLOAD_PATH = 'C:/Java/nginx-1.26.2/html/cdn/img/'

    @staticmethod
    async def process(files: List[UploadFile]):
        attachs = []  # 업로드된 파일 정보를 저장하기 위한 리스트
        today = datetime.today().strftime('%Y%m%d%H%M%S')  # 현재 날짜와 시간을 기반으로 한 문자열 생성

        for file in files:
            if file.filename and file.content_type:
                nfname = f'{today}_{file.filename}'  # 파일 이름에 현재 날짜와 시간을 추가
                fname = os.path.join(ProcessUpload.UPLOAD_PATH, nfname)  # 업로드할 파일 경로 생성

                content = await file.read()  # 업로드할 파일의 내용을 비동기로 읽음
                with open(fname, 'wb') as f:
                    f.write(content)  # 파일을 저장

                attach = [nfname, file.size]  # 업로드된 파일 정보를 리스트에 저장
                attachs.append(attach)

        return attachs

class GalleryService:
    pass

