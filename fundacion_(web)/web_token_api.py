import endpoints
from google.appengine.ext import ndb
from google.appengine.api import app_identity
from protorpc import remote

import jwt
import time

from CustomExceptions import NotFoundException

from messages import EmailPasswordMessage, TokenMessage, CodeMessage, Token, TokenKey,MessageNone
from messages import FilialInput, FilialUpdate, FilialList
from messages import TweetInput, TweetUpdate, TweetList
from messages import UserInput, UserUpdate, UserList
from messages import ProductInput, ProductUpdate, ProductList
from messages import MedicinaInput, MedicinaUpdate, MedicinaList
from messages import ViveresInput, ViveresUpdate, ViveresList

from endpoints_proto_datastore.ndb import EndpointsModel

import models
from models import validarEmail
from models import Filial, Usuarios, Tweet, Product, Medicina, Viveres


###############
# Product
###############
@endpoints.api(name='products_api', version='v1', description='products endpoints')
class ProductsApi(remote.Service):
###############get the info of one########
# insert
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(ProductInput, CodeMessage, path='product/insert', http_method='POST', name='product.insert')
#siempre lleva cls y request
 def product_add(cls, request):
  try:
   token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
   user = Usuarios.get_by_id(token['user_id']) #obtiene el usuario para poder acceder a los metodos declarados en models.py en la seccion de
   myproduct = Product()
   if myproduct.product_m(request, user.key)==0:#llama a la funcion declarada en models.py en la seccion de USUARIOS
    codigo=1
   else:
    codigo=-3
          #la funcion josue_m puede actualizar e insertar
          #depende de la ENTRADA de este endpoint method
   message = CodeMessage(code=codigo, message='Product added')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message

  ########################## product list ###################
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(Token, ProductList, path='products/list', http_method='POST', name='product.list')
 def product_list(cls, request):
  try:
   token = jwt.decode(request.tokenint, 'secret')  #checa token
   user = Usuarios.get_by_id(token['user_id']) #obtiene usuario dado el token
   lista = []  #crea lista
   lstMessage = ProductList(code=1) # crea objeto mensaje
   lstBd = Product.query().fetch() # recupera de base de datos
   for i in lstBd: # recorre
    lista.append(ProductUpdate(token='',
     entityKey=i.entityKey,
     #filial_key=user.filial_key.urlsafe(),
     code=i.code,
     description=i.description,
     urlImage=i.urlImage)) # agrega a la lista
    
   lstMessage.data = lista # la manda al messa
   message = lstMessage #regresa
    
  except jwt.DecodeError:
   message = ProductList(code=-1, data=[]) #token invalido
  except jwt.ExpiredSignatureError:
   message = ProuctList(code=-2, data=[]) #token expiro
  return message

###############get the info of one########
 @endpoints.method(TokenKey, ProductList, path='products/get', http_method='POST', name='product.get')
 def product_get(cls, request):
  try:                 
   token = jwt.decode(request.tokenint, 'secret')  #checa token
   productentity = ndb.Key(urlsafe=request.entityKey)
   product = Product.get_by_id(productentity.id()) #obtiene usuario
            #user = Usuarios.get_by_id(token['user_id']) #obtiene usuario dado el token
   lista = []  #crea lista
   lstMessage = ProductList(code=1) # crea objeto mensaje
   lista.append(ProductUpdate(token='', 
    entityKey= product.entityKey,
    #filial_key = user.filial_key.urlsafe(),
    code = product.code,
    description=product.description,
    urlImage=product.urlImage))
   lstMessage.data = lista#ASIGNA a la salida la lista
   message = lstMessage
  except jwt.DecodeError:
   message = ProductList(code=-1, data=[]) #token invalido
  except jwt.ExpiredSignatureError:
   message = ProductList(code=-2, data=[]) #token expiro
  return message

# delete
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(TokenKey, CodeMessage, path='products/delete', http_method='POST', name='products.delete')
 #siempre lleva cls y request
 def product_remove(cls, request):
  try:
   token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
   productentity = ndb.Key(urlsafe=request.entityKey)#Obtiene el elemento dado el EntitKey
   productentity.delete()#BORRA
   message = CodeMessage(code=1, message='Succesfully deleted')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message

