from ext import get_uuid
from models.Enterprise import Enterprise
from models.Users import User


def dict2user(d):
    return User(d['username'], d['password'], d['name'], d['department'], d['memo'])


def dict2enterprise(d):
    return Enterprise(d['nsrsbh'], d['entername'], d['legalname'], d['regdate'], d['taxwebaddress'], d['regcapital'],
                      d['legalpwd'], d['enterattr'], d['province'], d['city'], d['district'], d['regaddr'],
                      d['materialsaddr'], d['filinguser'], d['filingpwd'], d['filinground'])
