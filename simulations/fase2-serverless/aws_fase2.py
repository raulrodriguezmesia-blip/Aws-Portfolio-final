#!/usr/bin/env python3
"""
AWS Fase 2: Desarrollo y Bases de Datos
Servicios: Lambda, API Gateway, DynamoDB, RDS
Simulador para practicar sin cuenta real
"""

import json
from datetime import datetime
from typing import Dict, List, Any, Optional


class AWSLambdaSimulador:
    """Simulador de AWS Lambda - Computacion sin servidores"""
    
    def __init__(self):
        self.funciones = []
        self._crear_funciones_iniciales()
    
    def _crear_funciones_iniciales(self):
        """Crear funciones Lambda de ejemplo"""
        self.funciones = [
            {
                'FunctionName': 'procesar-imagen',
                'Runtime': 'python3.9',
                'Handler': 'index.handler',
                'Role': 'arn:aws:iam::123456789012:role/lambda-role',
                'Timeout': 30,
                'MemorySize': 128,
                'State': 'Active',
                'LastModified': datetime(2024, 1, 10),
                'Description': 'Redimensiona imagenes subidas a S3'
            },
            {
                'FunctionName': 'enviar-email',
                'Runtime': 'nodejs18.x',
                'Handler': 'index.handler',
                'Role': 'arn:aws:iam::123456789012:role/lambda-role',
                'Timeout': 10,
                'MemorySize': 256,
                'State': 'Active',
                'LastModified': datetime(2024, 2, 15),
                'Description': 'Envia emails de bienvenida'
            }
        ]
    
    def listar_funciones(self):
        """Listar todas las funciones Lambda"""
        print("\n" + "="*60)
        print("FUNCIONES LAMBDA")
        print("="*60)
        for func in self.funciones:
            print(f"\n  Funcion: {func['FunctionName']}")
            print(f"    Runtime: {func['Runtime']}")
            print(f"    Handler: {func['Handler']}")
            print(f"    Timeout: {func['Timeout']}s")
            print(f"    Memoria: {func['MemorySize']} MB")
            print(f"    Estado: {func['State']}")
            print(f"    Descripcion: {func['Description']}")
    
    def invocar_funcion(self, nombre_funcion: str, payload: Dict):
        """Simular invocacion de una funcion Lambda"""
        print(f"\n[INVOCANDO] Lambda: {nombre_funcion}")
        print(f"[PAYLOAD] {json.dumps(payload, indent=2)}")
        
        # Simular respuesta basada en la funcion
        respuestas = {
            'procesar-imagen': {
                'statusCode': 200,
                'body': {'mensaje': 'Imagen procesada', 'tamano_original': '2MB', 'tamano_final': '500KB'}
            },
            'enviar-email': {
                'statusCode': 200,
                'body': {'mensaje': 'Email enviado', 'destinatario': payload.get('email', 'N/A')}
            }
        }
        
        respuesta = respuestas.get(nombre_funcion, {
            'statusCode': 200,
            'body': {'mensaje': 'Funcion ejecutada exitosamente'}
        })
        
        print(f"[RESPUESTA] Status: {respuesta['statusCode']}")
        print(f"[RESPUESTA] Body: {json.dumps(respuesta['body'], indent=2)}")
        return respuesta
    
    def crear_funcion(self, nombre: str, runtime: str, descripcion: str):
        """Simular creacion de una funcion Lambda"""
        print(f"\n[CREANDO] Funcion Lambda: {nombre}")
        nueva_funcion = {
            'FunctionName': nombre,
            'Runtime': runtime,
            'Handler': 'index.handler',
            'Role': 'arn:aws:iam::123456789012:role/lambda-role',
            'Timeout': 30,
            'MemorySize': 128,
            'State': 'Active',
            'LastModified': datetime.now(),
            'Description': descripcion
        }
        self.funciones.append(nueva_funcion)
        print(f"[OK] Funcion '{nombre}' creada exitosamente")
        return nueva_funcion


