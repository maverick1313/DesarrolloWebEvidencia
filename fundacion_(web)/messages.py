from protorpc import messages
from protorpc import message_types

class MessageNone(messages.Message):
    inti = messages.StringField(1)
# Input messages
#Recibe el token para validar
class Token(messages.Message):
    tokenint = messages.StringField(1, required=True)
    #entityKey = messages.StringField(2, required=False)
    #fromurl = messages.StringField(3)

#Recibe el token y un entityKey de cualquier base de datos para validar
class TokenKey(messages.Message):
    tokenint = messages.StringField(1, required=True)
    entityKey = messages.StringField(2, required=True)
    #fromurl = messages.StringField(3)


#Recibe el email y contrasena para la creacion de token
class EmailPasswordMessage(messages.Message):
    email = messages.StringField(1, required=True)
    password = messages.StringField(2, required=True)

# Output messages
#regresa un token
class TokenMessage(messages.Message):
    code = messages.IntegerField(1)
    message = messages.StringField(2)
    token = messages.StringField(3)

#regresa mensajes de lo ocurrido
class CodeMessage(messages.Message):
    code = messages.IntegerField(1)
    message = messages.StringField(2)

#USERS
class UserInput(messages.Message):
    token = messages.StringField(1) 
    filial_key = messages.StringField(2)
    email = messages.StringField(3)
    password = messages.StringField(4)



class UserUpdate(messages.Message):
    token = messages.StringField(1)
    email = messages.StringField(2)
    password = messages.StringField(3)
    entityKey = messages.StringField(4, required=True)

class UserList(messages.Message):
    code = messages.IntegerField(1)
    data = messages.MessageField(UserUpdate, 2, repeated=True)


###### Filial ########

#Mensaje de Entrada y Salida para la base de datos Filial
class FilialInput(messages.Message):
    token = messages.StringField(1, required=True) 
    codigo_filial = messages.StringField(2)
    nombre_filial = messages.StringField(3)


class FilialUpdate(messages.Message):
    token = messages.StringField(1, required=True)
    entityKey = messages.StringField(2, required=True)
    codigo_filial = messages.StringField(3)
    nombre_filial = messages.StringField(4)



#regresa una lista para la base de datos Filial
class FilialList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIELD que regresa una lista de tipo FilialUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(FilialUpdate, 2, repeated=True)


######Team########

#Mensaje de Entrada y Salida para Tweets
class TweetInput(messages.Message):
    token = messages.StringField(1, required=True) 
    title = messages.StringField(2)
    description = messages.StringField(3)
    urlImage = messages.StringField(5)

    
class TweetUpdate(messages.Message):
    token = messages.StringField(1, required=True)
    #filial_key = messages.StringField(2, required=True)
    entityKey = messages.StringField(2, required=True)
    title = messages.StringField(3)
    description = messages.StringField(4)
    urlImage = messages.StringField(5)

#regresa una lista para la base de datos Filial
class TweetList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIELD que regresa una lista de tipo TeamUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(TweetUpdate, 2, repeated=True)

   
######Product########

#Mensaje de Entrada y Salida para Tweets
class ProductInput(messages.Message):
    token = messages.StringField(1, required=True) 
    code = messages.StringField(2)
    description = messages.StringField(3)
    urlImage = messages.StringField(5)

class ProductUpdate(messages.Message):
    token = messages.StringField(1, required=True)
    #filial_key = messages.StringField(2, required=True)
    entityKey = messages.StringField(2, required=True)
    code = messages.StringField(3)
    description = messages.StringField(4)
    urlImage = messages.StringField(5)

#regresa una lista para la base de datos Filial
class ProductList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIELD que regresa una lista de tipo TeamUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(ProductUpdate, 2, repeated=True)

######Medicina########

#Mensaje de Entrada y Salida para Tweets
class MedicinaInput(messages.Message):
    token = messages.StringField(1, required=True) 
    title = messages.StringField(2)
    description = messages.StringField(3)
    urlImage = messages.StringField(5)

class MedicinaUpdate(messages.Message):
    token = messages.StringField(1, required=True)
    #filial_key = messages.StringField(2, required=True)
    entityKey = messages.StringField(2, required=True)
    title = messages.StringField(3)
    description = messages.StringField(4)
    urlImage = messages.StringField(5)

#regresa una lista para la base de datos Filial
class MedicinaList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIELD que regresa una lista de tipo TeamUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(MedicinaUpdate, 2, repeated=True)


######Viveres########

#Mensaje de Entrada y Salida para Tweets
class ViveresInput(messages.Message):
    token = messages.StringField(1, required=True) 
    code = messages.StringField(2)
    description = messages.StringField(3)
    urlImage = messages.StringField(5)

class ViveresUpdate(messages.Message):
    token = messages.StringField(1, required=True)
    #filial_key = messages.StringField(2, required=True)
    entityKey = messages.StringField(2, required=True)
    code = messages.StringField(3)
    description = messages.StringField(4)
    urlImage = messages.StringField(5)

#regresa una lista para la base de datos Filial
class ViveresList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIELD que regresa una lista de tipo TeamUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(ViveresUpdate, 2, repeated=True)







