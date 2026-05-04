#!/usr/bin/env python3
"""
AWS Fase 3: Servicios Avanzados y Orquestación
Servicios: SQS, SNS, EventBridge, ECS/Fargate
Simulador para practicar sin cuenta real
"""

import json
from datetime import datetime
from typing import Dict, List, Any, Optional
from collections import deque
import uuid


class SQSSimulador:
    """Simulador de Amazon SQS - Colas de mensajes"""
    
    def __init__(self):
        self.colas = {}
        print("[OK] SQS Simulador inicializado")
    
    def crear_cola(self, nombre: str, tipo: str = 'standard', 
                   retencion: int = 4, visibilidad: int = 30) -> Dict:
        """Crear una nueva cola SQS"""
        url_cola = f"https://sqs.us-east-1.amazonaws.com/123456789012/{nombre}"
        
        cola = {
            'QueueName': nombre,
            'QueueUrl': url_cola,
            'QueueArn': f"arn:aws:sqs:us-east-1:123456789012:{nombre}",
            'Tipo': tipo,
            'RetencionSegundos': retencion * 3600,
            'TiempoVisibilidad': visibilidad,
            'Mensajes': deque(),
            'MensajesEnVuelo': [],
            'CreatedAt': datetime.now(),
            'ApproximateNumberOfMessages': 0
        }
        
        self.colas[nombre] = cola
        print(f"[OK] Cola creada: {nombre} (Tipo: {tipo})")
        return cola
    
    def enviar_mensaje(self, nombre_cola: str, cuerpo: str, 
                       demora: int = 0, grupo: str = None) -> Dict:
        """Enviar mensaje a una cola SQS"""
        if nombre_cola not in self.colas:
            raise ValueError(f"Cola no encontrada: {nombre_cola}")
        
        cola = self.colas[nombre_cola]
        
        mensaje = {
            'MessageId': str(uuid.uuid4()),
            'ReceiptHandle': str(uuid.uuid4()),
            'MD5OfBody': str(uuid.uuid4())[:32],
            'Body': cuerpo,
            'Attributes': {
                'SentTimestamp': datetime.now().isoformat(),
                'ApproximateReceiveCount': '0',
                'SenderId': '123456789012'
            },
            'MD5OfMessageAttributes': None,
            'MessageAttributes': {}
        }
        
        if grupo and cola['Tipo'] == 'fifo':
            mensaje['MessageGroupId'] = grupo
        
        cola['Mensajes'].append(mensaje)
        cola['ApproximateNumberOfMessages'] = len(cola['Mensajes'])
        
        print(f"[OK] Mensaje enviado a {nombre_cola}: {cuerpo[:50]}...")
        return mensaje
    
    def recibir_mensaje(self, nombre_cola: str, max_mensajes: int = 1,
                        espera: int = 0) -> List[Dict]:
        """Recibir mensajes de una cola SQS"""
        if nombre_cola not in self.colas:
            raise ValueError(f"Cola no encontrada: {nombre_cola}")
        
        cola = self.colas[nombre_cola]
        mensajes = []
        
        for _ in range(min(max_mensajes, len(cola['Mensajes']))):
            if cola['Mensajes']:
                mensaje = cola['Mensajes'].popleft()
                mensaje['Attributes']['ApproximateReceiveCount'] = str(
                    int(mensaje['Attributes']['ApproximateReceiveCount']) + 1
                )
                cola['MensajesEnVuelo'].append(mensaje)
                mensajes.append(mensaje)
        
        cola['ApproximateNumberOfMessages'] = len(cola['Mensajes'])
        
        if mensajes:
            print(f"[OK] Mensajes recibidos de {nombre_cola}: {len(mensajes)}")
        else:
            print(f"[INFO] No hay mensajes en {nombre_cola}")
        
        return mensajes
    
    def eliminar_mensaje(self, nombre_cola: str, receipt_handle: str):
        """Eliminar mensaje de una cola"""
        if nombre_cola not in self.colas:
            raise ValueError(f"Cola no encontrada: {nombre_cola}")
        
        cola = self.colas[nombre_cola]
        cola['MensajesEnVuelo'] = [
            m for m in cola['MensajesEnVuelo'] 
            if m['ReceiptHandle'] != receipt_handle
        ]
        
        print(f"[OK] Mensaje eliminado de {nombre_cola}")
    
    def listar_colas(self) -> List[Dict]:
        """Listar todas las colas"""
        print("\n" + "="*60)
        print("COLAS SQS")
        print("="*60)
        
        for nombre, cola in self.colas.items():
            print(f"  • {nombre} ({cola['Tipo']})")
            print(f"    URL: {cola['QueueUrl']}")
            print(f"    Mensajes: {cola['ApproximateNumberOfMessages']}")
            print(f"    Creada: {cola['CreatedAt'].strftime('%Y-%m-%d %H:%M')}")
            print()
        
        return list(self.colas.values())


