# Validación local — 2026-10-09

Recurso docente para el Sistema de Monitoreo Remoto de Pacientes Críticos.

- Seis pruebas automatizadas aprobadas: clasificación, validación, persistencia/idempotencia, flujo HTTP, duplicados concurrentes y dataset sintético.
- Configuración Docker Compose y construcción de imagen verificadas; contenedor saludable.
- Envío HTTP de seis eventos sintéticos: dos Normal, dos Precaución y dos Crítico; seis eventos almacenados y dos alertas generadas.
- Reinicio del contenedor: se conservaron los seis eventos y las dos alertas.
- Se retiraron el contenedor, la red y el volumen temporal de prueba; el volumen contenía exclusivamente datos sintéticos descartables.

Estas comprobaciones son locales. No constituyen un despliegue AWS, prueba de carga, validación clínica ni acreditación de SLA, RPO o RTO. La aplicación es una base didáctica; las adaptaciones cloud, los controles por rol y la entrega de alertas deben desarrollarse y verificarse en las actividades.
