from twisted.web import vhost
resource = vhost.VHostMonsterResource()
<VirtualHost ip-addr>
ProxyPass / http://localhost:8538/
ServerName example.com
</VirtualHost>

<VirtualHost ip-addr>
ProxyPass / http://localhost:8538/vhost.rpy/http/example.com:8082/
ServerName example.com
</VirtualHost>
