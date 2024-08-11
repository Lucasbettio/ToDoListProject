from aiohttp import web
# Importar Controllers


async def status():
    '''
    Status Function:
    Only to test if API is running and working
    * Params: request, useless in this case
    '''
    return web.Response(text="API is healthy and working!")

class Routes:
    def __init__(self):
        self.routes = []
        self.routes.append(web.get("/status", status))
        
        # Criar coleção de rotas conforma controllers!!!
        # Deixarei uma coleção de rotas de exemplo por enquanto...
        self._set_example_routes()
        
    def _set_example_routes(self):
        # Pegar o import do controller e colocar aqui
        example_controller = ExampleController()
        
        self.routes.append(web.get("/examples", example_controller.get_examples))
        self.routes.append(web.post("/example/{id}", example_controller.get_example_by_id))
        self.routes.append(web.remove("example/{id}", example_controller.remove_example))
        
    def get_routes(self) -> list:
        return self.routes