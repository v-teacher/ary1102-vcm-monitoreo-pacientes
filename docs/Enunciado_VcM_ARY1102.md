# Sistema de Monitoreo Remoto de Pacientes Críticos

Iniciativa de Vinculación con el Medio · período 2026/02.

## Desafío

Una institución de salud necesita disminuir el tiempo entre una anomalía fisiológica
y su detección por el personal responsable. El escenario considera seguimiento
remoto de pacientes críticos/crónicos, trazabilidad, continuidad y crecimiento.
El desafío consiste en proponer y justificar una arquitectura que responda a esta necesidad.
Cada equipo define sus componentes, servicios, tecnologías y estrategia de implementación.
No se entrega una arquitectura de referencia ni un generador de eventos predefinido.
El prototipo y sus pruebas deben utilizar exclusivamente datos sintéticos; no constituye
una solución clínica ni un sistema productivo.

## Objetivos y actores

Vincula las decisiones con continuidad del seguimiento, detección oportuna,
trazabilidad, control de costos y crecimiento. Considera pacientes ficticios,
enfermería, médicos, TI, respuesta a urgencias y dirección como actores del diseño.
El MVP no atiende pacientes ni envía notificaciones a destinatarios reales.

## Requerimientos funcionales

Los códigos RF y RNF conservan su significado en el caso institucional.

| Requerimiento | Necesidad que la propuesta debe abordar |
|---|---|
| RF-01 Ingesta continua | Recepción de mediciones |
| RF-02 Clasificación | Estados Normal, Precaución y Crítico |
| RF-03 Detección de umbrales | Umbrales configurables por paciente |
| RF-04 Alertamiento | Comunicación de alertas a los roles responsables |
| RF-05 Consulta temporal | Consulta por paciente y período |
| RF-06 Historial de eventos y acciones | Trazabilidad de eventos y respuestas |
| RF-07 Perfiles de acceso | Acceso diferenciado según rol |
| RF-08 Cambios autorizados de umbrales | Configuración controlada y trazable |
| RF-09 Histórico | Conservación de mediciones para análisis |
| RF-10 Exportación | Exportación JSON/CSV |
| RF-11 Auditoría | Registro de accesos y acciones relevantes |

Cada equipo prioriza el alcance de su prototipo y justifica las decisiones.
Distinguir requisitos implementados, simulados y pendientes. Los umbrales usados
en pruebas son ficticios: no deben interpretarse como recomendaciones clínicas.

## Objetivos productivos y pruebas del MVP

| Condición del caso | Evidencia para validar la propuesta |
|---|---|
| RNF-01 Flujo crítico <1 s | Medir recepción → alerta; informar p50, p95, p99, errores y condiciones |
| RNF-02 Incremento del 200% en <30 s | Explicitar interpretación de la carga y medir respuesta/escalamiento; informar limitaciones |
| RNF-03 99,99% de disponibilidad | Diseño y pruebas de fallo/recuperación; una demo breve no acredita el SLA anual |
| RNF-04 TLS 1.2+, cifrado en reposo y MFA | Evidencias de controles aplicados y restricciones; HTTP local no acredita TLS |
| RNF-05 RPO <=5 min / RTO <=30 min | Diseñar respaldo/recuperación y ejecutar una prueba acotada cronometrada |
| RNF-06 Observabilidad | Logs, métricas y alerta técnica de prueba |
| RNF-07 Mantenibilidad | Separación de componentes y actualización del clasificador |
| RNF-08 Portabilidad | Contrato de eventos y exportación estándar |
| RNF-09 Costos | Estimación, medición de uso y propuesta de retención histórica |
| RNF-10 Protección de información | Minimización, acceso autorizado y datos sintéticos en todas las evidencias |

## Dimensionamiento de referencia

El caso plantea hasta 10.000 pacientes a un evento/s, 500 usuarios internos y
5–10 TB/mes. Estas cifras orientan el diseño; no son resultados acreditados por
este repositorio. Las pruebas del prototipo deben tener un alcance acotado,
presupuesto y cuotas verificados, sin afirmar capacidad productiva a partir de una demo.

## Propuesta de cada equipo

No se prescribe proveedor, servicios, topología, patrón de procesamiento ni herramienta.
Cada equipo debe explicar:

- Cómo interpreta el problema, los actores y las prioridades.
- Qué arquitectura propone, mediante un diagrama y el flujo de información.
- Cómo responde a los RF/RNF y qué compromisos o limitaciones acepta.
- Qué alternativas consideró y por qué eligió su propuesta.
- Cómo validará seguridad, rendimiento, continuidad, costos y utilidad.
- Qué tiene diseñado, implementado, probado o pendiente.

El mecanismo para obtener datos sintéticos y los escenarios de prueba también
forman parte de la propuesta del equipo.

## Hitos de vinculación



- **Hito 1:** docente presenta caso/elementos abordados dentro del plazo límite;
  priorizar próxima sesión disponible y registrar fecha/alcance efectivo.
- **Hito 2:** enviar avance a la empresa en la semana del lunes **19 de octubre
  de 2026 (19–25 de octubre)** y esperar su retroalimentación. El avance puede
  ser parcial: diseño, prioridades, estado real y preguntas.
- **Hito 3:** exposición de solución, resultados y cambios por feedback.
  Fecha y modalidad pendientes de confirmación institucional.

El docente coordina envío/contacto institucional; registrar la respuesta real e
incorporarla a la propuesta y la exposición. No se ha informado un plazo de respuesta empresarial.

## Restricciones

Solo datos ficticios/sintéticos: no incluir nombres, RUT, datos clínicos reales,
contactos, IP identificables ni accesos productivos en código, capturas o informes.
Si se utiliza un laboratorio cloud, verificar sus permisos, cuotas y presupuesto. No registrar contactos del socio
ni realizar acercamientos institucionales por cuenta del equipo.
HL7/FHIR, wearables reales, validación clínica y operación productiva quedan fuera
del MVP. Reportar explícitamente funciones faltantes y controles no implementados.

## Documentos de coordinación

Consultar [hitos](Hitos_VcM_2026.02.md) y [plantilla de avance](Plantilla_Avance_Hito2.md).
