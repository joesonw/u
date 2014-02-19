from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core import validators
from django.contrib import auth
from django.contrib.auth.signals import user_logged_in
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission,Group
from django.contrib.contenttypes.models import ContentType
#------------CUSTOM GROUP/PERMISSION MODEL----------------



#------------CUSTOM MODELS NEEDED IN USER MODEL-----

#------------CUSTOM USER MODEL----------------------
class MemberManager(BaseUserManager):

    def create_user(self,username,realname,password):
        if (not realname) or (not username) or (not password):
            raise ValueError("Illegal Arguments")
        user = self.model(username=MemberManager.normalize_email(username),realname=realname,password=password)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username,realname,password):
        user = self.create_user(username=MemberManager.normalize_email(username),realname=realname,password=password)
        user.is_active=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user
    
    
class Member(AbstractBaseUser):
    
    #-------Required Fields-------------
    username        = models.EmailField(_('username'),max_length=255,unique=True,db_index=True)
    date_joined     = models.DateTimeField(_('date joined'),default=timezone.now)
    is_active       = models.BooleanField(_('active'),default=True)
    is_staff        = models.BooleanField(_('staff status'),default=False)
    is_superuser    = models.BooleanField(_('superuser status'),default=False)
    realname        = models.CharField(_('real name'),max_length=40)
    #--------Custom Fields---------------
    Renren 		= models.CharField(_('renren id'),max_length=30)
    WB 			= models.CharField(_('weibo id'),max_length=30)
    QQT 		= models.CharField(_('tencent weibo id'),max_length=30)
    Renren_RToken 	= models.CharField(_('renren refresh token'),max_length=100)
    WB_RToken 		= models.CharField(_('weibo refresh token'),max_length=100)
    QQT_RToken 		= models.CharField(_('tencent weibo refresh token'),max_length=100)
    Renren_expire       = models.CharField(_('renren token expiring time'),max_length=30)
    WB_expire           = models.CharField(_('renren token expiring time'),max_length=30)
    QQT_expire          = models.CharField(_('renren token expiring time'),max_length=30)


    #-----SYS Variables
    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['realname']
    objects = MemberManager()
    

    #------Implementing Methods---
    def get_full_name(self):
        pass
    def get_short_name(self):
        pass
    def get_group_permissions(self,obj=None):
        permissions = set()
        for backend in auth.get_backends():
            if hasattr(backend,"get_group_permissions"):
                if obj is not None:
                    permissions.update(backend.get_group_permissions(self,obj))
                else:
                    permissions.update(backend.get_group_permissions(self))
        return permissions
    def get_all_permissions(self,obj=None):
        permissions = set()
        for backend in auth.get_backends():
            if hasattr(backend,"get_all_permissions"):
                if obj is not None:
                    permissions.update(backend.get_all_permissions(self,obj))
                else:
                    permissions.update(backend.get_all_permissions(self))
        return permissions
            
    def has_perm(self,perm,obj=None):
        if self.is_active and self.is_superuser:
            return True
        for backend in auth.get_backends():
            if hasattr(backend,"get__perm"):
                if obj is not None:
                    if backend.has_perm(self,perm,obj):
                        return True
                else:
                    if backend.has_perm(self,perm):
                        return True
        return False
    def has_perms(self,perm_list,obj=None):
        if self.is_active and self.is_superuser:
            return True
        for perm in perm_list:
            if not self.has_perm(perm,obj):
                return False
        return True
    def has_module_perms(self,package_name):
        if self.is_active and self.is_superuser:
            return True
        for backend in auth.get_backends():
            if hasattr(backend,"has_module_perms"):
                if backend.has_module_perms(self,package_name):
                    return True
        return False
    def email_user(self,subject,message,form_email=None):
        pass
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        permissions = (
            #("code name","human readable string"),
            )
    

