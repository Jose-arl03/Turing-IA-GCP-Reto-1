import pytest
from unittest.mock import patch
import main 

# Clase simulada para el evento de Cloud Storage
class MockCloudEvent:
    def __init__(self, data):
        self.data = data

def test_procesar_archivo_exito():
    """Prueba el flujo exitoso con un payload válido."""
    payload = {
        "name": "reporte_ventas.pdf",
        "size": "2048576",
        "contentType": "application/pdf"
    }
    evento_simulado = MockCloudEvent(data=payload)
    
    # Si la función no lanza excepciones, la prueba es exitosa
    try:
        main.procesar_archivo(evento_simulado)
        assert True
    except Exception:
        pytest.fail("La función falló inesperadamente con un payload válido")

def test_procesar_archivo_error():
    """Prueba el manejo de errores con un payload malformado (sin 'name')."""
    payload = {
        "size": "1024",
        "contentType": "text/plain"
    }
    evento_simulado = MockCloudEvent(data=payload)
    
    # Verificamos que capture el error y levante una excepción
    with pytest.raises(Exception):
        main.procesar_archivo(evento_simulado)