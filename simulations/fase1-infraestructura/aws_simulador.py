#!/usr/bin/env python3
"""
Simulador de AWS - Para practicar sin cuenta real
Fase 1: Conceptos basicos simulados
"""

import json
from datetime import datetime


class AWSSimulador:
    """Simulador de servicios AWS para practicar"""
    
    def __init__(self, region='us-east-1'):
        self.region = region
        self.buckets_s3 = []
        self.instancias_ec2 = []
        self.usuarios_iam = []
        self.vpcs = []
        self._crear_datos_iniciales()
        print("[OK] Simulador AWS inicializado en region: " + region)
    
    def _crear_datos_iniciales(self):
        """Crear datos de ejemplo"""
        self.buckets_s3 = [
            {'Name': 'mi-primer-bucket-2026', 'CreationDate': datetime.now()},
            {'Name': 'backup-datos-importantes', 'CreationDate': datetime.now()}
        ]
        
        self.instancias_ec2 = [
            {
                'InstanceId': 'i-12345abcde',
                'InstanceType': 't2.micro',
                'State': {'Name': 'running'},
                'PrivateIpAddress': '10.0.0.5',
                'PublicIpAddress': '54.123.45.67'
            },
            {
                'InstanceId': 'i-67890fghij',
                'InstanceType': 't3.small',
                'State': {'Name': 'stopped'},
                'PrivateIpAddress': '10.0.0.10',
                'PublicIpAddress': None
            }
        ]
        
        self.usuarios_iam = [
            {
                'UserName': 'admin-user',
                'Arn': 'arn:aws:iam::123456789012:user/admin-user',
                'CreateDate': datetime(2024, 1, 15)
            },
            {
                'UserName': 'developer-user',
                'Arn': 'arn:aws:iam::123456789012:user/developer-user',
                'CreateDate': datetime(2024, 3, 20)
            }
        ]
        
        self.vpcs = [
            {
                'VpcId': 'vpc-12345abc',
                'CidrBlock': '10.0.0.0/16',
                'State': 'available'
            },
            {
                'VpcId': 'vpc-67890def',
                'CidrBlock': '172.31.0.0/16',
                'State': 'available'
            }
        ]
    
    def listar_buckets_s3(self):
        """Listar buckets S3 simulados"""
        print("\n" + "="*50)
        print("BUCKETS S3 (Simulados)")
        print("="*50)
        for bucket in self.buckets_s3:
            print("  * " + bucket['Name'] + " (creado: " + str(bucket['CreationDate'].date()) + ")")
    
    def listar_instancias_ec2(self):
        """Listar instancias EC2 simuladas"""
        print("\n" + "="*50)
        print("INSTANCIAS EC2 (Simuladas)")
        print("="*50)
        for i, instance in enumerate(self.instancias_ec2, 1):
            print("\n  Instancia " + str(i) + ":")
            print("    ID: " + instance['InstanceId'])
            print("    Tipo: " + instance['InstanceType'])
            print("    Estado: " + instance['State']['Name'])
            print("    IP Privada: " + str(instance.get('PrivateIpAddress', 'N/A')))
            print("    IP Publica: " + str(instance.get('PublicIpAddress', 'N/A')))
    
    def listar_usuarios_iam(self):
        """Listar usuarios IAM simulados"""
        print("\n" + "="*50)
        print("USUARIOS IAM (Simulados)")
        print("="*50)
        for user in self.usuarios_iam:
            print("  * " + user['UserName'])
            print("    ARN: " + user['Arn'])
            print("    Creado: " + str(user['CreateDate'].date()))
    
    def obtener_info_vpc(self):
        """Obtener informacion VPC simulada"""
        print("\n" + "="*50)
        print("VPCS (Simuladas)")
        print("="*50)
        for vpc in self.vpcs:
            print("  * VPC ID: " + vpc['VpcId'])
            print("    CIDR: " + vpc['CidrBlock'])
            print("    Estado: " + vpc['State'])
    
    def crear_bucket_s3(self, nombre_bucket):
        """Crear bucket S3 simulado"""
        print("\n[ACCION] Creando bucket S3: " + nombre_bucket)
        nuevo_bucket = {
            'Name': nombre_bucket,
            'CreationDate': datetime.now()
        }
        self.buckets_s3.append(nuevo_bucket)
        print("[OK] Bucket creado exitosamente")
    
    def lanzar_instancia_ec2(self, tipo_instancia='t2.micro'):
        """Lanzar instancia EC2 simulada"""
        print("\n[ACCION] Lanzando instancia EC2 tipo: " + tipo_instancia)
        nueva_instancia = {
            'InstanceId': 'i-' + ''.join([str(i) for i in range(5)]),
            'InstanceType': tipo_instancia,
            'State': {'Name': 'pending'},
            'PrivateIpAddress': '10.0.0.' + str(len(self.instancias_ec2) + 1),
            'PublicIpAddress': None
        }
        self.instancias_ec2.append(nueva_instancia)
        nueva_instancia['State']['Name'] = 'running'
        print("[OK] Instancia lanzada exitosamente")
        return nueva_instancia


def main():
    """Funcion principal"""
    print("AWS Fundamentos - Simulador de Servicios")
    print("(Practica sin necesidad de cuenta real)")
    print("="*50)
    
    # Inicializar el simulador
    aws = AWSSimulador(region='us-east-1')
    
    # Listar recursos existentes
    aws.listar_buckets_s3()
    aws.listar_instancias_ec2()
    aws.listar_usuarios_iam()
    aws.obtener_info_vpc()
    
    # Simular creacion de nuevos recursos
    print("\n" + "="*50)
    print("SIMULACION: Creando nuevos recursos")
    print("="*50)
    
    aws.crear_bucket_s3('nuevo-bucket-ejemplo')
    aws.lanzar_instancia_ec2('t3.medium')
    
    # Mostrar estado actualizado
    print("\n" + "="*50)
    print("ESTADO ACTUALIZADO")
    print("="*50)
    aws.listar_buckets_s3()
    aws.listar_instancias_ec2()
    
    print("\n" + "="*50)
    print("Practica completada")
    print("="*50)


if __name__ == "__main__":
    main()