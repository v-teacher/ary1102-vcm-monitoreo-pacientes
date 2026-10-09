# Sistema de Monitoreo Remoto de Pacientes Críticos

Aplicación base de ARY1102, período 2026/02, para el proyecto VcM. Este código
es un recurso docente nuevo; no corresponde al `producer.py` institucional
mencionado en el PDF, que no estaba disponible en los antecedentes recibidos.

Simulador → API → validación/clasificación → historial y alerta simulada → panel.
La clasificación utiliza `signal_score`, un índice artificial: <40 Normal,
40–69 Precaución y >=70 Crítico. Los límites son didácticos, no umbrales clínicos.
Los valores de frecuencia cardiaca y saturación son ficticios y no deciden el estado.

## Inicio local con Python

Requiere Python 3.12 o posterior. No necesita paquetes externos.
Desde esta carpeta, abrir dos terminales. En ambas configurar el mismo token
temporal de laboratorio; no copiarlo a Git, capturas o informes:

```bash
export API_TOKEN='token-sintetico-solo-laboratorio'
python3 -m app.server
```

En la segunda terminal:

```bash
export API_TOKEN='token-sintetico-solo-laboratorio'
python3 producer.py --url http://127.0.0.1:8080/events --count 30 --rate 2
```

Abrir http://127.0.0.1:8080, ingresar el token y consultar. El panel no guarda el
token en almacenamiento del navegador. La alerta es un registro PENDIENTE visible
en el panel; no hay entrega de mensajes a personal real ni confirmación de recepción.

## Inicio con Docker

```bash
export API_TOKEN='token-sintetico-solo-laboratorio'
docker compose up --build -d
docker compose ps
python3 producer.py --url http://127.0.0.1:8080/events --count 30 --rate 2
docker compose down
```

El volumen conserva eventos al detener Compose. `docker compose down --volumes`
elimina los datos sintéticos persistidos: usarlo únicamente si se desea reiniciar
la demostración. Compose expone el servicio solo en la interfaz local.

## Contrato y pruebas

| Método/ruta | Uso |
|---|---|
| GET `/health` | Salud pública del proceso; no prueba integraciones cloud |
| GET `/` | Panel sin datos hasta ingresar token |
| POST `/events` | Ingesta autenticada; 201 nuevo, 200 repetido, 409 ID en conflicto |
| GET `/events` | Últimos 100 eventos, máximo 1000; consulta por `patient_id`, `since`, `until`, `limit` |
| GET `/alerts` | Hasta 100 alertas simuladas, orden reciente |
| GET `/export.csv` | Exporta la misma consulta acotada que `/events` |

Las rutas de datos requieren `Authorization: Bearer <API_TOKEN>`.
`timestamp`, `since` y `until` usan ISO 8601 con zona horaria. Campos adicionales
se rechazan; el contrato no incluye nombres ni otros identificadores reales.
El filtro sintáctico no detecta datos reales disfrazados de identificadores sintéticos:
utilizar exclusivamente el generador y los fixtures de esta aplicación.

```json
{"event_id":"demo-1","patient_id":"SYN-0001","timestamp":"2026-10-09T12:00:00Z","heart_rate":75,"spo2":98,"signal_score":90}
```

```bash
python3 -m unittest discover -s tests -v
python3 producer.py --count 6
```

`datasets/telemetria-sintetica.jsonl` contiene tres fixtures con los estados esperados.
El generador produce JSONL sin `--url`; con URL envía eventos secuencialmente,
con máximo didáctico de 20 eventos/s. No es una herramienta para acreditar 1000
eventos/s. La semilla fija los valores numéricos; UUID y fecha cambian en cada ejecución.

## Límites y evolución del curso

Esta base usa SQLite en una sola réplica. Copiarla a varias tareas con un disco por
tarea fragmenta el historial; NO acredita alta disponibilidad. En EA2 deben sustituir
el almacenamiento por un servicio administrado compartido y demostrarlo mediante
consulta posterior a reinicio/cambio de réplica. No se entrega una solución cloud terminada.

El token compartido permite la demostración local; no implementa RF-07 (roles),
MFA, auditoría completa, cambios autorizados de umbrales, acuse de alertas, ni respaldo
gestionado. TLS debe resolverse en el ingreso cloud; HTTP local no cumple el RNF
productivo. No abrir esta base HTTP directamente a Internet con datos o tokens reales.

RF-04 está representado parcialmente por la alerta simulada; RF-06 parcialmente por
historial de eventos, sin acciones clínicas. RF-08 y RF-11 son trabajo pendiente,
no funciones acreditadas por el código inicial. Tampoco se acredita SLA, RPO/RTO ni
escalamiento automático con esta base.

En EA3 reutilizar `app/domain.py` en funciones, agregar persistencia, cola/reintentos,
control de duplicados y manejo de errores. Los estudiantes diseñan e implementan
los adaptadores cloud y justifican las decisiones; esta base no incluye Terraform
ni un despliegue AWS preconfigurado.

## Material académico

- [Enunciado VcM](docs/Enunciado_VcM_ARY1102.md).
- [Integración curricular y guía docente](docs/Integracion_Curricular_VcM_ARY1102.md).
- EA2: [comparación](docs/actividades/ea2/2.1_VcM_Actividad.md), [diseño](docs/actividades/ea2/2.2_VcM_Actividad.md), [implementación](docs/actividades/ea2/2.3_VcM_Actividad.md).
- EA3: [evaluación](docs/actividades/ea3/3.1_VcM_Actividad.md), [diseño](docs/actividades/ea3/3.2_VcM_Actividad.md), [implementación](docs/actividades/ea3/3.3_VcM_Actividad.md).
- [Hitos](docs/Hitos_VcM_2026.02.md), [anuncio AVA](docs/Anuncio_AVA_Hito1.md), [plantilla de avance](docs/Plantilla_Avance_Hito2.md) y [borrador de correo](docs/Borrador_Correo_Hito2.md).
- [Validación local](VALIDACION.md).

Ubicación principal: `repos/ary1102/ary1102-vcm-monitoreo-pacientes`.
Repositorio público: [v-teacher/ary1102-vcm-monitoreo-pacientes](https://github.com/v-teacher/ary1102-vcm-monitoreo-pacientes).
Los antecedentes institucionales internos no forman parte del repositorio.
No publicar datos personales, respuestas privadas del socio ni credenciales.
