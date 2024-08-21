import requests
from sqlalchemy import insert
from sqlalchemy.exc import SQLAlchemyError

from app.model.member import Member


class MemberService:
    @staticmethod
    def insert_member(db, member):
        try:
            stmt = insert(Member).values(
                userid=member.userid, passwd=member.passwd,
                name=member.name, email=member.email)
            result = db.execute(stmt)
            db.flush()
            db.commit()
            return result

        except SQLAlchemyError as ex:
            print(f'▶▶▶ insert_member 오류발생: {str(ex)}')
            db.rollback()


    # google recaptcha 확인 url
    # https://www.google.com/recaptcha/api/siteverify?secret=비밀키&response=응답토큰
    @staticmethod
    def check_captcha(member):
        req_url = 'https://www.google.com/recaptcha/api/siteverify'
        params = { 'secret': '',
                   'response': member.captcha }

        res = requests.get(req_url, params=params)
        result = res.json()
        print('check => ', result)

        return result['success']
        # return True