##update##
# update
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(ProductUpdate, CodeMessage, path='products/update', http_method='POST', name='products.update')
#siempre lleva cls y request
 def product_update(cls, request):
  try:
   token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
   user = Usuarios.get_by_id(token['user_id'])#obtiene el usuario para poder acceder a los metodos declarados en models.py en la seccion de USUARIOS
   #filialkey = ndb.Key(urlsafe=user.filial_key.urlsafe())#convierte el string dado a entityKey
   product = Product()
   if product.product_m(request, user.key)==0:#llama a la funcion declarada en models.py en la seccion de USUARIOS
    codigo=1
   else:
    codigo=-3
      #la funcion josue_m puede actualizar e insertar
      #depende de la ENTRADA de este endpoint method
   message = CodeMessage(code=1, message='Sus cambios han sido guardados exitosamente')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message















###############
# Medicina
###############
@endpoints.api(name='medicinas_api', version='v1', description='medicinas endpoints')
class MedicinasApi(remote.Service):
###############get the info of one########
# insert
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(MedicinaInput, CodeMessage, path='medicina/insert', http_method='POST', name='medicina.insert')
#siempre lleva cls y request
 def medicina_add(cls, request):
  try:
   token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
   user = Usuarios.get_by_id(token['user_id']) #obtiene el usuario para poder acceder a los metodos declarados en models.py en la seccion de
   mymedicina = Medicina()
   if mymedicina.medicina_m(request, user.filial_key)==0:#llama a la funcion declarada en models.py en la seccion de USUARIOS
    codigo=1
   else:
    codigo=-3
          #la funcion josue_m puede actualizar e insertar
          #depende de la ENTRADA de este endpoint method
   message = CodeMessage(code=codigo, message='Medicine added')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message

  ########################## medicines list ###################
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(Token, MedicinaList, path='medicinas/list', http_method='POST', name='medicina.list')
 def medicina_list(cls, request):
  try:
   token = jwt.decode(request.tokenint, 'secret')  #checa token
   user = Usuarios.get_by_id(token['user_id']) #obtiene usuario dado el token
   lista = []  #crea lista
   lstMessage = MedicinaList(code=1) # crea objeto mensaje
   lstBd = Medicina.query().fetch() # recupera de base de datos
   for i in lstBd: # recorre
    lista.append(MedicinaUpdate(token='',
     entityKey=i.entityKey,
     #filial_key=user.filial_key.urlsafe(),
     title=i.title,
     description=i.description,
     urlImage=i.urlImage)) # agrega a la lista
    
   lstMessage.data = lista # la manda al messa
   message = lstMessage #regresa
    
  except jwt.DecodeError:
   message = MedicinaList(code=-1, data=[]) #token invalido
  except jwt.ExpiredSignatureError:
   message = MedicinaList(code=-2, data=[]) #token expiro
  return message

###############get the info of one########
 @endpoints.method(TokenKey, MedicinaList, path='medicinas/get', http_method='POST', name='medicina.get')
 def medicina_get(cls, request):
  try:                 
   token = jwt.decode(request.tokenint, 'secret')  #checa token
   medicinaentity = ndb.Key(urlsafe=request.entityKey)
   medicina = Medicina.get_by_id(medicinaentity.id()) #obtiene usuario
            #user = Usuarios.get_by_id(token['user_id']) #obtiene usuario dado el token
   lista = []  #crea lista
   lstMessage = MedicinaList(code=1) # crea objeto mensaje
   lista.append(MedicinaUpdate(token='',
    entityKey=medicinaentity.get().entityKey,
    #filial_key=teamentity.get().filial_key.urlsafe(), 
    title=medicinaentity.get().title,  
    #entityKey= medicina.entityKey,
    #filial_key = user.filial_key.urlsafe(),
    #title = medicina.title,
    description=medicina.description,
    urlImage=medicina.urlImage))
   lstMessage.data = lista#ASIGNA a la salida la lista
   message = lstMessage
  except jwt.DecodeError:
   message = MedicinaList(code=-1, data=[]) #token invalido
  except jwt.ExpiredSignatureError:
   message = MedicinaList(code=-2, data=[]) #token expiro
  return message

