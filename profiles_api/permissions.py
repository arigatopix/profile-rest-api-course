from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ 
    - BasePermission คือ django ให้ custom permission 
    - Allow user to edit their own profile class จะ return True, False
    """

    def has_object_permission(self, request, view, obj):
        """ Check user is trying to edit their own profile เมื่อมี request django จะเรียก function โดยเอา request มาเช็คกับ object แล้วบอกว่าใช่ตัวตนนั้นมั้ยโดยเช็คกับ id """

        if request.method in permissions.SAFE_METHODS:
            """ method ที่เป็น get, post (อยู่ใน SAFE_METHODS) สามารถดูข้อมูลได้ เลยส่งกลับเป็น True """
            return True
        
        return obj.id == request.user.id
        """ มี permission สำหรับ method put, patch, delete เมื่อ user มี id ตรงกับ obj id (เช็คกับ db) จะ return True, False """

""" 
permission : จัดการสิทธิ์สำหรับการแก้ไข 
    - จำกัด ถ้าไม่ใช่คำสั่ง update, put, patch ให้ดูได้ (ก็คือ list, create) 
    - ถ้านอกเหนือจากนั้นให้เช็ค permission
    """