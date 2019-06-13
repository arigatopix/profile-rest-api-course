# APIView เป็น function เกี่ยวกับ Http Method
from rest_framework.views import APIView
# ViewSets เป็นการ combine logic คล้ายๆ controller (มาจาก docs)
from rest_framework import viewsets
# response ตอบกลับเป็น JSON
from rest_framework.response import Response
# check status HTTP
from rest_framework import status
# TokenAuthentication เป็น Type ของ auth ที่ใช้กับ api จะ gen ให้อัตโนมัติ
from rest_framework.authentication import TokenAuthentication
# Search profile by name, email
from rest_framework import filters
# create auth token เอาไว้แสดงผลใน LoginView
from rest_framework.authtoken.views import ObtainAuthToken
# API setting เพราะ..
from rest_framework.settings import api_settings
# import serializers
from profiles_api import serializers
# import models สำหรับ เพื่อใช้กับ modelViewSet คล้ายๆ viewsets เพื่อ mananging models ผ่าน api
from profiles_api import models
# use permissions
from profiles_api import permissions


class HelloApiView(APIView):
    """ Test API View create endpoint """

    # บอก APIView ว่า data ไหนที่จะใช้ post, put, patch, delete
    serializer_class = serializers.HelloSerializer

    # GET METHOD อย่าลืมมี self เพราะเป็น class base

    def get(self, request, format=None):
        """ Returns a list of APIView features จะรับข้อมูล API เมื่อ client enter เข้า URL """
        """ format คือ format ของ endpoint """

        an_apiview = [
            # list ในนี้คือ response เมื่อ client get
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLS'  # คือต้อง defined urls ขึ้นมาเป็น endpoint
        ]

        # output เมื่อ api ถูก get จะเป็น format dictionary
        # สุดท้าย Response APIView แปลงเป็น JSON
        return Response({'message': 'Hello', 'an_apiview': an_apiview, })

    # POST METHOD
    def post(self, request):
        """ Create a hello message with our name รับ request จาก client"""

        # save or update into database
        serializer = self.serializer_class(data=request.data)
        """ inherit มาจาก serializers.py และนำเอา request.data ไป validate โดย (data=request.data) เป็นการ save new instance """

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
                serializer.errors,  # serializer.errors,เป็น dictionary
                status=status.HTTP_400_BAD_REQUEST  # บอก status ในหน้า apiview
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

        """ หลังจากนั้นไปตั้งค่า urls > profiles_api (urls) > render APIView """


class HelloViewSet(viewsets.ViewSet):
    """ TEST API ViewSet พวก function list, create, ... มาจาก viewset action"""

    # serializer มีเพื่อแปลงข้อมูล และเพื่อเช็ค validate และบอกให้ django แสดงหน้าเว็บสำหรับ post, put, patch, delete
    serializer_class = serializers.HelloSerializer
    """ จะไปแสดงผลในหน้า api/hello-viewset (HTML form) และ post Name field ในหน้าเว็บได้ """

    # ! ประกาศ function ระวังเรื่อง indent *****************
    # list คล้ายๆ get ที่ viewsets ส่งกลับมา
    def list(self, request):
        """ Return a hello message and a_viewset """
        a_viewset = [
            'Users actions (list, create, retrieve, update, partial_update)',
            'Automatically map to URLS using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello! ViewSets', 'a_viewset': a_viewset})

    def create(self, request):
        """ Create a new hello message """

        # POST เข้ามา แล้วเก็บไว้ใน serializer และ serializers ใน HelloSerializer
        serializer = self.serializer_class(data=request.data)

        # check valid data
        if serializer.is_valid():
            """
            - serializer คือข้อมูลที่รับมา
            - validate_data return Returns the validated incoming data (มาเป็น dict) โดย get('name') คือเอามาจาก serializers.HelloSerializer
            """
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    # retrieve, update, patial_update, destroy ต่างจาก APIView นิดหน่อยที่จะต้อง จะต้องเข้า url ที่ระบุ id หรือ pk เพื่อ action ถ้าเข้า api/hello-viewset/1 แล้วไม่ขึ้นแสดงว่า indent ที่ประกาศ function ไม่ถูกต้อง
    def retrieve(self, request, pk=None):
        """ Handle getting an object by its ID """
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """ Handle updating an object """
        return Response({'message': 'PUT'})

    def partial_update(self, request, pk=None):
        """ Handle updating part of an object """
        """ * พิมพ์ชื่อ function จาก partial_update เป็น patial_update ผิดไปปุ่ม PATCH ไม่ขึ้น """
        return Response({'message': 'PATCH'})

    def destroy(self, request, pk=None):
        """ Handle removing an object """
        return Response({'message': 'DELETE'})


# UserProfileViewSet
class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and update profiles """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    """ django รู้ว่าเราจะ list, post, update, destroy models ก็เลย provide ให้เรียบร้อยแล้วผ่าน serializer_class กับ queryset """

    authentication_classes = (TokenAuthentication, )
    """ เป็น tuple โดยบรรจุ type ของ auth ที่เราใช้ อาจจะมากกว่า 1 ก็ได้  auth_classes เป็นการ how to authenticate """

    permission_classes = (permissions.UpdateOwnProfile, )
    """ permission คือการกำหนดให้ user ทำในสิ่งที่ทำได้ """

    filter_backends = (filters.SearchFilter, )
    """ search in backend """
    search_fields = ('name', 'email', )
    """ บอก backend ว่าจะ search field อะไรได้บ้าง จะเพิ่ม filter หน้าเว็บ และ querystring ใน url"""

# Login APIView base on class ObtainAuthToken


class UserLoginApiView(ObtainAuthToken):
    """ Handle creating user authentication tokens """
    """ จะทำให้ระบุตัวตนได้ด้วยเลข Token เมื่อ login จะมี header Authentication : Token (token no.) มาคู่กับ permission จะต้องใช้ renderer_classes ในการตั้งค่า """
    """ObtainAuthToken จะเป็นการ custom AuthToken โดย Obtain สามารถเข้าไปใช้งาน urls.py ได้ (เช็ค auth ด้วย url) https://www.django-rest-framework.org/api-guide/authentication/#by-exposing-an-api-endpoint"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    """ add manaul เพราะใช้ ObtainAuthToken """
    """ AuthToken เป็นค่าคงที่ของแต่ละคน  """


# APIviews สร้าง endpoint (get, post, put, patch) นำไปแสดงผลเหมือนกับ views.py ปกติ แต่นี่เป็น api โดยใช้ rest framework
# Class-base view จะช่วย render เป็นหน้าจอ api_view converse จาก class to json
""" 
++ DJango Restframeworks Views
Helper class create API endpoint
- APIViews :
	- logic to make API endpoint
	- Use standard HTTP Methods for functions (get, put, patch, delete)
	- Control over the logic คือใช้เรียก api ไรงี้มากกว่าเป็น logic
	- ใช้เรียก และแสดงผลมากกว่า เป็น logic
	- Calling other APIs/services
	- accesing local files or data
- ViewSet : logic in endpoint
	- map http method
	- เขียน code ให้ใกล้เคียงกับ database operations และใกล้เคียงกับ database interface backend
	- CRUD interface to database
	- Create simple API
- ModelViewSet : คล้ายๆ กับ viewset ที่สามารถ manage model
 """