class SNSSimulador:
    """Simulador de Amazon SNS - Notificaciones"""
    
    def __init__(self):
        self.topics = {}
        self.suscripciones = []
        print("[OK] SNS Simulador inicializado")
    
    def crear_topic(self, nombre: str) -> Dict:
        """Crear un nuevo topic SNS"""
        topic_arn = f"arn:aws:sns:us-east-1:123456789012:{nombre}"
        
        topic = {
            'TopicArn': topic_arn,
            'DisplayName': nombre,
            'TopicName': nombre,
            'Subscriptions': [],
            'CreatedAt': datetime.now(),
            'MensajesPublicados': 0
        }
        
        self.topics[nombre] = topic
        print(f"[OK] Topic creado: {nombre}")
        return topic
    
    def suscribir(self, topic_nombre: str, protocolo: str, endpoint: str) -> Dict:
        """Suscribir un endpoint a un topic"""
        if topic_nombre not in self.topics:
            raise ValueError(f"Topic no encontrado: {topic_nombre}")
        
        suscripcion = {
            'SubscriptionArn': f"arn:aws:sns:us-east-1:123456789012:{topic_nombre}:{uuid.uuid4().hex[:8]}",
            'TopicArn': self.topics[topic_nombre]['TopicArn'],
            'Protocol': protocolo,
            'Endpoint': endpoint,
            'Status': 'Confirmed',
            'CreatedAt': datetime.now()
        }
        
        self.topics[topic_nombre]['Subscriptions'].append(suscripcion)
        self.suscripciones.append(suscripcion)
        
        print(f"[OK] Suscripción creada: {protocolo} -> {endpoint}")
        return suscripcion
    
    def publicar(self, topic_nombre: str, mensaje: str, asunto: str = None) -> Dict:
        """Publicar mensaje en un topic"""
        if topic_nombre not in self.topics:
            raise ValueError(f"Topic no encontrado: {topic_nombre}")
        
        topic = self.topics[topic_nombre]
        mensaje_id = str(uuid.uuid4())
        
        publicacion = {
            'MessageId': mensaje_id,
            'TopicArn': topic['TopicArn'],
            'Message': mensaje,
            'Subject': asunto,
            'Timestamp': datetime.now().isoformat(),
            'Destinatarios': len(topic['Subscriptions'])
        }
        
        topic['MensajesPublicados'] += 1
        
        # Simular envío a suscriptores
        for suscripcion in topic['Subscriptions']:
            print(f"  -> Enviado a {suscripcion['Protocol']}: {suscripcion['Endpoint']}")
        
        print(f"[OK] Mensaje publicado en {topic_nombre}: {mensaje[:50]}...")
        return publicacion
    
    def listar_topics(self) -> List[Dict]:
        """Listar todos los topics"""
        print("\n" + "="*60)
        print("TOPICS SNS")
        print("="*60)
        
        for nombre, topic in self.topics.items():
            print(f"  • {nombre}")
            print(f"    ARN: {topic['TopicArn']}")
            print(f"    Suscripciones: {len(topic['Subscriptions'])}")
            print(f"    Mensajes: {topic['MensajesPublicados']}")
            print()
        
        return list(self.topics.values())


