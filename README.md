**Examen 1**
**Asignatura:** Ingeniería DevOps (DOY0101)
**Integrantes:** Daniel Betancourt - Rodrigo Muñoz

## Estrategia de Ramificación (GitFlow)
* **Trunk-Based Development:** Propone trabajar casi todo directamente sobre una rama principal (main), haciendo integraciones de código muy seguidas (varias veces al día). Aunque reduce los conflictos pesados de merge, requiere tener una batería de pruebas automatizadas muy madura para no romper producción de forma continua.
* **GitFlow:** Define dos ramas de vida larga (main para código estable y develop para integración) y utiliza ramas auxiliares de vida corta (feature para nuevas funciones y hotfix para correcciones de emergencia).

### ¿Por qué elegimos GitFlow?
Nos decidimos por **GitFlow** principalmente por la estructura del trabajo y el contexto del proyecto:
1. Nos permite desarrollar y probar cambios en la rama develop sin arriesgar la versión estable que está en main.
2. Como trabajamos en parejas, trabajar en ramas aisladas (feature) evita que colisionemos con el código del otro mientras la funcionalidad no esté terminada.
3. Permite simular parches críticos en producción usando ramas hotfix directas desde main, un flujo clave que exige la rúbrica de la evaluación.

### Mapeo de Ramas en el Repositorio
* main: Contiene el código probado y listo para producción.
* develop: Rama central donde integramos el trabajo diario antes de un release.
* feature: Ramas temporales creadas desde develop para agregar funcionalidades.
* hotfix: Ramas temporales creadas desde main para resolver bugs urgentes en producción.

## Convenciones de commits

### Formato de Mensajes de Commit
Aplicamos una convención basada en *Conventional Commits* redactada en español:

tipo: mensaje corto que explique el cambio en presente.