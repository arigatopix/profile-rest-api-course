from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)

# Manage for user profiles
class UserProfileManager(BaseUserManager):
    """ บอกให้ django สร้าง user ตามที่เรา custom ขึ้นมา """

    # cli สร้าง user จะต้องมี email, name, password(default=None)
    def create_user(self, email, name, password=None):
        """ เราแทนที่ username_field ด้วย email_field """
        
        if not email:
            """ check not email or empty """
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        """ มีไว้เพื่อตั้งค่าให้ email เป็นตัวเลขทั้งหมด เพราะบางบริษัทใช้ case sensitive เล็กบ้างใหญ่บ้าง แต่อันนี้ให้เป็นตัวเล็กหมด เพื่อป้องกันการใช้ซ้ำซ้อน """

        user = self.model(email=email, name=name)
        """ สร้าง model ของ user ใหม่ """

        user.set_password(password)
        """ password จะถูกแปลงเป็น hash not plain text """

        user.save(using=self._db)
        """ เผื่อใช้ multiple database """

        return user

    def create_superuser(self, email, name, password):
        """ Create and save a new superuser with given details """

        # inherite จาก create user ใช้ function เหมือนกัน
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

# Custom user : Database model for users in the system
class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''
    ตั้งค่า user เองโดยเป็นส่วนหนึ่งของ Database (model)
    - ใช้ email เป็นตัว login ต้อง migrate ก่อน django ถึงจะทำงานได้
    - AbstractBaseUer : เปลี่ยน structure ของ default user เช่นตั้งค่าให้ email เป็น USERNAME_FIELD, is_active, set_password etc.
    - PermissionsMixin : เปลี่ยน permission แบบ custom เช่น staff, superuser
    อย่าลืมไป register admin , django จะตั้งชื่อในหน้า admin แยกชื่อ class ตามตัวพิมพ์ใหญ่
    '''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    # สำหรับสร้าง user ผ่าน CLI (commandline) โดยจะเป็น function สร้าง และ check
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    ''' overwrite ปกติ username ด้วย email '''
    REQUIRED_FIELDS = ['name']

    # method เพื่อส่งข้อมูลแสดงผลใน cli
    def get_full_name(self):
        """ Retrieve full name of user """
        return self.name
        
    def get_short_name(self):
        """ Retrieve short name of user """
        return self.name

    def __str__(self):
        ''' converse UserProfile object to string or show in django admin'''
        """ return string representation of our user """
        return self.email