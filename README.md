# Bank API

## Descripción
Esta es una API RESTful para un banco que permite a los usuarios crear cuentas bancarias y actualizar sus saldos.

## Arquitectura
- **Patrón Capas**: Controller (Routers) → Service → Repository
- **Base de Datos**: MongoDB con operaciones atómicas para actualización de saldos
- **Escalabilidad**: Diseño modular con inyección de dependencias

## Tecnologías Utilizadas
- **Python** con **FastAPI** para el backend
- **MongoDB** como base de datos
- **Docker** y **Docker Compose** para contenedorización
- **pytest y httpx** para pruebas unitarias

## Endpoints

### Crear una cuenta bancaria
- **Endpoint**: `POST /accounts`
- **Parámetros de entrada**:
```json
{
  "holder_name": "Juan Pérez",
  "balance": 1000.0
}
```
- **Respuesta**:
```json
{
  "account_id": "60a7c1d5f5a5f1234567890b"
}
```

### Actualizar saldo de una cuenta
- **Endpoint**: `PATCH /accounts/{account_id}`
- **Parámetros de entrada**:
```json
{
  "balance": 500.0
}
```
- **Respuesta**:
```json
{
  "updated_balance": 1500.0
}
```

### Listar todas las cuentas
- **Endpoint**: `GET /accounts`
- **Respuesta**:
```json
[
  {
    "account_id": "60a7c1d5f5a5f1234567890b",
    "holder_name": "Juan Pérez",
    "balance": 1500.0
  }
]
```

## Ejecución con Docker
```bash
docker-compose up --build
```

## Pruebas Unitarias
Para ejecutar las pruebas unitarias, usa:
```bash
pytest tests/
```

## Variables de Entorno
Crea un archivo `.env` con el siguiente contenido:
```plaintext
MONGODB_URL=mongodb://host.docker.internal:27017
MONGODB_DB_NAME=bank_db
MONGODB_COLLECTION_NAME=accounts
```

## Mejoras Implementadas
- Validaciones de entrada con **Pydantic**
- Manejo adecuado de errores con **HTTPException**
- Implementación de **tests unitarios** para endpoints
- Instrucciones detalladas en el **README**

---
© 2025 - Bank API