# delete
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(TokenKey, CodeMessage, path='medicinas/delete', http_method='POST', name='medicinas.delete')
 #siempre lleva cls y request
 def medicina_remove(cls, request):
  try:
   token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
   medicinaentity = ndb.Key(urlsafe=request.entityKey)#Obtiene el elemento dado el EntitKey
   medicinaentity.delete()#BORRA
   message = CodeMessage(code=1, message='Succesfully deleted')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message

##update##
# update
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(MedicinaUpdate, CodeMessage, path='medicinas/update', http_method='POST', name='medicinas.update')
#siempre lleva cls y request
 def medicina_update(cls, request):
  try:
   token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
   user = Usuarios.get_by_id(token['user_id'])#obtiene el usuario para poder acceder a los metodos declarados en models.py en la seccion de USUARIOS
   #filialkey = ndb.Key(urlsafe=user.filial_key.urlsafe())#convierte el string dado a entityKey
   medicina = Medicina()
   if medicina.medicina_m(request, user.key)==0:#llama a la funcion declarada en models.py en la seccion de USUARIOS
    codigo=1
   else:
    codigo=-3
      #la funcion josue_m puede actualizar e insertar
      #depende de la ENTRADA de este endpoint method
   message = CodeMessage(code=1, message='Sus cambios han sido guardados exitosamente')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message









###############
# Viveres
###############
@endpoints.api(name='viveres_api', version='v1', description='viveres endpoints')
class ViveresApi(remote.Service):
###############get the info of one########
# insert
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(ViveresInput, CodeMessage, path='viveres/insert', http_method='POST', name='viveres.insert')
#siempre lleva cls y request
 def viveres_add(cls, request):
  try:
   token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
   user = Usuarios.get_by_id(token['user_id']) #obtiene el usuario para poder acceder a los metodos declarados en models.py en la seccion de
   myviveres = Viveres()
   if myviveres.viveres_m(request, user.key)==0:#llama a la funcion declarada en models.py en la seccion de USUARIOS
    codigo=1
   else:
    codigo=-3
          #la funcion josue_m puede actualizar e insertar
          #depende de la ENTRADA de este endpoint method
   message = CodeMessage(code=codigo, message='Viveres added')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message

  ########################## viveres list ###################
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(Token, ViveresList, path='viveres/list', http_method='POST', name='viveres.list')
 def viveres_list(cls, request):
  try:
   token = jwt.decode(request.tokenint, 'secret')  #checa token
   user = Usuarios.get_by_id(token['user_id']) #obtiene usuario dado el token
   lista = []  #crea lista
   lstMessage = ViveresList(code=1) # crea objeto mensaje
   lstBd = Viveres.query().fetch() # recupera de base de datos
   for i in lstBd: # recorre
    lista.append(ViveresUpdate(token='',
     entityKey=i.entityKey,
     #filial_key=user.filial_key.urlsafe(),
     code=i.code,
     description=i.description,
     urlImage=i.urlImage)) # agrega a la lista
    
   lstMessage.data = lista # la manda al messa
   message = lstMessage #regresa
    
  except jwt.DecodeError:
   message = ViveresList(code=-1, data=[]) #token invalido
  except jwt.ExpiredSignatureError:
   message = ViveresList(code=-2, data=[]) #token expiro
  return message

###############get the info of one########
 @endpoints.method(TokenKey, ViveresList, path='viveres/get', http_method='POST', name='viveres.get')
 def viveres_get(cls, request):
  try:                 
   token = jwt.decode(request.tokenint, 'secret')  #checa token
   viveresentity = ndb.Key(urlsafe=request.entityKey)
   viveres = Viveres.get_by_id(viveresentity.id()) #obtiene usuario
            #user = Usuarios.get_by_id(token['user_id']) #obtiene usuario dado el token
   lista = []  #crea lista
   lstMessage = ViveresList(code=1) # crea objeto mensaje
   lista.append(ViveresUpdate(token='', 
    entityKey= viveres.entityKey,
    #filial_key = user.filial_key.urlsafe(),
    code = viveres.code,
    description=viveres.description,
    urlImage=viveres.urlImage))
   lstMessage.data = lista#ASIGNA a la salida la lista
   message = lstMessage
  except jwt.DecodeError:
   message = ViveresList(code=-1, data=[]) #token invalido
  except jwt.ExpiredSignatureError:
   message = ViveresList(code=-2, data=[]) #token expiro
  return message

