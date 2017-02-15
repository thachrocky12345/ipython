from twisted.application import internet, service
from twisted.web import static, server

root = static.File("/var/www/htdocs")
application = service.Application('web')
site = server.Site(root)
sc = service.IServiceCollection(application)
i = internet.TCPServer(80, site)
i.setServiceParent(sc)
