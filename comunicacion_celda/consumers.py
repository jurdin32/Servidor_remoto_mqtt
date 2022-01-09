from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
import json
from random import randint
from asyncio import sleep
from  .Funciones_para_comunicacion_mqtt import publish, connect_mqtt
import paho.mqtt.subscribe as subscribe
import paho.mqtt.client as mqtt


topic = "python/mqtt/Activar_Celda"
topic1 = "python/mqtt/Lista_Pesos"
topic2 = "python/mqtt/Notificaciones"
topic3 = "python/mqtt/MV"
topic4 = "python/mqtt/Detener_Clacificacion"
topic5 = "python/mqtt/CP"
topic8 = "python/mqtt/CM"
topic6 = "python/mqtt/Estado"
topic9 = "python/mqtt/Posicion_Inicial"
# Create your views here.

class Mensajes_MQTT(object):
    def __init__(self,broker,port,topic,username,password,client_id,protocolo):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.username=username
        self.password=password
        self.client_id=client_id
        self.protocolo=protocolo
    def Recibir_mensajes(self):
        msg1 = subscribe.simple(self.topic, qos=0, msg_count=1, retained=False, hostname=self.broker,
        port=self.port, client_id=self.client_id, keepalive=60, will=None, auth=None, tls=None,protocol=self.protocolo)
        print("Pesos", msg1.payload.decode("utf-8"), "Tipo", type(msg1.payload.decode("utf-8")))
        mensaje = msg1.payload.decode("utf-8")
        return mensaje

    def Enviar_mensajes(self,orden):
        client = connect_mqtt(self.broker, self.port, self.username, self.password,self.client_id)
        client.loop_start()
        publish(self.client, self.topic, orden)