# delete
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(TokenKey, CodeMessage, path='viveres/delete', http_method='POST', name='viveres.delete')
 #siempre lleva cls y request
 def viveres_remove(cls, request):
  try:
   token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
   viveresentity = ndb.Key(urlsafe=request.entityKey)#Obtiene el elemento dado el EntitKey
   viveresentity.delete()#BORRA
   message = CodeMessage(code=1, message='Succesfully deleted')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message

##update##
# update
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(ViveresUpdate, CodeMessage, path='viveres/update', http_method='POST', name='viveres.update')
#siempre lleva cls y request
 def viveres_update(cls, request):
  try:
   token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
   user = Usuarios.get_by_id(token['user_id'])#obtiene el usuario para poder acceder a los metodos declarados en models.py en la seccion de USUARIOS
   #filialkey = ndb.Key(urlsafe=user.filial_key.urlsafe())#convierte el string dado a entityKey
   viveres = Viveres()
   if viveres.viveres_m(request, user.key)==0:#llama a la funcion declarada en models.py en la seccion de USUARIOS
    codigo=1
   else:
    codigo=-3
      #la funcion josue_m puede actualizar e insertar
      #depende de la ENTRADA de este endpoint method
   message = CodeMessage(code=1, message='Sus cambios han sido guardados exitosamente')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message












###############
# Usuarios
###############
@endpoints.api(name='usuarios_api', version='v1', description='usuarios endpoints')
class UsuariosApi(remote.Service):
###############get the info of one########
 @endpoints.method(TokenKey, UserList, path='users/get', http_method='POST', name='users.get')
 def users_get(cls, request):
  try:                 
   token = jwt.decode(request.tokenint, 'secret')  #checa token
   userentity = ndb.Key(urlsafe=request.entityKey)
   user = Usuarios.get_by_id(userentity.id()) #obtiene usuario
            #user = Usuarios.get_by_id(token['user_id']) #obtiene usuario dado el token
   lista = []  #crea lista
   lstMessage = UserList(code=1) # crea objeto mensaje
   lista.append(UserUpdate(token='', 
    entityKey= user.entityKey,
    #filial_key = user.filial_key.urlsafe(),
    email = user.email))
   lstMessage.data = lista#ASIGNA a la salida la lista
   message = lstMessage
  except jwt.DecodeError:
   message = UserList(code=-1, data=[]) #token invalido
  except jwt.ExpiredSignatureError:
   message = UserList(code=-2, data=[]) #token expiro
  return message


########################## list###################
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(Token, UserList, path='users/list', http_method='POST', name='users.list')
 def lista_usuarios(cls, request):
  try:
   token = jwt.decode(request.tokenint, 'secret')  #checa token
   user = Usuarios.get_by_id(token['user_id']) #obtiene usuario dado el token
   lista = []  #crea lista
   lstMessage = UserList(code=1) # crea objeto mensaje
   lstBd = Usuarios.query().fetch() # recupera de base de datos
   for i in lstBd: # recorre
    lista.append(UserUpdate(token='',
     entityKey=i.entityKey,
     #filial_key=user.filial_key.urlsafe(),
     email=i.email)) # agrega a la lista
    
   lstMessage.data = lista # la manda al messa
   message = lstMessage #regresa
    
  except jwt.DecodeError:
   message = UserList(code=-1, data=[]) #token invalido
  except jwt.ExpiredSignatureError:
   message = UserList(code=-2, data=[]) #token expiro
  return message

# delete
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(TokenKey, CodeMessage, path='users/delete', http_method='POST', name='users.delete')
 #siempre lleva cls y request
 def user_remove(cls, request):
  try:
   token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
   usersentity = ndb.Key(urlsafe=request.entityKey)#Obtiene el elemento dado el EntitKey
   usersentity.delete()#BORRA
   message = CodeMessage(code=1, message='Succesfully deleted')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message

