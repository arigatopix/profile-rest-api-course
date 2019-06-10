# APIviews สร้าง endpoint (get, post, put, patch) นำไปแสดงผลเหมือนกับ views.py ปกติ แต่นี่เป็น api โดยใช้ rest framework
# Class-base view จะช่วย render เป็นหน้าจอ api_view converse จาก class to json

from rest_framework.views import APIView
from rest_framework.response import Response
''' response ตอบกลับเป็น JSON '''

class HelloApiView(APIView):
	""" Test API View create endpoint """
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

		# urls > profiles_api (urls) > render APIView
