import ScribeLog as lo
from ScribeLog import FileError
lo.ConfigLog("Logs\FileLogTest.log")
lo.Log("Este es un log de prueba")
lo.Log(f"El file de log se llama:{lo.GetPathLogin()}")

TestQa = lo.FileLogger("Logs\FileLogQA.log")
TestOper = lo.FileLogger("Logs\FileLogOper.log")

TestQa.Log("Este es un log de QA",time=False)
TestOper.Log("Este es un log de OPER")

TestQa.Log(f"El file de log de QA se llama:{TestQa.GetPathLogin()}")
TestOper.Log(f"El file de log de OPER se llama:{TestOper.GetPathLogin()}")

try:
    TestInvalido = lo.ConfigLog("/ruta/no/valida/archivo.log")
except FileError as e:
    print(f"Ocurrió un error: {e}")