# insert
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(UserInput, CodeMessage, path='users/insert', http_method='POST', name='users.insert')
 def user_add(cls, request):
  try:
   token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
   user = Usuarios.get_by_id(token['user_id'])
   if validarEmail(request.email) == False: #checa si el email esta registrado
                       #filialkey = ndb.Key(urlsafe=request.filial_key) #convierte el string dado a entityKey
    if user.usuario_m(request, user.filial_key)==0:#llama a la funcion declarada en models.py en la seccion de USUARIOS
     codigo=1
    else:
     codigo=-3
                       #la funcion josue_m puede actualizar e insertar
                       #depende de la ENTRADA de este endpoint method
    message = CodeMessage(code=codigo, message='Succesfully added')
   else:
    message = CodeMessage(code=-4, message='El email ya ha sido registrado')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message


##login##

 @endpoints.method(EmailPasswordMessage, TokenMessage, path='users/login', http_method='POST', name='users.login')
 def users_login(cls, request):
  try:
   user = Usuarios.query(Usuarios.email == request.email).fetch() #obtiene el usuario dado el email
   if not user or len(user) == 0: #si no encuentra user saca
    raise NotFoundException()
   user = user[0] 
   keye = user.filial_key.urlsafe() # regresa como mensaje el filial key
   if not user.verify_password(request.password): # checa la contrasena
    raise NotFoundException()

   token = jwt.encode({'user_id': user.key.id(), 'exp': time.time() + 43200}, 'secret') #crea el token
   message = TokenMessage(token=token, message=keye, code=1) # regresa token
  except NotFoundException:
   message = TokenMessage(token=None, message='Wrong username or password', code=-1)
  return message

##update##
# update
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(UserUpdate, CodeMessage, path='user/update', http_method='POST', name='user.update')
#siempre lleva cls y request
 def user_update(cls, request):
  try:
   token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
   user = Usuarios.get_by_id(token['user_id'])#obtiene el usuario para poder acceder a los metodos declarados en models.py en la seccion de USUARIOS
   filialkey = ndb.Key(urlsafe=user.filial_key.urlsafe())#convierte el string dado a entityKey
   if user.usuario_m(request, filialkey)==0:#llama a la funcion declarada en models.py en la seccion de USUARIOS
    codigo=1
   else:
    codigo=-3
      #la funcion josue_m puede actualizar e insertar
      #depende de la ENTRADA de este endpoint method
   message = CodeMessage(code=1, message='Sus cambios han sido guardados exitosamente')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message


'''
'''

###########################
#### Filial
###########################


## Google Cloud Endpoint
@endpoints.api(name='filiales_api', version='v1', description='filiales REST API')
class FilialesApi(remote.Service):


# get one

 @endpoints.method(TokenKey, FilialList, path='filial/get', http_method='POST', name='filial.get')
#siempre lleva cls y request
 def filial_get(cls, request):
  try:
   token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
      #Obtiene el elemento dado el entityKey
   filialentity = ndb.Key(urlsafe=request.entityKey)
      #CREA LA SALIDA de tipo JosueInput y le asigna los valores, es a como se declaro en el messages.py
      #filialentity.get().filial_key.urlsafe() para poder optener el EntityKey
     ##### ejemplo real
    ####### message = FilialList(code=1, data=[FilialUpdate(token='Succesfully get', nombre_filial=filialentity.get().nombre_filial, filial_key=filialentity.get().filial_key.urlsafe(), entityKey=filialentity.get().entityKey)])
   message = FilialList(code=1, data = [FilialUpdate(token='Succesfully get',
    entityKey = filialentity.get().entityKey,
    codigo_filial=filialentity.get().codigo_filial, 
    nombre_filial = filialentity.get().nombre_filial)])

  except jwt.DecodeError:
   message = FilialList(code=-1, data=[])
  except jwt.ExpiredSignatureError:
   message = FilialList(code=-2, data=[])
  return message




 @endpoints.method(TokenKey, CodeMessage, path='filial/delete', http_method='POST', name='filial.delete')
