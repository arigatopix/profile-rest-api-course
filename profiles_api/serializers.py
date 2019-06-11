from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ 
    - serializers เป็น class Serializer (ไม่มี s) , a name field for testing our APIView
    - เอาไปเรียกใช้ใน views.py ต่อในการ post, put, patch
    """

    name = serializers.CharField(max_length=10)

""" 
- Serializers ช่วยแปลง data input เป็น python object เหมือนเปน form validate (post, put, patch)
    - ช่วยดู validate ตาม data type ที่กำหนดไว้
    - คล้ายๆ django form คอย valide api ที่ส่งเข้ามา
    - เป็น validation rules ของแต่ละ field
 """