import random
import json
from faker import Faker
from datetime import datetime, timedelta


class GenerateMockJsonLogFile:
    _FAKE = Faker()
    _IP = "192.168.1."
    _HOSTNAMES = ["server.local", "gateway.local", "dbserver.local"]
    _METHODS = ["GET", "POST", "PUT", "DELETE"]
    _REQ_URI = ["/api/data", "/api/auth", "/login", "/index.html", "/admin"]
    _STATUS_CODES = [200, 302, 400, 404, 500]
    _USER_AGENTS = [
        "curl/7.68.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "PostmanRuntime/7.28.4",
    ]
    _ACTIONS = [
        "Accessed resource",
        "Requested data",
        "Uploaded file",
        "Downloaded file",
    ]
    _PROTOCOL_PORT_MAP = [
        {"protocol": "HTTP", "port": 80},
        {"protocol": "HTTPS", "port": 443},
        {"protocol": "FTP", "port": 21},
        {"protocol": "SFTP", "port": 22},
        {"protocol": "SMTP", "port": 25},
        {"protocol": "IMAP", "port": 143},
        {"protocol": "POP3", "port": 110},
        {"protocol": "DNS", "port": 53},
        {"protocol": "SNMP", "port": 161},
        {"protocol": "SSH", "port": 22},
        {"protocol": "Telnet", "port": 23},
        {"protocol": "LDAP", "port": 389},
        {"protocol": "XMPP", "port": 5222},
        {"protocol": "HTTP/2", "port": 443},
        {"protocol": "TCP", "port": None},
        {"protocol": "UDP", "port": None},
        {"protocol": "SCTP", "port": None},
        {"protocol": "DCCP", "port": None},
        {"protocol": "IP", "port": None},
        {"protocol": "ICMP", "port": None},
        {"protocol": "ARP", "port": None},
        {"protocol": "IGMP", "port": None},
    ]

    def _timestamp(self) -> datetime:
        start_time = datetime.now()
        day = random.randint(0, 30)
        hours = random.randint(0, 23)
        min = random.randint(0, 59)
        return (
            start_time - timedelta(days=day, hours=hours, minutes=min, seconds=min)
        ).strftime("%d/%b/%Y:%H:%M:%S +0000")

    def _ip_address(self) -> str:
        return self._IP + str(random.randint(2, 254))

    def _mac_address(self):
        mac = [
            random.randint(0x00, 0xFF),
            random.randint(0x00, 0xFF),
            random.randint(0x00, 0xFF),
            random.randint(0x00, 0xFF),
            random.randint(0x00, 0xFF),
            random.randint(0x00, 0xFF),
        ]
        return ":".join(f"{x:02x}" for x in mac)

    def create_entry(self):
        protocol_entry = random.choice(self._PROTOCOL_PORT_MAP)
        protocol = protocol_entry["protocol"]
        port = protocol_entry["port"]

        return {
            "timestamp": self._timestamp(),
            "source_ip": self._ip_address(),
            "destination_ip": self._ip_address(),
            "protocol": protocol,
            "source_port": port,
            "destination_port": random.randint(3000, 20000),
            "device_name": "Device-" + str(random.randint(10, 1000)),
            "hostname": random.choice(self._HOSTNAMES),
            "request_method": random.choice(self._METHODS),
            "request_uri": random.choice(self._REQ_URI),
            "status_code": random.choice(self._STATUS_CODES),
            "response_size": random.randint(1000, 5000),
            "response_time_ms": random.randint(50, 200),
            "latency_ms": random.randint(5, 20),
            "mac_address": self._mac_address(),
            "device_type": "Server",
            "network_segment": "192.168.1.0/24",
            "request_id": self._FAKE.uuid4(),
            "user_agent": random.choice(self._USER_AGENTS),
            "auth_status": random.choice(["Authenticated", "Failed"]),
            "error_message": None,
            "data_transfered_bytes": random.randint(500, 5000),
            "server_name": random.choice(self._HOSTNAMES),
            "ssl_protocol": random.choice(["TLSv1.2", "TLSv1.3"]),
            "ssl_cipher": random.choice(
                ["AES128-GCM-SHA256", "ECDHE-RSA-AES256-GCM-SHA384"]
            ),
            "protocol_version": "1.1",
            "packet_count": random.randint(5, 50),
            "dns_query": self._FAKE.domain_name(),
            "firewall_status": random.choice(["Allowed", "Blocked"]),
            "intrusion_detected": random.choice([True, False]),
            "geo_location": {
                "country": self._FAKE.country(),
                "city": self._FAKE.city(),
                "latitude": str(self._FAKE.latitude()),
                "longitude": str(self._FAKE.longitude()),
            },
            "user_name": self._FAKE.user_name(),
            "action": random.choice(self._ACTIONS),
        }

    def create_logs_file(self, num_of_lines, file_name) -> None:
        log_lines = []
        for _ in range(num_of_lines):
            log_lines.append(self.create_entry())
        with open(file_name + ".json", "w") as file:
            json.dump(log_lines, file, indent=4)
        print("log created!")


log = GenerateMockJsonLogFile()

log.create_logs_file(3, "custom_log")
