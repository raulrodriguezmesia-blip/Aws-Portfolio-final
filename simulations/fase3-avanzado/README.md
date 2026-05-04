# FASE 3 - Servicios Avanzados AWS

## Descripción

Esta fase implementa servicios avanzados de AWS para orquestación, mensajería y contenedores serverless.

## Servicios Implementados

### 1. Amazon SQS (Simple Queue Service)
- Colas FIFO para procesamiento ordenado
- Colas estándar para alto rendimiento
- Retardo de mensajes y visibilidad configurable
- Procesamiento asíncrono de tareas

### 2. Amazon SNS (Simple Notification Service)
- Publicación/suscripción de mensajes
- Multiples protocolos (Email, Lambda, HTTP/S)
- Fan-out pattern para distribución masiva
- Notificaciones en tiempo real

### 3. Amazon EventBridge
- Orquestación basada en eventos
- Patrones de coincidencia de eventos
- Rutas de eventos a múltiples destinos
- Arquitectura event-driven

### 4. Amazon ECS con Fargate
- Contenedores sin gestión de servidores
- Escalado automático de servicios
- Balanceo de carga integrado
- Aislamiento y seguridad por tarea

## Ejecución

```bash
# Ejecutar simulador completo
python simulations/fase3-avanzado/aws_fase3.py

# Ejecutar componentes individuales
python -c "from aws_fase3 import SQSSimulador; s = SQSSimulador(); s.crear_cola('test')"
python -c "from aws_fase3 import SNSSimulador; s = SNSSimulador(); s.crear_topic('notificaciones')"
python -c "from aws_fase3 import EventBridgeSimulador; e = EventBridgeSimulador(); e.crear_regla('procesar', {})"
python -c "from aws_fase3 import ECSFargateSimulador; e = ECSFargateSimulador(); e.crear_cluster('cluster')"
```

## Ejemplo de Uso

```python
from aws_fase3 import AWSSimuladorFase3

# Inicializar simulador completo
simulador = AWSSimuladorFase3()

# Ejecutar demostración completa
simulador.demo_completa()
```

## Casos de Uso

1. **Procesamiento asíncrono**: Colas SQS para tareas en segundo plano
2. **Notificaciones**: SNS para alertas y comunicaciones
3. **Orquestación**: EventBridge para flujos de trabajo complejos
4. **Microservicios**: ECS/Fargate para aplicaciones contenerizadas

## Próximos Pasos

- [ ] Integración con AWS Step Functions
- [ ] Implementar DLQ (Dead Letter Queues) en SQS
- [ ] Configurar CloudWatch Events
- [ ] Añadir ECS con servicios balanceados
- [ ] Implementar patrón Saga con SQS y EventBridge