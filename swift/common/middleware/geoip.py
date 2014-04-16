

class SwiftGeoIPMiddleware(object):
    """Middleware doing virus scan for Swift."""
 
    def __init__(self, app, conf):
        # app is the final application
        self.app = app
 
    def __call__(self, env, start_response):
        return self.app(env, start_response)
 

def filter_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)
 
    def GeoIP_filter(app):
        return SwiftGeoIPMiddleware(app, conf)
    return GeoIP_filter
