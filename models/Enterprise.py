# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

from ext import db, get_uuid


class Enterprise(db.Model):
    __tablename__ = 'enterprise'

    id = db.Column(db.String(32), primary_key=True, default=get_uuid, unique=True, info='ID\\n')
    nsrsbh = db.Column(db.String(32), nullable=False, info='纳税人识别号')
    entername = db.Column(db.String(32), nullable=False, info='企业名称')
    legalname = db.Column(db.String(16), nullable=False, info='法人名称')
    regdate = db.Column(db.Date, info='注册日期')
    taxwebaddress = db.Column(db.String(256), info='税务申报网站地址')
    regcapital = db.Column(db.Numeric(10, 0), info='注册资本')
    legalpwd = db.Column(db.String(32), info='法人密码')
    enterattr = db.Column(db.Integer, info='企业属性')
    province = db.Column(db.Integer, nullable=False, info='所属省份')
    city = db.Column(db.Integer, nullable=False, info='所属城市')
    district = db.Column(db.Integer, nullable=False, info='所属区')
    regaddr = db.Column(db.String(128), info='注册地址')
    materialsaddr = db.Column(db.String(128), info='资料存放地址\\n')
    filinguser = db.Column(db.String(16), info='税务申报人姓名')
    filingpwd = db.Column(db.String(32), info='税务申报密码')
    filinground = db.Column(db.Integer, info='税务申报周期')

    def __init__(self, nsrsbh, entername, legalname, regdate, taxwebaddress, regcapital, legalpwd, enterattr, province,
                 city, district, regaddr, materialsaddr, filinguser, filingpwd, filinground):
        self.nsrsbh = nsrsbh
        self.entername = entername
        self.legalname = legalname
        self.regdate = regdate
        self.taxwebaddress = taxwebaddress
        self.regcapital = regcapital
        self.legalpwd = legalpwd
        self.enterattr = enterattr
        self.province = province
        self.city = city
        self.district = district
        self.regaddr = regaddr
        self.materialsaddr = materialsaddr
        self.filinguser = filinguser
        self.filingpwd = filingpwd
        self.filinground = filinground

    def __repr__(self):
        return self.entername

    def __str__(self):
        return self.nsrsbh