class datos_recibidos(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Parametros para comunicacion MQTT
        broker = 'broker.emqx.io'
        port = 1883
        username = 'emqx'
        password = 'public'
        # generate client ID with pub prefix randomly
        client_id = f'python-mqtt-{randint(100, 1000)}'
        protocolo = mqtt.MQTTv311
        topic_mensajes = "python/mqtt/mensajes"


        # Creamos el objeto mesnajes 
        Obj_mensajes = Mensajes_MQTT(broker, port, topic_mensajes, username, password, client_id, protocolo)

        while True:
            await self.send(json.dumps({'value': json.loads(Obj_mensajes.Recibir_mensajes())}))
            await sleep(0.5)

class Iniciar_celda(WebsocketConsumer):
    def connect(self):
        self.accept()
    def receive(self, text_data):
        ''' Cliente envía información y nosotros la recibimos '''
        text_data_json = json.loads(text_data)
        text = text_data_json['text']

        self.send(json.dumps({'value': text}))
        print("text",type(text),text)

         # Parametros para comunicacion MQTT
        broker = 'broker.emqx.io'
        port = 1883
        username = 'emqx'
        password = 'public'
        # generate client ID with pub prefix randomly
        client_id = f'python-mqtt-{randint(100, 1000)}'
        protocolo = mqtt.MQTTv311
        topic = "python/mqtt/Activar_Celda"

        # Creamos la coneccion y publicamos al broker
        client=connect_mqtt(client_id,username,password,broker,port)
        client.loop_start()
        publish(client, topic, str(text))
        
   
            
    


class Detener_celda(WebsocketConsumer):
    def connect(self):
        self.accept()
    def receive(self, text_data):
        ''' Cliente envía información y nosotros la recibimos '''
        text_data_json = json.loads(text_data)
        text = text_data_json['text']


         # Parametros para comunicacion MQTT
        broker = 'broker.emqx.io'
        port = 1883
        username = 'emqx'
        password = 'public'
        # generate client ID with pub prefix randomly
        client_id = f'python-mqtt-{randint(100, 1000)}'
        protocolo = mqtt.MQTTv311
        topic = "python/mqtt/Activar_Celda"

        # Creamos la coneccion y publicamos al broker
        client=connect_mqtt(client_id,username,password,broker,port)
        client.loop_start()
        publish(client, topic, str(text))
        

        self.send(json.dumps({'value': text}))





class Activar_colocacion(WebsocketConsumer):
    def connect(self):
        self.accept()
    def receive(self, text_data):
        ''' Cliente envía información y nosotros la recibimos '''
        text_data_json = json.loads(text_data)
        text = text_data_json['text']


         # Parametros para comunicacion MQTT
        broker = 'broker.emqx.io'
        port = 1883
        username = 'emqx'
        password = 'public'
        # generate client ID with pub prefix randomly
        client_id = f'python-mqtt-{randint(100, 1000)}'
        protocolo = mqtt.MQTTv311
        topic6 = "python/mqtt/Estado"

        # Creamos la coneccion y publicamos al broker
        client=connect_mqtt(client_id,username,password,broker,port)
        client.loop_start()
        publish(client, topic6, str(text))
        



        self.send(json.dumps({'value': text}))



class Detener_colocacion(WebsocketConsumer):
    def connect(self):
        self.accept()
    def receive(self, text_data):
        ''' Cliente envía información y nosotros la recibimos '''
        text_data_json = json.loads(text_data)
        text = text_data_json['text']
        self.send(json.dumps({'value': text}))

           # Parametros para comunicacion MQTT
        broker = 'broker.emqx.io'
        port = 1883
        username = 'emqx'
        password = 'public'
        # generate client ID with pub prefix randomly
        client_id = f'python-mqtt-{randint(100, 1000)}'
        protocolo = mqtt.MQTTv311
        topic6 = "python/mqtt/Estado"

        # Creamos la coneccion y publicamos al broker
        client=connect_mqtt(client_id,username,password,broker,port)
        client.loop_start()
        publish(client, topic6, str(text))
        


        
class Activar_taladrado(WebsocketConsumer):
    def connect(self):
        self.accept()
    def receive(self, text_data):
        ''' Cliente envía información y nosotros la recibimos '''
        text_data_json = json.loads(text_data)
        text = text_data_json['text']


        # Parametros para comunicacion MQTT
        broker = 'broker.emqx.io'
        port = 1883
        username = 'emqx'
        password = 'public'
        # generate client ID with pub prefix randomly
        client_id = f'python-mqtt-{randint(100, 1000)}'
        protocolo = mqtt.MQTTv311
        topic4 = "python/mqtt/Detener_taladrado"

        # Creamos la coneccion y publicamos al broker
        client=connect_mqtt(client_id,username,password,broker,port)
        client.loop_start()
        publish(client, topic4, str(text))
        


        self.send(json.dumps({'value': text}))



class Desactivar_taladrado(WebsocketConsumer):
    def connect(self):
        self.accept()
    def receive(self, text_data):
        ''' Cliente envía información y nosotros la recibimos '''
        text_data_json = json.loads(text_data)
        text = text_data_json['text']

           # Parametros para comunicacion MQTT
        broker = 'broker.emqx.io'
        port = 1883
        username = 'emqx'
        password = 'public'
        # generate client ID with pub prefix randomly
        client_id = f'python-mqtt-{randint(100, 1000)}'
        protocolo = mqtt.MQTTv311
        topic4 = "python/mqtt/Detener_taladrado"

        # Creamos la coneccion y publicamos al broker
        client=connect_mqtt(client_id,username,password,broker,port)
        client.loop_start()
        publish(client, topic4, str(text))
        

        self.send(json.dumps({'value': text}))


class Reiniciar_celda(WebsocketConsumer):
    def connect(self):
        self.accept()
    def receive(self, text_data):
        ''' Cliente envía información y nosotros la recibimos '''
        text_data_json = json.loads(text_data)
        text = text_data_json['text']


           # Parametros para comunicacion MQTT
        broker = 'broker.emqx.io'
        port = 1883
        username = 'emqx'
        password = 'public'
        # generate client ID with pub prefix randomly
        client_id = f'python-mqtt-{randint(100, 1000)}'
        protocolo = mqtt.MQTTv311
        topic9 = "python/mqtt/Posicion_Inicial"

        # Creamos la coneccion y publicamos al broker
        client=connect_mqtt(client_id,username,password,broker,port)
        client.loop_start()
        publish(client, topic9, str(text))
        


        self.send(json.dumps({'value': text}))


