from pathlib import Path

from dotenv import load_dotenv
from starlite import Starlite, Template, get
from starlite.config import TemplateConfig
from starlite.contrib.jinja import JinjaTemplateEngine

from controllers.routes import RoutesController
from controllers.status import StatusController


@get()
async def index() -> Template:
    return Template(name="index.html", context={"title": "Home"})

load_dotenv()
app = Starlite(
    route_handlers=[index, StatusController, RoutesController],
    template_config=TemplateConfig(
        directory=Path("templates"),
        engine=JinjaTemplateEngine,
    )
)
