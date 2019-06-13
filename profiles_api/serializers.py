from rest_framework import serializers
# import profiles_api models.py
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """ 
    - serializers เป็น class Serializer (ไม่มี s) , a name field for testing our APIView
    - เอาไปเรียกใช้ใน views.py ต่อในการ post, put, patch
    """

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """ Create User โดยใช้ Serializer รับ DATA จาก API โดยมี ModelSerializer เชื่อมต่อกับ models.py """
    """ Serializer a user profile object ตัว ModeilSerializer  """

    class Meta:
        """ จะ map models ดึงข้อมูลจาก db """
        model = models.UserProfile
        # ใช้ tuple  ว่าจะเอา field ไหนมาแสดงบ้าง
        fields = ('id', 'email', 'name', 'password')
        """ extra keyword เพื่อป้องกันไม่ให้แสดง password และแสดงผลเป็น dot หรือ * """
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    # ModelSerializer allow to create simple object กำหนด function create เพื่อรับค่าของ user ที่ส่งมาทางหน้าเว็บ และเรียก create_user ใน models มาเพื่อส่งข้อมูลไปสร้าง user เก็บลง db
    def create(self, validated_data):
        """ 
            - overwrite create_user เพราะว่า password ที่รับมาเป็น clear text แล้ว save โดย create_user ใน models.py
            - create and return a new user
        """

        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        """ มี comma ด้วย เพราะคนละ agru """

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ Serializer profile feed items """

    class Meta:
        """ บอก serializer ว่าใช้ models อะไร """
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        """ id django จะสร้างให้อัตโนมัติ และต้องให้ user_profile เป็น read_only """
        extra_kwargs = {
            'user_profile': {'read_only': True}
        }


""" 
- Serializers ช่วยแปลง data input เป็น python object เหมือนเปน form validate (post, put, patch)
    - ช่วยดู validate ตาม data type ที่กำหนดไว้
    - คล้ายๆ django form คอย valide api ที่ส่งเข้ามา
    - เป็น validation rules ของแต่ละ field
    - สามารถแปลงจาก dict > json,  json = JSONRenderer().render(serializer.data)
    - แปลงจาก json > dict (Deserializing) data = JSONParser().parse(stream)
 """
