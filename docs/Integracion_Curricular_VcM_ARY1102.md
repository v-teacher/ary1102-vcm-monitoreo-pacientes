# Integración curricular VcM · Guía docente

Caso: **Sistema de Monitoreo Remoto de Pacientes Críticos**. Elaborado 09-10-2026.
Fuentes: caso institucional (6 páginas), comunicaciones VcM, PA226 y PDA226 ARY1102.

## Incorporación

Introducir el caso en EA2 usando una sesión de encuadre dentro de las actividades
existentes. Aprovechar conceptos de EA1; EP1/FreshBox ya evaluada no se modifica.
Esta adaptación conserva RA/IL, horas y ponderaciones; no altera fechas de evaluaciones.

Hitos comunicados por el docente: presentación del caso (1), envío de avance
durante **19–25 de octubre de 2026** y espera de feedback empresarial (2), y
exposición con fecha/modalidad pendientes (3). Consultar [plan de hitos](Hitos_VcM_2026.02.md).
Preparar avance con 2.1/2.2 y pruebas de 2.3 disponibles, sin esperar al MVP completo.
Incorporar respuesta efectivamente recibida en 3.1 y en la exposición.

| Actividad | Horas pedagógicas del PA | Indicador | Evidencia VcM |
|---|---:|---|---|
| 2.1 | 5 | IL3.1 | Comparación tradicional/orquestación/PaaS |
| 2.2 | 6 | IL3.2 | Diagrama, decisiones, controles y matriz RF/RNF |
| 2.3 | 7 | IL3.3 | Aplicación desplegada, pruebas y operación |
| 3.1 | 4 | IL4.1 | Evaluación de costos, seguridad, rendimiento y negocio |
| 3.2 | 6 | IL4.2 | Diseño desacoplado, escalamiento y recuperación |
| 3.3 | 7 | IL4.3 | Funciones, API y almacenamiento con pruebas funcionales |

Las seis guías adaptadas están en sus carpetas de actividades. Son recursos
complementarios: no se presentan como PPT, rúbrica o enunciado institucional original.

## Encargo EP2 propuesto

Mantener informe técnico y presentación individual. Pedir comparación de modelos,
diagrama con orquestación/PaaS, implementación y pruebas, justificación en función
del negocio. Incluir matriz RF/RNF y versión del código usado en la demostración.
Evaluar con el instrumento institucional de EP2 cuando esté disponible; no reutilizar
la rúbrica de EP1 ni inventar porcentajes para indicadores de EP2.

## Encargo EP3 propuesto

Mantener informe técnico y presentación individual. Pedir análisis de arquitectura
existente, evolución serverless, implementación funcional de funciones/APIs/datos,
desacoplamiento, validación de costos, seguridad y rendimiento. Usar el instrumento
institucional de EP3; las listas de las actividades son retroalimentación formativa.

## Preparación EFT

Construir una solución integrada: interfaz/consulta contenerizada y orquestada,
persistencia administrada y procesamiento de eventos serverless, sobre una base
segura. Exigir justificar cada componente, evitando servicios redundantes solo para
llenar un diagrama. La EFT debe evidenciar integración de enfoques, no dos demos
aisladas. El instrumento final se comunica conforme a la planificación institucional.

## Validación del entorno antes de elegir servicios

Leer la documentación vigente dentro de Learner Lab y probar permisos/regiones,
roles, cuotas y presupuesto en la cuenta de trabajo. Los nombres de servicios
seleccionados por cada equipo requieren validación técnica previa: este paquete
no acredita permisos para orquestación, PaaS, colas o funciones en ninguna cuenta.
Consultar las restricciones vigentes en el portal de Learner Lab. Las alternativas limitadas por permisos deben dejar evidencia del error y una justificación; una restricción no equivale a implementación.

En EA2, asegurar que las instancias/tareas descargan imágenes previamente publicadas.
No copiar tokens AWS temporales dentro de contenedores, imágenes o código. La
base local HTTP/token no acredita MFA, autorización de roles ni TLS productivo.

## Acompañamiento y pruebas

- Ejecutar la aplicación docente y los fixtures antes del encuadre.
- Entregar contratos y ejemplos; los estudiantes implementan adaptadores cloud.
- Usar escenarios normales, de precaución y críticos, más datos inválidos y duplicados.
- Capturar tiempos recepción→alerta, denominador de errores, carga y período medido.
- Evitar cargar 1.000 eventos/s por defecto; empezar con 2 eventos/s y ampliar con control.
- Probar pérdida/reinicio de una réplica, persistencia y una recuperación acotada.
- Separar metas productivas, simulaciones y resultados efectivamente observados.
- Guardar evidencias y finalizar recursos que consumen presupuesto.

## Coordinación VcM

Mantener exactamente el nombre del caso en documentos y futuro registro de equipos.
La comunicación recibida anuncia instrucciones posteriores de registro, sin solicitar
registro inmediato. La composición de equipos y el contacto/validación con el socio
se coordinan institucionalmente. No se ha inventado un acta de aceptación ni métricas
de impacto del socio. La valoración de utilidad requiere retroalimentación real
cuando esa interacción sea organizada.

El simulador y los fixtures son elaboración docente, pues faltan los apoyos originales
enumerados en el PDF. Antes de presentar resultados al socio, depurar las evidencias
y usar los canales autorizados, conservando el carácter académico del prototipo.