class DynamoDBSimulador:
    """Simulador de Amazon DynamoDB - Base de datos NoSQL"""
    
    def __init__(self):
        self.tablas = {}
        self._crear_tablas_iniciales()
    
    def _crear_tablas_iniciales(self):
        """Crear tablas de ejemplo"""
        # Tabla de usuarios
        self.tablas['usuarios'] = {
            'TableName': 'usuarios',
            'KeySchema': [{'AttributeName': 'user_id', 'KeyType': 'HASH'}],
            'AttributeDefinitions': [{'AttributeName': 'user_id', 'AttributeType': 'S'}],
            'BillingMode': 'PAY_PER_REQUEST',
            'ItemCount': 15420,
            'Items': [
                {'user_id': 'U001', 'nombre': 'Ana', 'email': 'ana@ejemplo.com', 'edad': 28},
                {'user_id': 'U002', 'nombre': 'Carlos', 'email': 'carlos@ejemplo.com', 'edad': 35},
                {'user_id': 'U003', 'nombre': 'Diana', 'email': 'diana@ejemplo.com', 'edad': 31}
            ]
        }
        
        # Tabla de productos
        self.tablas['productos'] = {
            'TableName': 'productos',
            'KeySchema': [{'AttributeName': 'producto_id', 'KeyType': 'HASH'}],
            'AttributeDefinitions': [{'AttributeName': 'producto_id', 'AttributeType': 'S'}],
            'BillingMode': 'PROVISIONED',
            'ItemCount': 856,
            'Items': [
                {'producto_id': 'P001', 'nombre': 'Laptop', 'precio': 999.99, 'stock': 50},
                {'producto_id': 'P002', 'nombre': 'Mouse', 'precio': 29.99, 'stock': 200},
                {'producto_id': 'P003', 'nombre': 'Teclado', 'precio': 49.99, 'stock': 150}
            ]
        }
    
    def listar_tablas(self):
        """Listar todas las tablas"""
        print("\n" + "="*60)
        print("TABLAS DYNAMODB")
        print("="*60)
        for nombre, tabla in self.tablas.items():
            print(f"\n  Tabla: {tabla['TableName']}")
            print(f"    Items: {tabla['ItemCount']}")
            print(f"    Billing: {tabla['BillingMode']}")
            print(f"    Primary Key: {tabla['KeySchema'][0]['AttributeName']}")
    
    def consultar_items(self, nombre_tabla: str, limite: int = 5):
        """Consultar items de una tabla"""
        print(f"\n[CONSULTA] Tabla: {nombre_tabla}")
        if nombre_tabla in self.tablas:
            tabla = self.tablas[nombre_tabla]
            items = tabla['Items'][:limite]
            print(f"  Items encontrados: {len(items)}")
            for i, item in enumerate(items, 1):
                print(f"\n  Item {i}:")
                for key, value in item.items():
                    print(f"    {key}: {value}")
            return items
        else:
            print(f"  [ERROR] Tabla '{nombre_tabla}' no existe")
            return []
    
    def insertar_item(self, nombre_tabla: str, item: Dict):
        """Insertar un item en una tabla"""
        print(f"\n[INSERTANDO] Item en tabla: {nombre_tabla}")
        if nombre_tabla in self.tablas:
            self.tablas[nombre_tabla]['Items'].append(item)
            self.tablas[nombre_tabla]['ItemCount'] += 1
            print(f"  [OK] Item insertado: {json.dumps(item, indent=4)}")
            return item
        else:
            print(f"  [ERROR] Tabla '{nombre_tabla}' no existe")
            return None
    
    def crear_tabla(self, nombre: str, primary_key: str):
        """Simular creacion de una tabla DynamoDB"""
        print(f"\n[CREANDO] Tabla DynamoDB: {nombre}")
        nueva_tabla = {
            'TableName': nombre,
            'KeySchema': [{'AttributeName': primary_key, 'KeyType': 'HASH'}],
            'AttributeDefinitions': [{'AttributeName': primary_key, 'AttributeType': 'S'}],
            'BillingMode': 'PAY_PER_REQUEST',
            'ItemCount': 0,
            'Items': []
        }
        self.tablas[nombre] = nueva_tabla
        print(f"  [OK] Tabla '{nombre}' creada exitosamente")
        return nueva_tabla


