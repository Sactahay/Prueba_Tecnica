# Módulo de Gestión de Proyectos de Investigación para Odoo 18

Este módulo para Odoo 18 proporciona una funcionalidad completa para la gestión de proyectos de investigación, permitiendo a los usuarios organizar, seguir y reportar el progreso de sus investigaciones.

## Descripción General del Módulo

El módulo `research_project` introduce un nuevo modelo llamado `research.project` que permite gestionar la información esencial de los proyectos de investigación, incluyendo:

* Nombre del proyecto
* Código único del proyecto (generado automáticamente)
* Descripción detallada
* Fechas de inicio y finalización estimadas
* Presupuesto asignado
* Estado del proyecto (Nuevo, En Progreso, En Revisión, Completado, Cancelado)
* Prioridad del proyecto
* Lista de investigadores participantes
* Investigador principal
* Cálculo automático del progreso del proyecto

Además, el módulo incluye vistas intuitivas para la gestión de los proyectos, lógica de negocio para el flujo de trabajo, un informe en PDF para la documentación y medidas de seguridad para controlar el acceso.

## Instrucciones de Instalación

Para instalar este módulo en tu instancia de Odoo 18, sigue estos pasos:

1.  Asegúrate de tener Odoo 18 instalado y en funcionamiento.
2.  Coloca la carpeta `research_project` dentro del directorio de addons de tu instalación de Odoo. Puedes encontrar este directorio siguiendo la ruta que identificamos al principio (o la ruta configurada en tu archivo de configuración de Odoo).
3.  Activa el modo desarrollador en Odoo (Ajustes > Información técnica > Activar el modo desarrollador).
4.  Ve a la aplicación de "Módulos".
5.  Haz clic en el botón "Actualizar lista de aplicaciones".
6.  Busca el módulo "Proyectos de Investigación" y haz clic en el botón "Instalar".

## Explicación de las Funcionalidades Implementadas

* **Modelo `research.project`:** Define la estructura de los proyectos de investigación con los campos especificados. Incluye un campo computado para el progreso, una restricción para las fechas y un método `onchange` para el investigador principal.
* **Secuencia Automática:** El campo `code` se genera automáticamente al crear un nuevo proyecto con el formato `PR000X`.
* **Vistas:**
    * **Formulario:** Permite la creación y edición detallada de los proyectos, con botones para cambiar el estado, campos organizados y pestañas para descripción e investigadores.
    * **Árbol (Lista):** Ofrece una visión general de los proyectos, agrupada por estado por defecto y con columnas relevantes.
* **Lógica de Negocio:**
    * Botones en el formulario para cambiar el estado del proyecto.
    * Restricción para asegurar que la fecha de inicio no sea posterior a la fecha de finalización.
    * Método `onchange` para alertar si el investigador principal no está en la lista de participantes y ofrecer agregarlo.
* **Informe (QWeb Report):** Genera un PDF con la información detallada del proyecto y la lista de investigadores participantes.
* **Seguridad:**
    * Se definieron dos grupos de seguridad: "Usuario de Proyectos de Investigación" y "Administrador de Proyectos de Investigación".
    * Se implementaron reglas de acceso (`ir.model.access.csv`) para controlar los permisos de cada grupo sobre el modelo `research.project`.

## Consideraciones Especiales o Mejoras Potenciales

* **Workflow más complejo:** Se podría implementar un workflow más detallado con transiciones de estado automáticas o validaciones adicionales.
* **Gestión de tareas:** Añadir la capacidad de gestionar tareas específicas dentro de cada proyecto de investigación.
* **Seguimiento de costos:** Implementar el seguimiento de los costos reales incurridos en el proyecto y compararlos con el presupuesto.
* **Alertas y notificaciones:** Configurar alertas automáticas para eventos importantes (ej: proyecto cerca de su fecha de finalización).
* **Gráficos y análisis:** Incorporar gráficos para visualizar el progreso de los proyectos, la distribución por estado, etc.

¡Este módulo proporciona una base sólida para la gestión de proyectos de investigación en Odoo 18!