
class twofa(object):
    TNAPI = ''
    NUM = ''
    NAME = ''
    DBA = ''
    EMAIL = ''
    REPORTURL = ''
    SENDER = ''
    USRNUM = ''
    
    def set(cfg, value):
        if cfg == 'key':
            twofa.TNAPI = value
        elif cfg == 'telnum':
            twofa.NUM = value
        elif cfg == 'usrname':
            twofa.NAME = value
        elif cfg == 'businessName':
            twofa.DBA = value
        elif cfg == 'usremail':
            twofa.EMAIL = value
        elif cfg == 'abuseurl':
            twofa.REPORTURL = value
        elif cfg == 'senderemail':  
            twofa.SENDER = value
        elif cfg == 'usrnum':  
            twofa.USRNUM = value

    def get(cfg):
        if cfg == 'key':
            return twofa.TNAPI
        elif cfg == 'telnum':
            return twofa.NUM
        elif cfg == 'usrname':
            return twofa.NAME
        elif cfg == 'businessName':
            return twofa.DBA
        elif cfg == 'usremail':
            return twofa.EMAIL
        elif cfg == 'abuseurl':
            return twofa.REPORTURL
        elif cfg == 'senderemail':  
            return twofa.SENDER
        elif cfg == 'usrnum':  
            return twofa.USRNUM