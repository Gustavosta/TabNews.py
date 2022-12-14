class Config:
    HOST = 'https://www.tabnews.com.br'
    #HOST = 'https://tabnews-4lk1vytlv-tabnews.vercel.app'

    LOGIN_URL = HOST+'/api/v1/sessions'
    CONTENTS_URL = HOST+'/api/v1/contents'
    USER_DATA_URL = HOST+'/api/v1/user'
    USERS_DATA_URL = HOST+'/api/v1/users'