class EventBridgeSimulador:
    """Simulador de Amazon EventBridge - Orquestación de eventos"""
    
    def __init__(self):
        self.eventos = []
        self.reglas = {}
        self.destinos = {}
        print("[OK] EventBridge Simulador inicializado")
    
    def crear_regla(self, nombre: str, patron_evento: Dict, 
                    descripcion: str = "") -> Dict:
        """Crear una regla de EventBridge"""
        regla = {
            'Name': nombre,
            'Arn': f"arn:aws:events:us-east-1:123456789012:rule/{nombre}",
            'EventPattern': json.dumps(patron_evento, indent=2),
            'Description': descripcion,
            'State': 'ENABLED',
            'CreatedAt': datetime.now(),
            'EventosProcesados': 0
        }
        
        self.reglas[nombre] = regla
        print(f"[OK] Regla creada: {nombre}")
        return regla
    
    def agregar_destino(self, regla_nombre: str, destino_arn: str, 
                        tipo: str = 'lambda') -> Dict:
        """Agregar destino a una regla"""
        if regla_nombre not in self.reglas:
            raise ValueError(f"Regla no encontrada: {regla_nombre}")
        
        destino = {
            'Id': str(uuid.uuid4())[:8],
            'Arn': destino_arn,
            'Type': tipo,
            'Regla': regla_nombre
        }
        
        if regla_nombre not in self.destinos:
            self.destinos[regla_nombre] = []
        
        self.destinos[regla_nombre].append(destino)
        
        print(f"[OK] Destino agregado a {regla_nombre}: {tipo}")
        return destino
    
    def enviar_evento(self, origen: str, tipo_evento: str, 
                      detalle: Dict) -> Dict:
        """Enviar evento a EventBridge"""
        evento = {
            'EventId': str(uuid.uuid4()),
            'Source': origen,
            'DetailType': tipo_evento,
            'Detail': json.dumps(detalle),
            'Time': datetime.now().isoformat(),
            'Region': 'us-east-1',
            'ReglasActivadas': []
        }
        
        # Procesar reglas
        for nombre, regla in self.reglas.items():
            patron = json.loads(regla['EventPattern'])
            if self._coincide_patron(evento, patron):
                evento['ReglasActivadas'].append(nombre)
                regla['EventosProcesados'] += 1
                
        # Enviar a destinos
        for destino in self.destinos.get(nombre, []):
            print(f"  -> Evento enviado a: {destino['Type']}")
        
        self.eventos.append(evento)
        
        if evento['ReglasActivadas']:
            print(f"[OK] Evento procesado: {tipo_evento} -> {evento['ReglasActivadas']}")
        else:
            print(f"[INFO] Evento sin reglas: {tipo_evento}")
        
        return evento
    
    def _coincide_patron(self, evento: Dict, patron: Dict) -> bool:
        """Verificar si evento coincide con patrón"""
        # Simulación simplificada
        if 'source' in patron:
            if evento['Source'] not in patron['source']:
                return False
        if 'detail-type' in patron:
            if evento['DetailType'] not in patron['detail-type']:
                return False
        return True
    
    def listar_reglas(self) -> List[Dict]:
        """Listar todas las reglas"""
        print("\n" + "="*60)
        print("REGLAS EVENTBRIDGE")
        print("="*60)
        
        for nombre, regla in self.reglas.items():
            print(f"  • {nombre}")
            print(f"    Estado: {regla['State']}")
            print(f"    Eventos: {regla['EventosProcesados']}")
            print(f"    Destinos: {len(self.destinos.get(nombre, []))}")
            print()
        
        return list(self.reglas.values())