class APIGatewaySimulador:
    """Simulador de API Gateway - Creacion de APIs REST"""
    
    def __init__(self):
        self.apis = []
        self.recursos = {}
        self._crear_api_inicial()
    
    def _crear_api_inicial(self):
        """Crear API de ejemplo"""
        self.apis = [
            {
                'apiId': 'api123',
                'name': 'API de Productos',
                'description': 'API REST para gestionar productos',
                'endpoint': 'https://api123.execute-api.us-east-1.amazonaws.com',
                'stage': 'prod',
                'createdDate': datetime(2024, 1, 20)
            }
        ]
        
        # Recursos de la API
        self.recursos = {
            'api123': {
                '/products': {
                    'GET': 'Listar productos',
                    'POST': 'Crear producto'
                },
                '/products/{id}': {
                    'GET': 'Obtener producto',
                    'PUT': 'Actualizar producto',
                    'DELETE': 'Eliminar producto'
                }
            }
        }
    
    def listar_apis(self):
        """Listar todas las APIs"""
        print("\n" + "="*60)
        print("APIS API GATEWAY")
        print("="*60)
        for api in self.apis:
            print(f"\n  API: {api['name']}")
            print(f"    ID: {api['apiId']}")
            print(f"    Endpoint: {api['endpoint']}")
            print(f"    Stage: {api['stage']}")
            print(f"    Descripcion: {api['description']}")
    
    def mostrar_recursos(self, api_id: str):
        """Mostrar los recursos de una API"""
        print(f"\n[RECURSOS] API: {api_id}")
        if api_id in self.recursos:
            for path, metodos in self.recursos[api_id].items():
                print(f"\n  Path: {path}")
                for metodo, descripcion in metodos.items():
                    print(f"    {metodo}: {descripcion}")
        else:
            print(f"  [ERROR] API '{api_id}' no existe")
    
    def crear_api(self, nombre: str, descripcion: str):
        """Simular creacion de una API"""
        print(f"\n[CREANDO] API Gateway: {nombre}")
        api_id = 'api' + str(len(self.apis) + 456)
        nueva_api = {
            'apiId': api_id,
            'name': nombre,
            'description': descripcion,
            'endpoint': f'https://{api_id}.execute-api.us-east-1.amazonaws.com',
            'stage': 'dev',
            'createdDate': datetime.now()
        }
        self.apis.append(nueva_api)
        self.recursos[api_id] = {}
        print(f"  [OK] API '{nombre}' creada exitosamente")
        print(f"  Endpoint: {nueva_api['endpoint']}")
        return nueva_api
    
    def agregar_recurso(self, api_id: str, path: str, metodo: str, lambda_func: str):
        """Agregar un recurso a una API"""
        print(f"\n[CONFIGURANDO] Recurso: {metodo} {path}")
        if api_id in self.recursos:
            if path not in self.recursos[api_id]:
                self.recursos[api_id][path] = {}
            self.recursos[api_id][path][metodo] = f'Integrado con: {lambda_func}'
            print(f"  [OK] Recurso configurado")
            print(f"    Path: {path}")
            print(f"    Metodo: {metodo}")
            print(f"    Integracion: Lambda '{lambda_func}'")
        else:
            print(f"  [ERROR] API '{api_id}' no existe")


