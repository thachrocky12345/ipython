from twisted.application import internet, service
from twisted.web import proxy, server, vhost
vhostName = 'example.com'
reverseProxy = proxy.ReverseProxyResource('internal', 8538,
                                          '/vhost.rpy/http/'+vhostName+'/')
root = vhost.NameVirtualHost()
root.addHost(vhostName, reverseProxy)
site = server.Site(root)
application = service.Application('web-proxy')
sc = service.IServiceCollection(application)
i = internet.TCPServer(80, site)
i.setServiceParent(sc)
