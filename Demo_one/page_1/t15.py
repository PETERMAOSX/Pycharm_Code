#摘要算法
import hashlib
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def register(user,passwd):
    global db
    md = hashlib.md5()
    md.update(passwd.encode('utf-8'))
    pd = md.hexdigest()
    db[user] = pd
def login(user,passwd:str):
    if user not in db.keys():
        return 'Not register'
    md = hashlib.md5()
    md.update(passwd.encode('utf-8'))
    pd = md.hexdigest()
    if pd == db[user]:
        return 'Hello '+str(user)+' Welcome to Login.'
    else:
        return 'Erro!!'

register('Peter','mmmmmm')
register('Raymond','MaoShao')
s = login('Peter','mmmmmm')
d = login('Raymond','MaoShao')
md5 = hashlib.md5()
md5.update('MaoShao!Xiong'.encode("utf-8"))
print(md5.hexdigest())
print(s)
print(d)