#siempre lleva cls y request
 def filial_remove(cls, request):
  try:
   token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
   filialentity = ndb.Key(urlsafe=request.entityKey)#Obtiene el elemento dado el EntitKey
   filialentity.delete()#BORRA
   message = CodeMessage(code=1, message='Succesfully deleted')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message


# insert
 @endpoints.method(FilialInput, CodeMessage, path='filial/insert', http_method='POST', name='filial.insert')
#siempre lleva cls y request
 def filial_add(cls, request):
  try:
   token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
   user = Usuarios.get_by_id(token['user_id'])#obtiene el usuario models.py 
   myfilial = Filial()
   if myfilial.filial_m(request)==0: 
    codigo=1
   else:
		codigo=-3
      	      #la funcion josue_m puede actualizar e insertar
	      #depende de la ENTRADA de este endpoint method
   message = CodeMessage(code=codigo, message='Succesfully added')
      #else:
	    #  message = CodeMessage(code=-4, message='Succesfully added')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message



# update
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(FilialUpdate, CodeMessage, path='filial/update', http_method='POST', name='filial.update')
#siempre lleva cls y request
 def filial_update(cls, request):
  try:
   token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN 
   user = Usuarios.get_by_id(token['user_id'])#obtiene el usuario para poder acceder a los metodos declarados en models.py en la seccion de USUARIOS
      #filialkey = ndb.Key(urlsafe=request.filial_key)#convierte el string dado a entityKey
   myfilial = Filial()
   if myfilial.filial_m(request)==0:#llama a la funcion declarada en models.py en la seccion de USUARIOS
    codigo=1
   else:
    codigo=-3
      #la funcion josue_m puede actualizar e insertar
      #depende de la ENTRADA de este endpoint method
   message = CodeMessage(code=1, message='Sus cambios han sido guardados exitosamente')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message



# list
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(Token, FilialList, path='filial/list', http_method='POST', name='filial.list')
#siempre lleva cls y request
 def filial_list(cls, request):
  try:
   token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
   user = Usuarios.get_by_id(token['user_id']) #obtiene usuario dado el token
   #if user.importante==1 or user.importante==2:
   lista = [] #crea lista para guardar contenido de la BD
   lstMessage = FilialList(code=1) #CREA el mensaje de salida
   lstBdFilial = Filial.query().fetch() #obtiene de la base de datos
   for i in lstBdFilial: #recorre la base de datos
             #inserta a la lista creada con los elementos que se necesiten de la base de datos
             #i.filial_key.urlsafe() obtiene el entityKey
	     #lista.append(ClientesUpdate(token='', nombre=i.nombre, status=i.status, filial_key=i.filial_key.urlsafe(), entityKey=i.entityKey))
    lista.append(FilialUpdate(token='', 
     entityKey = i.entityKey,
     codigo_filial=i.codigo_filial, 
     nombre_filial = i.nombre_filial))
      
   lstMessage.data = lista #ASIGNA a la salida la lista
   message = lstMessage
      #else:
      #    message = FilialList(code=-3, data=[])
  except jwt.DecodeError:
   message = FilialList(code=-1, data=[])
  except jwt.ExpiredSignatureError:
   message = FilialList(code=-2, data=[])
  return message


###########################
#### Tweets
###########################

@endpoints.api(name='tweet_api', version='v1', description='tweet REST API')
class TweetsApi(remote.Service):
# get one
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(TokenKey, TweetList, path='tweet/get', http_method='POST', name='tweet.get')
#siempre lleva cls y request
 def tweet_get(cls, request):
  try:
   token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
      #Obtiene el elemento dado el entityKey
   tweetentity = ndb.Key(urlsafe=request.entityKey)
      #CREA LA SALIDA de tipo JosueInput y le asigna los valores, es a como se declaro en el messages.py
      #josuentity.get().filial_key.urlsafe() para poder optener el EntityKey
   message = TweetList(code=1, data=[TweetUpdate(token='Succesfully get',
    entityKey=tweetentity.get().entityKey,
    #filial_key=teamentity.get().filial_key.urlsafe(), 
    title=tweetentity.get().title, 
    description=tweetentity.get().description, 
    urlImage=tweetentity.get().urlImage)])
  except jwt.DecodeError:
   message = TweetList(code=-1, data=[])
  except jwt.ExpiredSignatureError:
   message = TweetList(code=-2, data=[])
  return message


