# Challenge QA

Este proyecto contiene la automatización de pruebas funcionales y de API para el sitio https://www.saucedemo.com/.

## Instrucciones

1. Crear entorno virtual
2. Instalar dependencias:
```bash
pip install -r requirements.txt
```
3. Ejecutar pruebas:
```bash
pytest --html=reports/reporte.html
```

## Estructura
- `tests/`: Casos de prueba automatizados
- `pages/`: Clases de páginas (Page Object Model)
- `utils/`: Configuración de Pytest
- `docs/`: Documentación funcional
- `screenshots/`: Evidencias de fallos
- `reports/`: Reportes de ejecución