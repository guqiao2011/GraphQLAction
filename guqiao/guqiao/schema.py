# _*_ coding:utf-8 _*_
__author__ = 'guqiao'
__date__ = '2018/11/5 10:32'

from django.contrib.auth.models import User as UserModel

from graphene_django import DjangoObjectType
import graphene


class User(DjangoObjectType):
    class Meta:
        model = UserModel


class Query(graphene.ObjectType):
    users = graphene.List(User, id=graphene.Int())

    @graphene.resolve_only_args
    def resolve_users(self):
        return UserModel.objects.all()


schema = graphene.Schema(query=Query)