# delete
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(TokenKey, CodeMessage, path='tweet/delete', http_method='POST', name='tweet.delete')
#siempre lleva cls y request
 def tweet_remove(cls, request):
  try:
   token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
   tweetentity = ndb.Key(urlsafe=request.entityKey)#Obtiene el elemento dado el EntitKey
   tweetentity.delete()#BORRA
   message = CodeMessage(code=0, message='tweet deleted')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message

# list
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(Token, TweetList, path='tweet/list', http_method='POST', name='tweet.list')
#siempre lleva cls y request
 def tweet_list(cls, request):
  try:
   token = jwt.decode(request.tokenint, 'secret')#CHECA EL TOKEN
   user = Usuarios.get_by_id(token['user_id']) #obtiene usuario dado el token
   lista = [] #crea lista para guardar contenido de la BD
   lstMessage = TweetList(code=1) #CREA el mensaje de salida
   lstBd = Tweet.query().fetch() #obtiene de la base de datos
   for i in lstBd: #recorre la base de datos
    #inserta a la lista creada con los elementos que se necesiten de la base de datos
    #i.filial_key.urlsafe() obtiene el entityKey
	     
    lista.append(TweetUpdate(token='', 
     entityKey=i.entityKey, 
     #filial_key=i.filial_key.urlsafe(),
     title=i.title, 
     description=i.description, 
     urlImage=i.urlImage))
   lstMessage.data = lista #ASIGNA a la salida la lista
   message = lstMessage
  except jwt.DecodeError:
   message = TweetList(code=-1, data=[])
  except jwt.ExpiredSignatureError:
   message = TweetList(code=-2, data=[])
  return message

# insert
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(TweetInput, CodeMessage, path='tweet/insert', http_method='POST', name='tweet.insert')
#siempre lleva cls y request
 def tweet_add(cls, request):
  try:
   token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
   user = Usuarios.get_by_id(token['user_id']) #obtiene el usuario para poder acceder a los metodos declarados en models.py en la seccion de
   mytweet = Tweet()
   if mytweet.tweet_m(request, user.filial_key)==0:#llama a la funcion declarada en models.py en la seccion de USUARIOS
    codigo=1
   else:
    codigo=-3
          #la funcion josue_m puede actualizar e insertar
          #depende de la ENTRADA de este endpoint method
   message = CodeMessage(code=codigo, message='Tweet added')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message

# update
#                   ENTRADA    SALIDA        RUTA              siempre es POST     NOMBRE
 @endpoints.method(TweetUpdate, CodeMessage, path='tweet/update', http_method='POST', name='tweet.update')
#siempre lleva cls y request
 def tweet_update(cls, request):
  try:
   token = jwt.decode(request.token, 'secret')#CHECA EL TOKEN
   user = Usuarios.get_by_id(token['user_id'])#obtiene el usuario para poder acceder a los metodos declarados en models.py en la seccion de USUARIOS
   filialkey = ndb.Key(urlsafe=user.filial_key.urlsafe())#convierte el string dado a entityKey
   mytweet = Tweet()
   if mytweet.tweet_m(request, filialkey)==0:#llama a la funcion declarada en models.py en la seccion de USUARIOS
    codigo=1
   else:
    codigo=-3
      #la funcion josue_m puede actualizar e insertar
      #depende de la ENTRADA de este endpoint method
   message = CodeMessage(code=1, message='tweet updated')
  except jwt.DecodeError:
   message = CodeMessage(code=-2, message='Invalid token')
  except jwt.ExpiredSignatureError:
   message = CodeMessage(code=-1, message='Token expired')
  return message


application = endpoints.api_server([UsuariosApi, FilialesApi, TweetsApi, ProductsApi, MedicinasApi, ViveresApi], restricted=False)