class ECSFargateSimulador:
    """Simulador de Amazon ECS/Fargate - Contenedores serverless"""
    
    def __init__(self):
        self.clusters = {}
        self.tareas = {}
        self.servicios = {}
        print("[OK] ECS/Fargate Simulador inicializado")
    
    def crear_cluster(self, nombre: str) -> Dict:
        """Crear un nuevo cluster ECS"""
        cluster = {
            'ClusterName': nombre,
            'ClusterArn': f"arn:aws:ecs:us-east-1:123456789012:cluster/{nombre}",
            'Status': 'ACTIVE',
            'RunningTasksCount': 0,
            'PendingTasksCount': 0,
            'RegisteredContainerInstancesCount': 0,
            'CreatedAt': datetime.now()
        }
        
        self.clusters[nombre] = cluster
        print(f"[OK] Cluster creado: {nombre}")
        return cluster
    
    def crear_tarea(self, cluster_nombre: str, nombre: str, 
                    imagen: str, cpu: int = 256, memoria: int = 512) -> Dict:
        """Crear una definición de tarea"""
        if cluster_nombre not in self.clusters:
            raise ValueError(f"Cluster no encontrado: {cluster_nombre}")
        
        tarea = {
            'TaskDefinitionArn': f"arn:aws:ecs:us-east-1:123456789012:task-definition/{nombre}:1",
            'Family': nombre,
            'Revision': 1,
            'Status': 'ACTIVE',
            'RequiresAttributes': [],
            'ContainerDefinitions': [
                {
                    'Name': nombre,
                    'Image': imagen,
                    'Cpu': cpu,
                    'Memory': memoria,
                    'Essential': True,
                    'PortMappings': [],
                    'Environment': []
                }
            ],
            'Cpu': str(cpu),
            'Memory': str(memoria),
            'NetworkMode': 'awsvpc',
            'Fargate': True,
            'CreatedAt': datetime.now()
        }
        
        self.tareas[nombre] = tarea
        print(f"[OK] Tarea creada: {nombre} ({imagen})")
        return tarea
    
    def crear_servicio(self, cluster_nombre: str, nombre: str, 
                       tarea_nombre: str, conteo: int = 1) -> Dict:
        """Crear un servicio ECS"""
        if cluster_nombre not in self.clusters:
            raise ValueError(f"Cluster no encontrado: {cluster_nombre}")
        
        if tarea_nombre not in self.tareas:
            raise ValueError(f"Tarea no encontrada: {tarea_nombre}")
        
        servicio = {
            'ServiceName': nombre,
            'ServiceArn': f"arn:aws:ecs:us-east-1:123456789012:service/{cluster_nombre}/{nombre}",
            'Cluster': cluster_nombre,
            'TaskDefinition': tarea_nombre,
            'DesiredCount': conteo,
            'RunningCount': 0,
            'PendingCount': conteo,
            'LaunchType': 'FARGATE',
            'PlatformVersion': '1.4.0',
            'Status': 'ACTIVE',
            'CreatedAt': datetime.now()
        }
        
        self.servicios[nombre] = servicio
        self.clusters[cluster_nombre]['RunningTasksCount'] += conteo
        
        print(f"[OK] Servicio creado: {nombre} (Tareas: {conteo})")
        return servicio
    
    def escalar_servicio(self, nombre: str, conteo: int) -> Dict:
        """Escalar un servicio existente"""
        if nombre not in self.servicios:
            raise ValueError(f"Servicio no encontrado: {nombre}")
        
        servicio = self.servicios[nombre]
        anterior = servicio['DesiredCount']
        servicio['DesiredCount'] = conteo
        servicio['PendingCount'] = conteo - servicio['RunningCount']
        
        cluster = self.clusters[servicio['Cluster']]
        cluster['RunningTasksCount'] += (conteo - anterior)
        
        print(f"[OK] Servicio {nombre} escalado: {anterior} -> {conteo}")
        return servicio
    
    def listar_recursos(self) -> Dict:
        """Listar todos los recursos ECS"""
        print("\n" + "="*60)
        print("RECURSOS ECS/FARGATE")
        print("="*60)
        
        print("\nCLUSTERS:")
        for nombre, cluster in self.clusters.items():
            print(f"  • {nombre}")
            print(f"    Tareas: {cluster['RunningTasksCount']}")
            print(f"    Instancias: {cluster['RegisteredContainerInstancesCount']}")
        
        print("\nTAREAS:")
        for nombre, tarea in self.tareas.items():
            print(f"  • {nombre}")
            print(f"    CPU: {tarea['Cpu']} | Memoria: {tarea['Memory']} MB")
            print(f"    Imagen: {tarea['ContainerDefinitions'][0]['Image']}")
        
        print("\nSERVICIOS:")
        for nombre, servicio in self.servicios.items():
            print(f"  • {nombre}")
            print(f"    Cluster: {servicio['Cluster']}")
            print(f"    Deseado: {servicio['DesiredCount']}")
            print(f"    Ejecutándose: {servicio['RunningCount']}")
        
        return {
            'clusters': list(self.clusters.values()),
            'tareas': list(self.tareas.values()),
            'servicios': list(self.servicios.values())
        }


