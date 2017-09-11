import redis
from api.util import settings
import sendemail

class RedisPing(object):

    def __init__(self):
        self.failedList = []
        self.pool = None

    def run(self):
        """Monitera all redis servers use ping CMD
        """
        redis_servers = settings.get_redis_servers()

        for redis_server in redis_servers:
            redis_password = redis_server.get("password")
            self.ping(redis_server["server"], redis_server["port"], redis_password)

        if len(self.failedList) > 0:
            self.sendMail()

    def ping(self, rserver, rport, rpassword):
        """send ping command, send a alter email when ping failed.
        """
        try:
            if self.pool is None:
                pool = redis.ConnectionPool(host=rserver, port=rport, db=0, password=rpassword)
            connection = pool.get_connection('ping', None)
            connection.send_command("ping")
            return True
        except Exception:
            self.failedList.append(rserver + ":" + str(rport))
            return False

    def sendMail(self):
        """Send alter mail when ping failed.
        """
        content = '<table><thead><tr><th>IP</th><th>DOWN</th></tr></thead><tbody>'
        for f in self.failedList:
            content += '<tr><td style="padding: 8px;line-height: 20px;vertical-align: top;border-top: 1px solid #ddd;">'
            content += f + '</td>'
            content += '<td style="color: red;padding: 8px;line-height: 20px;vertical-align: top;border-top: 1px solid #ddd;">yes</td>'
        content += '</tbody></table>'
        mailConfig = settings.get_mail()
        sendemail.send(mailConfig.get('FromAddr'), mailConfig.get('ToAddr'), mailConfig.get('SMTPServer'), content)

if __name__ == '__main__':
    rp = RedisPing()
    rp.run()        
