# AWS Cloud Portfolio - Raul Rodriguez Mesia

[![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white)](https://www.java.com/)
[![Spring](https://img.shields.io/badge/spring-%236DB33F.svg?style=for-the-badge&logo=spring&logoColor=white)](https://spring.io/)

> **Portafolio de prácticas y proyectos en Amazon Web Services (AWS)**

## 📄 Sobre el Proyecto

Este repositorio contiene mi portafolio de prácticas y proyectos en **Amazon Web Services (AWS)**, demostrando habilidades en:

- 🏗️ **Infraestructura Cloud** (EC2, S3, IAM, VPC)
- ⚡ **Arquitectura Serverless** (Lambda, DynamoDB, API Gateway, RDS)
- 🔄 **Servicios Avanzados** (SQS, SNS, EventBridge, ECS/Fargate)
- 🌐 **Despliegue Web** (Sitios estáticos en S3)

## 🎯 Demo en Vivo

### 🌐 CV Desplegado en AWS S3

**URL:** [http://cv-raul-rodriguez-mesa-2026.s3-website-us-east-1.amazonaws.com](http://cv-raul-rodriguez-mesa-2026.s3-website-us-east-1.amazonaws.com)

![CV Preview](cv/preview.png)

> **Estado:** ✅ En Producción  
> **Disponibilidad:** 99.99%  
> **Costo:** ~$0.03/mes

---

## 📂 Estructura del Repositorio

```
aws-portfolio/
├── README.md                    # Este archivo
├── cv/
│   ├── index.html              # CV profesional (HTML/CSS)
│   └── preview.png             # Captura de pantalla
├── simulations/
│   ├── fase1-infraestructura/
│   │   └── aws_simulador.py   # EC2, S3, IAM, VPC
│   ├── fase2-serverless/
│   │   └── aws_fase2.py       # Lambda, DynamoDB, API Gateway, RDS
│   └── fase3-avanzado/
│       └── aws_fase3.py       # SQS, SNS, EventBridge, ECS/Fargate
├── projects/
│   └── cv-deployed/
│       ├── deploy.sh          # Script de despliegue
│       └── index.html         # Código fuente del CV
├── scripts/
│   └── deploy.sh              # Automatización de despliegue
└── docs/
    ├── 01-guia-aws.md         # Guía de aprendizaje
    ├── 02-arquitecturas.md    # Diagramas y arquitecturas
    └── 03-referencias.md      # Recursos útiles
```

---

## 🚀 Tecnologías Utilizadas

### Cloud & DevOps
- **Amazon Web Services (AWS)** - Plataforma Cloud
- **Amazon S3** - Almacenamiento y Web Hosting
- **Amazon EC2** - Computación en la nube
- **Amazon Lambda** - Computación serverless
- **Amazon DynamoDB** - Base de datos NoSQL
- **Amazon RDS** - Base de datos relacional
- **Amazon API Gateway** - Gestión de APIs REST
- **Docker** - Contenedorización

### Backend & Lenguajes
- **Java 11+** - Lenguaje principal (Experto)
- **Spring Boot** - Microservicios
- **Python 3.12** - Scripting y automatización
- **Node.js** - APIs RESTful

### Bases de Datos
- **MySQL / PostgreSQL** - SQL
- **DynamoDB** - NoSQL
- **Oracle** - Sistemas empresariales

### Herramientas
- **Git / GitHub** - Control de versiones
- **Maven / Gradle** - Gestión de dependencias
- **IntelliJ IDEA / Eclipse** - IDEs
- **Postman / Swagger** - Testing de APIs

---

## 🎓 Simuladores AWS

### FASE 1 - Infraestructura Básica

```bash
python simulations/fase1-infraestructura/aws_simulador.py
```

**Servicios simulados:**
- ✅ Amazon EC2 - Instancias virtuales
- ✅ Amazon S3 - Almacenamiento de objetos
- ✅ AWS IAM - Seguridad y acceso
- ✅ Amazon VPC - Redes virtuales

**Ejemplo de uso:**
```python
# Listar instancias EC2
instancias = simulador.listar_instancias_ec2()
for inst in instancias:
    print(f"ID: {inst['InstanceId']}, Estado: {inst['State']['Name']}")
```

---

### FASE 2 - Arquitectura Serverless

```bash
python simulations/fase2-serverless/aws_fase2.py
```

**Servicios simulados:**
- ✅ AWS Lambda - Funciones sin servidor
- ✅ Amazon DynamoDB - Base de datos NoSQL
- ✅ API Gateway - APIs REST
- ✅ Amazon RDS - Bases de datos relacionales

**Ejemplo de uso:**
```python
# Invocar función Lambda
respuesta = lambda_sim.invocar_funcion('procesar-imagen', {
    'bucket': 'mi-bucket',
    'key': 'foto.jpg'
})
print(f"Estado: {respuesta['statusCode']}")
```

---

### FASE 3 - Servicios Avanzados

```bash
python simulations/fase3-avanzado/aws_fase3.py
```

**Servicios simulados:**
- ✅ Amazon SQS - Colas de mensajes
- ✅ Amazon SNS - Notificaciones
- ✅ EventBridge - Orquestación de eventos
- ✅ ECS/Fargate - Contenedores

**Ejemplo de uso:**
```python
# Enviar mensaje a cola SQS
sqs.enviar_mensaje('pedidos', {
    'pedido_id': 'PED001',
    'total': 150.00
})
```

---

## 💼 Proyectos Destacados

### 🥇 Sistema Alcaldía - Gestión de Empleados
- **Tecnologías:** Java, JDBC, MySQL, Eclipse IDE
- **Características:** 
  - Control de acceso con JWT/OAuth 2.0
  - Sistema de Backup automatizado
  - Encriptación SHA-256 / BCrypt
- **Estado:** ✅ Completado

### 🥈 Spring Boot API REST (Microservicios)
- **Tecnologías:** Java, Spring Boot, Maven, Swagger
- **Características:**
  - APIs REST escalables
  - Validación y manejo de excepciones
  - Documentación Swagger/OpenAPI 3.0
- **Estado:** ✅ Completado

### 🥉 Ferretería JPA-Hibernate
- **Tecnologías:** Java, JPA, Hibernate, MySQL
- **Características:**
  - Gestión de inventario completa
  - Consultas optimizadas (HQL, Criteria API)
  - Patrón DAO y control de transacciones
- **Estado:** ✅ Completado

### 🌟 CV Desplegado en AWS S3
- **Tecnologías:** HTML5, CSS3, AWS S3, CloudFront
- **URL:** [Ver en Producción](http://cv-raul-rodriguez-mesa-2026.s3-website-us-east-1.amazonaws.com)
- **Estado:** ✅ En Producción

---

## 📊 Experiencia Profesional

### AREQUIPA EXPRESO MARVISUR EIRL | Perú
**Cargo:** Soporte Operativo y Logística (Enfoque Técnico)  
**Periodo:** 2020 - 2025 (5 años)

**Tecnologías:** Java, MySQL, Sistemas aduaneros/financieros

**Responsabilidades:**
- Mantenimiento y evolución del sistema MARVICOM (Java/MySQL)
- Resolución de incidencias críticas con enfoque colaborativo
- Análisis de flujos logísticos y sistemas aduaneros/financieros
- Optimización de procesos operativos mediante lógica computacional
- Atención a 100+ usuarios internos en equipos multidisciplinarios

---

## 🎓 Formación Académica

### Ingeniero en Informática
**Institución:** Instituto Universitario de Tecnología de Los Llanos (IUTLL)  
**Año:** 2017  
**País:** Venezuela 🇻🇪

**Formación integral en:**
- Ingeniería de software
- Bases de datos avanzadas
- Estructuras de datos y algoritmos
- Arquitectura de computadoras
- Sistemas operativos

---

## 📚 Certificaciones (En Progreso)

| Certificación | Estado | Proveedor |
|--------------|--------|-----------|
| AWS Certified Cloud Practitioner | 🔄 En curso | Amazon Web Services |
| Oracle Certified Associate, Java SE | 🔄 En curso | Oracle |

---

## 🌍 Modalidades de Trabajo

- ✅ **Remoto:** 100% disponible
- ✅ **Nearshore:** Perú-España
- ✅ **Presencial:** Disponible
- 🚀 **Inicio:** Inmediato

---

## 🚀 Despliegue del Proyecto

### Requisitos Previos
- Python 3.9+
- AWS CLI configurada
- Git

### Pasos para Desplegar

1. **Clonar repositorio:**
```bash
git clone https://github.com/TU_USUARIO/aws-portfolio.git
cd aws-portfolio
```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

3. **Ejecutar simuladores:**
```bash
# FASE 1
python simulations/fase1-infraestructura/aws_simulador.py

# FASE 2
python simulations/fase2-serverless/aws_fase2.py

# FASE 3
python simulations/fase3-avanzado/aws_fase3.py
```

4. **Ver CV localmente:**
```bash
python -m http.server 8000 --directory cv
# Abrir: http://localhost:8000
```

---

## 🔗 Recursos Adicionales

- **Documentación AWS:** https://docs.aws.amazon.com/
- **AWS Well-Architected:** https://aws.amazon.com/architecture/well-architected/
- **Certificaciones AWS:** https://aws.amazon.com/certification/

---

## 📞 Contacto

**Raul Rodriguez Mesia**  
📧 raulrodriguezmesia@gmail.com  
📱 +51 966 105 289 | +51 920 157 695  
🔗 [GitHub](https://github.com/raulrodriguezmesia-blip) | [LinkedIn](https://www.linkedin.com/in/raul-rodriguez-mesia/)  
🌐 [CV Web](http://cv-raul-rodriguez-mesa-2026.s3-website-us-east-1.amazonaws.com)

---

## 💡 Notas

- Este portafolio demuestra habilidades prácticas en AWS
- Los simuladores permiten experimentar sin costos
- El CV está desplegado en producción en AWS S3
- Proyectos reales documentados y funcionales

---

<div align="center">
  <strong>Desarrollado con 💻 y ☕ | Desplegado en 🚀 AWS</strong>
</div>

<div align="center">
  <sub>Última actualización: 3 de mayo de 2026</sub>
</div>
