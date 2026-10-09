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
La prueba de concepto no atiende pacientes ni envía notificaciones a destinatarios reales.

## Alcance de la contribución

El resultado esperado es una **propuesta de arquitectura cloud con una prueba de
concepto de infraestructura**. No se solicita desarrollar una aplicación clínica completa.

Dentro del alcance:

- Comparar y justificar alternativas de arquitectura y servicios cloud.
- Elaborar diagramas y explicar componentes, flujos e interfaces.
- Diseñar seguridad, disponibilidad, escalabilidad, respaldo, observabilidad y costos.
- Desplegar un subconjunto coherente de infraestructura, documentando su configuración.
- Ejecutar pruebas técnicas acotadas y reproducibles con entradas sintéticas.

Fuera del alcance obligatorio:

- Interfaces completas y gestión funcional de pacientes.
- Programación de reglas clínicas y flujos de atención médica.
- Integraciones reales con dispositivos, wearables o sistemas hospitalarios.
- Implementación completa de todos los requerimientos funcionales del caso.

Cada equipo elige el subconjunto que permite validar decisiones relevantes de su
arquitectura. Puede utilizar entradas enviadas manualmente, herramientas de prueba
o componentes mínimos, sin desarrollar ni entregar un generador completo.
Por ejemplo, un evento sintético marcado como crítico puede validar un flujo de
recepción y notificación a un canal de prueba, sin realizar diagnóstico ni clasificación clínica.
Este ejemplo no prescribe servicios, topología ni una arquitectura a replicar.

**Validación del alcance:** esta delimitación es la propuesta de trabajo acordada
por el docente. Debe comunicarse y validarse con la coordinación VcM y la empresa;
no equivale a una aceptación del socio ni modifica los requerimientos del caso original.

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

Los RF son contexto para decidir cómo la arquitectura soportaría esas necesidades;
no una lista de funcionalidades que deban programarse íntegramente. Cada equipo
prioriza su prueba de concepto y justifica las decisiones.
Distinguir requisitos abordados mediante diseño, implementados, simulados y pendientes. Los umbrales usados
en pruebas son ficticios: no deben interpretarse como recomendaciones clínicas.

## Metas del caso y validación técnica acotada

Las metas siguientes orientan el diseño productivo. La prueba de concepto valida
solo los aspectos seleccionados: no exige acreditar todos estos valores en el laboratorio.
Justificar con diseño los restantes y registrar qué se midió realmente.

| Condición del caso | Evidencia para validar la propuesta |
|---|---|
| RNF-01 Flujo crítico <1 s | Diseñar el flujo; si se prueba, medir latencia y errores con condiciones y tamaño de muestra |
| RNF-02 Incremento del 200% en <30 s | Explicitar interpretación de la carga y medir respuesta/escalamiento; informar limitaciones |
| RNF-03 99,99% de disponibilidad | Diseño y pruebas de fallo/recuperación; una demo breve no acredita el SLA anual |
| RNF-04 TLS 1.2+, cifrado en reposo y MFA | Evidencias de controles aplicados y restricciones; HTTP local no acredita TLS |
| RNF-05 RPO <=5 min / RTO <=30 min | Diseñar respaldo/recuperación y ejecutar una prueba acotada cronometrada |
| RNF-06 Observabilidad | Logs, métricas y alerta técnica de prueba |
| RNF-07 Mantenibilidad | Separación de componentes y estrategia de actualización, sin exigir implementar un clasificador |
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

## Entregables del proyecto

1. Propuesta de arquitectura: diagrama, alternativas, decisiones y relación con RF/RNF.
2. Infraestructura de la prueba de concepto: configuración reproducible, alcance y restricciones.
3. Evidencias técnicas: procedimiento, resultados observados, limitaciones y costos.
4. Presentación para la empresa: valor de la propuesta, avance real y preguntas de validación.

No se exige un producto clínico funcional. Una prueba de conectividad, persistencia,
control de acceso, recuperación o notificación puede aportar evidencia útil si
demuestra una decisión relevante. No afirmar que una prueba aislada valida toda la solución.

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
