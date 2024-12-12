import random
import json
from datetime import datetime, timedelta


class GenerateLogMock:
    HTTP_METHODS = ["POST", "GET", "DELETE", "PUT"]
    ENDPOINTS = ["/index.html", "/login", "/about", "/api", "/auth", "/admin"]
    STATUS_CODES = [200, 404, 400, 500, 302]

    def __init__(
        self, file_name: str, is_text_log: bool = True, num_of_lines: int = 100
    ):
        self.num_of_lines = num_of_lines
        self.is_text_log = is_text_log
        self.file_name = file_name
        self.__set_file_type()

    def __generate_ip_address(self) -> str:
        ip_start = "192.168.1."
        return ip_start + str(random.randint(2, 254))

    def __generate_http_method(self) -> str:
        return random.choice(self.HTTP_METHODS)

    def __generate_endpoint(self) -> str:
        return random.choice(self.ENDPOINTS)

    def __generate_status_code(self) -> int:
        return random.choice(self.STATUS_CODES)

    def __generate_size(self) -> int:
        return random.randint(100, 2048)

    def __generate_timestamp(self) -> datetime:
        start_time = datetime.now()
        random_day = random.randint(0, 30)
        random_hours = random.randint(0, 23)
        random_minutes_or_seconds = random.randint(0, 59)
        return (
            start_time
            - timedelta(
                days=random_day,
                hours=random_hours,
                minutes=random_minutes_or_seconds,
                seconds=random_minutes_or_seconds,
            )
        ).strftime("%d/%b/%Y:%H:%M:%S +0000")

    def __generate_text_log(self, ip, timestamp, method, endpoint, code, size) -> str:
        return f'{ip} - - [{timestamp}] "{method} {endpoint} HTTP/1.1" {code} {size}\n'

    def __generate_json_log(self, ip, timestamp, method, endpoint, code, size) -> dict:
        return {
            "ip_address": ip,
            "timestamp": timestamp,
            "http_method": method,
            "endpoint": endpoint,
            "status_code": code,
            "req_size": size,
        }

    def __set_file_type(self) -> None:
        if self.is_text_log is True:
            self.file_name = self.file_name + ".log"
        else:
            self.file_name = self.file_name + ".json"

    def __generate_log_line(self) -> str:
        ip = self.__generate_ip_address()
        method = self.__generate_http_method()
        endpoint = self.__generate_endpoint()
        code = self.__generate_status_code()
        timestamp = self.__generate_timestamp()
        size = self.__generate_size()
        if self.is_text_log is True:
            return self.__generate_text_log(ip, timestamp, method, endpoint, code, size)
        else:
            return self.__generate_json_log(ip, timestamp, method, endpoint, code, size)

    def create_logs_file(self) -> None:
        log_lines = []
        for _ in range(self.num_of_lines):
            log_lines.append(self.__generate_log_line())
        with open(self.file_name, "w") as file:
            if self.is_text_log is True:
                file.writelines(log_lines)
            else:
                json.dump(log_lines, file, indent=4)
        print("log created!")


log = GenerateLogMock(file_name="webserver", is_text_log=True, num_of_lines=50)

log.create_logs_file()
