# APIviews สร้าง endpoint (get, post, put, patch) นำไปแสดงผลเหมือนกับ views.py ปกติ แต่นี่เป็น api โดยใช้ rest framework
# Class-base view จะช่วย render เป็นหน้าจอ api_view converse จาก class to json

# APIView เป็น function เกี่ยวกับ Http Method
from rest_framework.views import APIView
# response ตอบกลับเป็น JSON
from rest_framework.response import Response
# check status HTTP
from rest_framework import status
# import serializers
from profiles_api import serializers

class HelloApiView(APIView):
	""" Test API View create endpoint """

	# บอก APIView ว่า data ไหนที่จะใช้ post, put, patch
	serializer_class = serializers.HelloSerializer


	# GET METHOD อย่าลืมมี self เพราะเป็น class base
	def get(self, request, format=None):
		""" Returns a list of APIView features จะรับข้อมูล API เมื่อ client enter เข้า URL """
		""" format คือ format ของ endpoint """

		an_apiview = [
			'Uses HTTP methods as function (get, post, patch, put, delete)', # list ในนี้คือ response เมื่อ client get
			'Is similar to a traditional Django View',
			'Gives you the most control over you application logic',
			'Is mapped manually to URLS' # คือต้อง defined urls ขึ้นมาเป็น endpoint
		]

		# output เมื่อ api ถูก get จะเป็น format dictionary 
		# สุดท้าย Response APIView แปลงเป็น JSON 
		return Response({'message': 'Hello', 'an_apiview': an_apiview,})

	# POST METHOD
	def post(self, request):
		""" Create a hello message with our name รับ request จาก client"""
		serializer = self.serializer_class(data=request.data)
		""" inherit มาจาก serializers.py และนำเอา request.data ไป validate และ return boolean (มั้ง) """

		# check valid serializer input ดูว่าเกิน 10 ตัวอักษรมั้ย และ return Response
		if serializer.is_valid():
			""" is_valid เป็น method check valid จริง """
			name = serializer.validated_data.get('name')
			""" เอา 'name' มาจาก serializers.py ที่พึ่งเช็คไปมาใส่ใน name"""
			message = f'Hello {name}'
			""" template string แสดงผลใน api """

			return Response({'message': message})
			""" อย่าลืมว่าต้องส่งกลับด้วย response และ dictionary """
		
		else:
			""" is not valid return error message and return 400 bad request """
			return Response(
				serializer.errors, # serializer.errors,เป็น dictionary 
				status=status.HTTP_400_BAD_REQUEST # บอก status ในหน้า apiview
			) 

	# PUT METHOD : UPDATE ENTIER OBJECT 
	def put(self, request, pk=None):
		"""Handle updateing an object และตอนนี้ยังไม่มี primary key"""
		return Response({'method': 'PUT'})
		
		
	# PATCH METHOD : Partial update object
	def patch(self, request, pk=None):
		""" Handle a partial update of an object จะขึ้นใน patch แบบ json """
		return Response({'method': 'PATCH'})

	# DELETE METHOD
	def delete(self, request, pk=None):
		return Response({'method': 'DELETE'})

""" 
Helper class create API endpoint
- APIViews :
	- logic to make API endpoint
	- Use standard HTTP Methods for functions (get, put, patch, delete)
	- Control over the logic คือใช้เรียก api ไรงี้มากกว่าเป็น logic
	- ใช้เรียก และแสดงผลมากกว่า เป็น logic
	- Calling other APIs/services
	- accesing local files or data
- ViewSet :
 """

 # urls > profiles_api (urls) > render APIView