from pathlib import Path
from datetime import datetime

LOG_DIR = Path(__file__).parent.parent.parent / "log.txt"

class Log:
    def _log(self, msg):
        raise NotImplementedError("Implemente o método log")
    
    def log_error(self, msg):
        return self._log(f"Error: {msg}")

    def log_success(self, msg):
        return self._log(f"Success: {msg}")

class LogFileMixin(Log):
     def _log(self, msg):
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        msg_formatada = f"[{data_hora}] {msg}"
        with open(LOG_DIR, 'a', encoding="UTF-8") as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write("\n")

class LogPrintMixin(Log):
     def _log(self, msg):
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"[{data_hora}] {msg}")