class RDSSimulador:
    """Simulador de Amazon RDS - Bases de datos relacionales"""
    
    def __init__(self):
        self.instancias = []
        self._crear_instancias_iniciales()
    
    def _crear_instancias_iniciales(self):
        """Crear instancias RDS de ejemplo"""
        self.instancias = [
            {
                'DBInstanceIdentifier': 'mi-base-datos-1',
                'Engine': 'postgres',
                'EngineVersion': '14.7',
                'DBInstanceClass': 'db.t3.micro',
                'AllocatedStorage': 20,
                'Endpoint': 'mi-base-datos-1.abc123.us-east-1.rds.amazonaws.com',
                'Port': 5432,
                'Status': 'available',
                'MultiAZ': False,
                'StorageEncrypted': True,
                'BackupRetentionPeriod': 7
            },
            {
                'DBInstanceIdentifier': 'base-produccion',
                'Engine': 'mysql',
                'EngineVersion': '8.0.35',
                'DBInstanceClass': 'db.r5.large',
                'AllocatedStorage': 100,
                'Endpoint': 'base-produccion.def456.us-east-1.rds.amazonaws.com',
                'Port': 3306,
                'Status': 'available',
                'MultiAZ': True,
                'StorageEncrypted': True,
                'BackupRetentionPeriod': 30
            }
        ]
    
    def listar_instancias(self):
        """Listar todas las instancias RDS"""
        print("\n" + "="*60)
        print("INSTANCIAS RDS")
        print("="*60)
        for db in self.instancias:
            print(f"\n  Instancia: {db['DBInstanceIdentifier']}")
            print(f"    Motor: {db['Engine']} {db['EngineVersion']}")
            print(f"    Clase: {db['DBInstanceClass']}")
            print(f"    Almacenamiento: {db['AllocatedStorage']} GB")
            print(f"    Endpoint: {db['Endpoint']}:{db['Port']}")
            print(f"    Estado: {db['Status']}")
            print(f"    Multi-AZ: {db['MultiAZ']}")
            print(f"    Encriptado: {db['StorageEncrypted']}")
    
    def crear_instancia(self, identificador: str, motor: str, clase: str, almacenamiento: int):
        """Simular creacion de una instancia RDS"""
        print(f"\n[CREANDO] Instancia RDS: {identificador}")
        print(f"  Motor: {motor}")
        print(f"  Clase: {clase}")
        print(f"  Almacenamiento: {almacenamiento} GB")
        print("  [PROCESO] Esto puede tardar varios minutos...")
        
        nueva_instancia = {
            'DBInstanceIdentifier': identificador,
            'Engine': motor,
            'EngineVersion': self._obtener_version(motor),
            'DBInstanceClass': clase,
            'AllocatedStorage': almacenamiento,
            'Endpoint': f'{identificador}.xyz789.us-east-1.rds.amazonaws.com',
            'Port': self._obtener_puerto(motor),
            'Status': 'available',
            'MultiAZ': False,
            'StorageEncrypted': True,
            'BackupRetentionPeriod': 7
        }
        
        self.instancias.append(nueva_instancia)
        print(f"  [OK] Instancia '{identificador}' creada exitosamente")
        print(f"  Endpoint: {nueva_instancia['Endpoint']}")
        return nueva_instancia
    
    def _obtener_version(self, motor: str) -> str:
        """Obtener version por defecto segun motor"""
        versiones = {
            'postgres': '14.7',
            'mysql': '8.0.35',
            'mariadb': '10.11.3',
            'oracle': '19c',
            'sqlserver': '15.00'
        }
        return versiones.get(motor, 'latest')
    
    def _obtener_puerto(self, motor: str) -> int:
        """Obtener puerto por defecto segun motor"""
        puertos = {
            'postgres': 5432,
            'mysql': 3306,
            'mariadb': 3306,
            'oracle': 1521,
            'sqlserver': 1433
        }
        return puertos.get(motor, 5432)


