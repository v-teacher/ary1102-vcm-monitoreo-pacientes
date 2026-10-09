# Sistema de Monitoreo Remoto de Pacientes Críticos

ARY1102 · Arquitectura Cloud · VcM · período 2026/02.

## Desafío

Una institución de salud necesita disminuir el tiempo entre una anomalía fisiológica
y su detección por el personal responsable. El escenario considera seguimiento
remoto de pacientes críticos/crónicos, trazabilidad, continuidad y crecimiento.
Tu trabajo consiste en diseñar, implementar y evaluar una arquitectura cloud para
un MVP académico que recibe telemetría sintética, clasifica eventos y presenta
alertas simuladas. Las reglas de prueba no son criterios clínicos.

El proyecto se incorpora desde EA2. EA1 y su evaluación con FreshBox permanecen
como antecedente de aprendizaje; no se solicita repetir ni recalificar EP1.

## Objetivos y actores

Vincula las decisiones con continuidad del seguimiento, detección oportuna,
trazabilidad, control de costos y crecimiento. Considera pacientes ficticios,
enfermería, médicos, TI, respuesta a urgencias y dirección como actores del diseño.
El MVP no atiende pacientes ni envía notificaciones a destinatarios reales.

## Requerimientos y etapas

Los códigos RF y RNF conservan su significado en el caso institucional.

| Requerimiento | Trabajo académico |
|---|---|
| RF-01 Ingesta continua | Simulador y recepción de eventos; EA2 y EA3 |
| RF-02 Clasificación / RF-03 Detección de umbrales | Reglas sintéticas Normal, Precaución y Crítico; prueba de fronteras |
| RF-04 Alertamiento | Alerta simulada visible en EA2; entrega a canal de prueba y reintentos en EA3 |
| RF-05 Consulta temporal | Consulta por paciente ficticio y ventana temporal |
| RF-06 Historial de eventos y acciones | Eventos en EA2; acciones/acuse ficticio y trazabilidad en EA3 |
| RF-07 Perfiles de acceso | Diseño desde EA2; demostrar autorización de dos roles en EA3 |
| RF-08 Cambios de umbrales autorizados | Diseñar en EA2; implementar configuración autorizada/versionada en EA3 |
| RF-09 Histórico | Persistencia compartida en EA2; retención/ciclo de vida en EA3 |
| RF-10 Exportación | JSON/CSV sintético con filtros y límites |
| RF-11 Auditoría | Diseñar en EA2; registrar acciones y accesos relevantes en EA3 sin secretos |

La base entregada implementa solo parte del flujo. Declara en una matriz qué
requerimientos están implementados, simulados, pendientes o limitados por el laboratorio.
No equipares un token compartido con perfiles diferenciados o MFA.

## Objetivos productivos y pruebas del MVP

| Condición del caso | Evidencia académica requerida |
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

Diseña para la referencia de hasta 10.000 pacientes a un evento/s, 500 usuarios
internos y 5–10 TB/mes. El PDF menciona hasta 1.000 eventos/s en una PoC, pero no
entrega evidencias de esa prueba. No se considera un resultado ya demostrado ni
se exige reproducirlo con el generador secuencial básico. Antes de una prueba de
carga ampliada, acuerda el alcance con el docente y revisa presupuesto/cuotas.

## Entregables progresivos

1. **EA2:** comparación de alternativas, diagrama editable, decisiones, implementación
   con orquestación y almacenamiento administrado, pruebas y matriz RF/RNF.
2. **EA3:** evaluación de evolución serverless, diagrama, funciones/APIs/almacenamiento,
   procesamiento desacoplado, pruebas de duplicados, errores, autorización y costos.
3. **EFT:** solución integral que articula infraestructura base, contenedores,
   PaaS y serverless; informe, repositorio, pruebas y defensa individual.

Documenta el paso desde la arquitectura base al caso nuevo. El código docente no
sustituye tu implementación ni acredita automáticamente el logro de los indicadores.

## Hitos de vinculación

- **Hito 1:** docente presenta caso/elementos abordados dentro del plazo límite;
  priorizar próxima sesión disponible y registrar fecha/alcance efectivo.
- **Hito 2:** enviar avance a la empresa en la semana del lunes **19 de octubre
  de 2026 (19–25 de octubre)** y esperar su retroalimentación. El avance puede
  ser parcial: diseño, prioridades, estado real y preguntas.
- **Hito 3:** exposición de solución, resultados y cambios por feedback.
  Fecha y modalidad pendientes de confirmación institucional.

El docente coordina envío/contacto institucional; registrar la respuesta real e
incorporarla a EA3 y la exposición. No se ha informado un plazo de respuesta empresarial.

## Trabajo y evaluación

Se permite colaborar en el análisis y la organización del proyecto VcM. Cada
estudiante entrega y defiende evidencias propias para las evaluaciones individuales.
Se mantienen las ponderaciones institucionales: EP1 40%, EP2 30%, EP3 30% del
proceso; proceso 60% y EFT 40% de la nota final. Este proyecto no añade una nota.
Los instrumentos institucionales y los enunciados comunicados por el docente
establecen la evaluación; este documento no crea una rúbrica ni fechas nuevas.

Conserva código, comandos reproducibles, versión/commit evaluado y evidencias
sin credenciales. Los repositorios del curso se trabajan bajo `repos/ary1102` y
los nuevos repositorios GitHub del curso pertenecen a `v-teacher`.

## Restricciones

Solo datos ficticios/sintéticos: no incluir nombres, RUT, datos clínicos reales,
contactos, IP identificables ni accesos productivos en código, capturas o informes.
Usar AWS Academy Learner Lab para el MVP cloud. No registrar contactos del socio
ni realizar acercamientos institucionales por cuenta del equipo.
HL7/FHIR, wearables reales, validación clínica y operación productiva quedan fuera
del MVP. Reportar explícitamente funciones faltantes y controles no implementados.

## Aplicación inicial

Consultar [README de la aplicación](../README.md).
Incluye API, simulador Python, dataset ficticio, clasificación artificial, historial,
exportación y panel de alertas simuladas. SQLite sirve para una réplica local;
debe sustituirse al evolucionar hacia múltiples réplicas y persistencia administrada.