class AWSSimuladorFase3:
    """Simulador completo AWS Fase 3 - Servicios Avanzados"""
    
    def __init__(self):
        self.sqs = SQSSimulador()
        self.sns = SNSSimulador()
        self.eventbridge = EventBridgeSimulador()
        self.ecs = ECSFargateSimulador()
        print("\n[OK] AWS Fase 3 - Simulador de Servicios Avanzados")
        print("="*60)
    
    def demo_completa(self):
        """Ejecutar demostración completa de servicios"""
        print("\n" + "="*60)
        print("DEMONSTRACIÓN AWS FASE 3")
        print("="*60)
        
        # 1. SQS - Colas de mensajes
        print("\n[SQS] 1. SQS - Colas de Mensajes")
        self.sqs.crear_cola("pedidos-colas", "fifo")
        self.sqs.enviar_mensaje("pedidos-colas", "Pedido #1234 procesado", grupo="pedidos")
        self.sqs.enviar_mensaje("pedidos-colas", "Pedido #1235 procesado", grupo="pedidos")
        mensajes = self.sqs.recibir_mensaje("pedidos-colas", max_mensajes=2)
        for msg in mensajes:
            print(f"  -> Procesado: {msg['Body']}")
        
        # 2. SNS - Notificaciones
        print("\n[SNS] 2. SNS - Notificaciones")
        self.sns.crear_topic("notificaciones-pedidos")
        self.sns.suscribir("notificaciones-pedidos", "email", "admin@empresa.com")
        self.sns.suscribir("notificaciones-pedidos", "lambda", "arn:aws:lambda:us-east-1:123456789012:function:procesar-notificacion")
        self.sns.publicar("notificaciones-pedidos", "Nuevo pedido recibido", "Nuevo Pedido")
        
        # 3. EventBridge - Orquestación
        print("\n[EventBridge] 3. EventBridge - Orquestación")
        self.eventbridge.crear_regla(
            "procesar-pedido",
            {
                "source": ["com.empresa.pedidos"],
                "detail-type": ["PedidoCreado"]
            },
            "Procesa nuevos pedidos"
        )
        self.eventbridge.agregar_destino("procesar-pedido", 
            "arn:aws:lambda:us-east-1:123456789012:function:procesar-pedido",
            "lambda"
        )
        self.eventbridge.enviar_evento(
            "com.empresa.pedidos",
            "PedidoCreado",
            {"pedido_id": "1234", "cliente": "Juan Perez", "total": 150.00}
        )
        
        # 4. ECS/Fargate - Contenedores
        print("\n[ECS] 4. ECS/Fargate - Contenedores Serverless")
        self.ecs.crear_cluster("cluster-produccion")
        self.ecs.crear_tarea("cluster-produccion", "api-rest", 
            "123456789012.dkr.ecr.us-east-1.amazonaws.com/api-rest:latest",
            cpu=512, memoria=1024
        )
        self.ecs.crear_servicio("cluster-produccion", "api-rest-svc", 
            "api-rest", conteo=2)
        self.ecs.escalar_servicio("api-rest-svc", 4)
        
        # Mostrar estado final
        self.sqs.listar_colas()
        self.sns.listar_topics()
        self.eventbridge.listar_reglas()
        self.ecs.listar_recursos()
        
        print("\n" + "="*60)
        print("OK - DEMOSTRACION COMPLETADA")
        print("="*60)


if __name__ == "__main__":
    # Ejecutar demostración
    simulador = AWSSimuladorFase3()
    simulador.demo_completa()