class Fase2Desarrollo:
    """Clase principal para la Fase 2"""
    
    def __init__(self):
        self.lambda_sim = AWSLambdaSimulador()
        self.dynamodb_sim = DynamoDBSimulador()
        self.api_gateway = APIGatewaySimulador()
        self.rds_sim = RDSSimulador()
    
    def ejecutar_demo_completa(self):
        """Ejecutar demostracion completa de la Fase 2"""
        print("="*70)
        print("AWS FASE 2: DESARROLLO Y BASES DE DATOS")
        print("Servicios: Lambda, API Gateway, DynamoDB, RDS")
        print("="*70)
        
        # 1. Lambda Functions
        print("\n" + "#"*70)
        print("# 1. AWS LAMBDA - Computacion sin servidores")
        print("#"*70)
        self.lambda_sim.listar_funciones()
        
        # Invocar una funcion
        print("\n--- Invocacion de funciones ---")
        self.lambda_sim.invocar_funcion('procesar-imagen', {
            'bucket': 'mi-bucket',
            'key': 'foto.jpg'
        })
        
        # Crear nueva funcion
        self.lambda_sim.crear_funcion(
            'procesar-pago',
            'python3.9',
            'Procesa pagos con tarjeta de credito'
        )
        
        # 2. DynamoDB
        print("\n" + "#"*70)
        print("# 2. DYNAMODB - Base de datos NoSQL")
        print("#"*70)
        self.dynamodb_sim.listar_tablas()
        
        # Consultar items
        print("\n--- Consultar datos ---")
        self.dynamodb_sim.consultar_items('usuarios', limite=3)
        
        # Insertar nuevo item
        print("\n--- Insertar nuevo item ---")
        self.dynamodb_sim.insertar_item('usuarios', {
            'user_id': 'U004',
            'nombre': 'Elena',
            'email': 'elena@ejemplo.com',
            'edad': 27
        })
        
        # 3. API Gateway
        print("\n" + "#"*70)
        print("# 3. API GATEWAY - Creacion de APIs REST")
        print("#"*70)
        self.api_gateway.listar_apis()
        
        # Mostrar recursos
        self.api_gateway.mostrar_recursos('api123')
        
        # Crear nueva API
        print("\n--- Crear nueva API ---")
        nueva_api = self.api_gateway.crear_api(
            'API de Usuarios',
            'API REST para gestionar usuarios'
        )
        
        # Agregar recursos
        self.api_gateway.agregar_recurso(
            nueva_api['apiId'],
            '/usuarios',
            'GET',
            'procesar-usuarios'
        )
        
        # 4. RDS
        print("\n" + "#"*70)
        print("# 4. RDS - Bases de datos relacionales")
        print("#"*70)
        self.rds_sim.listar_instancias()
        
        # Crear nueva instancia
        print("\n--- Crear nueva instancia RDS ---")
        self.rds_sim.crear_instancia(
            'base-desarrollo',
            'postgres',
            'db.t3.small',
            50
        )
        
        # Resumen Arquitectura Serverless
        print("\n" + "="*70)
        print("ARQUITECTURA SERVERLESS COMPLETA")
        print("="*70)
        print("""
        Cliente Web/Movil
            |
            v
        API Gateway (API REST)
            |
            v
        AWS Lambda (Logica de negocio)
            |
            +---> DynamoDB (Datos NoSQL)
            |--> RDS (Datos relacionales)
            |--> S3 (Almacenamiento)
        
        Beneficios:
        - Escalabilidad automatica
        - Pago por uso (sin servidores que mantener)
        - Alta disponibilidad
        - Despliegue rapido
        """)
        
        print("="*70)
        print("Fase 2 completada exitosamente!")
        print("="*70)
def main():
    """Funcion principal"""
    print("\n" + "="*70)
    print("SIMULADOR AWS - FASE 2 (Desarrollo y Bases de Datos)")
    print("="*70)
    
    demo = Fase2Desarrollo()
    demo.ejecutar_demo_completa()
    
    # Ejemplos de creacion rapida
    print("\n" + "="*70)
    print("EJEMPLOS DE CREACION DE RECURSOS")
    print("="*70)
    
    print("\n[EJEMPLO 1] Crear funcion Lambda")
    demo.lambda_sim.crear_funcion('procesar-archivo', 'python3.9', 'Procesa archivos subidos')
    
    print("\n[EJEMPLO 2] Crear tabla DynamoDB")
    demo.dynamodb_sim.crear_tabla('ordenes', 'orden_id')
    
    print("\n[EJEMPLO 3] Crear API Gateway")
    demo.api_gateway.crear_api('API de Ordenes', 'API para gestionar ordenes de compra')
    
    print("\n[EJEMPLO 4] Crear instancia RDS")
    demo.rds_sim.crear_instancia('base-analisis', 'postgres', 'db.t3.small', 50)
    
    print("\n" + "="*70)
    print("¡Practica completada!")
    print("="*70)


if __name__ == "__main__":
    main()