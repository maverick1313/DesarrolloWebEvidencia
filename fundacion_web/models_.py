import base64
import Crypto
from Crypto.Hash import SHA256
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from protorpc import remote
from endpoints_proto_datastore.ndb import EndpointsModel
import endpoints
from google.appengine.api import mail
from google.appengine.ext.webapp import blobstore_handlers

class CustomBaseModel(EndpointsModel):
    def populate(self, data):
        super(self.__class__, self).__init__()
        for attr in self._message_fields_schema:
            if hasattr(data, attr):
                setattr(self, attr, getattr(data, attr))

## filial
class Filial(CustomBaseModel):
    _message_fields_schema = ('entityKey', 'codigo_filial', 'nombre_filial')
    codigo_filial = ndb.StringProperty()
    nombre_filial = ndb.StringProperty()
    
       ###filial####
    def filial_m(self, data):
        filial = Filial()#Crea una variable de tipo Base de datos
        filial.populate(data)#Llena la variables con los datos dados por el request en main.py
        #filial.filial_key=filialkey #inserta el entityKey de la filial que es un parametro que se manda en main.py
        filial.put()#inserta o hace un update depende del main.py
        return 0



#####USUARIOS#########

class Usuarios(CustomBaseModel):
    _message_fields_schema = ('entityKey', 'email', 'password', 'salt')

    filial_key = ndb.KeyProperty(kind=Filial)
    email = ndb.StringProperty()
    password = ndb.StringProperty()
    salt = ndb.StringProperty(indexed=False)
   
 
    def hash_password(self):
        """ Create a cryptographyc random secure salt and hash the password
            using the salt created and store both in the database, the password
            and the salt """
        # Note: It is needed to encode in base64 the salt, otherwise it will
        # cause an exception trying to store non utf-8 characteres
        self.salt = base64.urlsafe_b64encode(
            Crypto.Random.get_random_bytes(16))
        hash_helper = SHA256.new()
        hash_helper.update(self.password + self.salt)
        self.password = hash_helper.hexdigest()

    def verify_password(self, password):
        """ Verify if the password is correct """
        hash_helper = SHA256.new()
        hash_helper.update(password + self.salt)
        return hash_helper.hexdigest() == self.password

       ###Usuarios####
    def usuario_m(self, data, filialkey):
        user = Usuarios()#Crea una variable de tipo Base de datos
        user.populate(data)#Llena la variables con los datos dados por el request en main.py
        user.filial_key=filialkey
        user.status=1
        user.hash_password()#encripta la contrasena
        user.put()#inserta o hace un update depende del main.py
        return 0


######### Tweets #########

class Tweet(CustomBaseModel):
    _message_fields_schema = ('entityKey', 'title', 'description', 'urlImage')
    filial_key = ndb.KeyProperty(kind=Filial)
    title = ndb.StringProperty()
    description = ndb.StringProperty()
    urlImage = ndb.StringProperty()
 
    ### Tweet ####
    def tweet_m(self, data, filialkey):
        tweet  = Tweet()#Crea una variable de tipo Tweet
        tweet.populate(data)#Llena la variables con los datos dados por el request en main.py
        tweet.filial_key=filialkey#inserta el entityKey de la filial que es un parametro que se manda en main.py
        tweet.put()#inserta o hace un update depende del main.py
        return 0

######### Product #########

class Product(CustomBaseModel):
    _message_fields_schema = ('entityKey', 'code', 'description', 'urlImage')
    user_key = ndb.KeyProperty(kind=Usuarios)
    code = ndb.StringProperty()
    description = ndb.StringProperty()
    urlImage = ndb.StringProperty()
 
    ### Add product ####
    def product_m(self, data, userkey):
        product  = Product()#Crea una variable de tipo Tweet
        product.populate(data)#Llena la variables con los datos dados por el request en main.py
        product.user_key=userkey#inserta el entityKey de la filial que es un parametro que se manda en main.py
        product.put()#inserta o hace un update depende del main.py
        return 0

######### Medicina #########

class Medicina(CustomBaseModel):
    _message_fields_schema = ('entityKey', 'title', 'description', 'urlImage')
    #user_key = ndb.KeyProperty(kind=Usuarios)
    filial_key = ndb.KeyProperty(kind=Filial)
    title = ndb.StringProperty()
    description = ndb.StringProperty()
    urlImage = ndb.StringProperty()
 
    ### Add medicina ####
    def medicina_m(self, data, filialkey):
        medicina  = Medicina()#Crea una variable de tipo Tweet
        medicina.populate(data)#Llena la variables con los datos dados por el request en main.py
        medicina.filial_key=filialkey#inserta el entityKey de la filial que es un parametro que se manda en main.py
        medicina.put()#inserta o hace un update depende del main.py
        return 0

######### Viveres #########

class Viveres(CustomBaseModel):
    _message_fields_schema = ('entityKey', 'code', 'description', 'urlImage')
    #user_key = ndb.KeyProperty(kind=Usuarios)
    filial_key = ndb.KeyProperty(kind=Filial)
    title = ndb.StringProperty()
    description = ndb.StringProperty()
    urlImage = ndb.StringProperty()
 
    ### Add medicina ####
    def viveres_m(self, data, userkey):
        viveres  = Viveres()#Crea una variable de tipo Tweet
        viveres.populate(data)#Llena la variables con los datos dados por el request en main.py
        viveres.filial_key=filialkey#inserta el entityKey de la filial que es un parametro que se manda en main.py
        viveres.put()#inserta o hace un update depende del main.py
        return 0

#### create demo

def validarEmail(email):
    emailv = Usuarios.query(Usuarios.email == email)
    if not emailv.get():
        return False
    else:
        return True

#### create root filial

if validarEmail("maverick@gmail.com") == False:  # mismo mail
    filialAdmin = Filial(
      codigo_filial = 'puebla',
      nombre_filial="puebla srl de cv",
    )
    filialAdmin.put()


#### create root user  

    keyadmincol = ndb.Key(urlsafe=filialAdmin.entityKey)
    admin = Usuarios(
          filial_key = keyadmincol,
          email="maverick@gmail.com", #mismo mail
          password="maverick",

    #### create root user  

    keyadmincol = ndb.Key(urlsafe=filialAdmin.entityKey)
    admin = Usuarios(
          filial_key = keyadmincol,
          email="maverick2@gmail.com", #mismo mail
          password="maverick2",
       
    )
    admin.hash_password()
    admin.put()
