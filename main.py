import hashlib
s='minidelta'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
