#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Creaet Time    : 2021/10/18 22:19
# @File           : role.py
# @IDE            : PyCharm
# @desc           : pydantic 模型，用于数据库序列化操作

# pydantic 验证数据：https://blog.csdn.net/qq_44291044/article/details/104693526


from typing import Optional, List
from pydantic import BaseModel, Field, validator
from core.validator import ValiDatetime


class Menu(BaseModel):
    title: str
    icon: Optional[str] = None
    component: str
    path: str
    disabled: bool = False
    hidden: bool = False
    order: Optional[int] = None
    perms: Optional[str] = None
    parent_id: Optional[int] = None
    menu_type: str


class MenuSimpleOut(Menu):
    id: int
    create_datetime: ValiDatetime
    update_datetime: ValiDatetime

    class Config:
        orm_mode = True


class Meta(BaseModel):
    title: str
    icon: Optional[str] = None
    hidden: bool = False
    noCache: Optional[bool] = True
    breadcrumb: Optional[bool] = True
    affix: Optional[bool] = False
    noTagsView: Optional[bool] = False
    canTo: Optional[bool] = False


# 路由展示
class RouterOut(BaseModel):
    name: Optional[str] = None
    component: str
    path: str
    redirect: Optional[str] = None
    meta: Optional[Meta] = None
    children: List['RouterOut'] = []

    class Config:
        orm_mode = True


RouterOut.update_forward_refs()


# 采单树列表，选用权限展示使用
class TreeselectOut(BaseModel):
    id: int
    label: str = Field(alias='title')
    order: Optional[int] = 1
    parent_id: Optional[int] = None

    class Config:
        orm_mode = True


class TreeListOut(MenuSimpleOut):
    children: List['TreeListOut'] = []

    class Config:
        orm_mode = True


RouterOut.update_forward_refs()