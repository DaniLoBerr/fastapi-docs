from fastapi import APIRouter

from lesson_routers import lesson_routers as lesson_routers_list

SECTION_DEFINITIONS = [
    {
        "slug": "foundations",
        "title": "Fundamentos de Python, async y entorno",
        "lessons": [
            {
                "slug": "python-types-intro",
                "title": "Python Types Intro",
                "url": "https://fastapi.tiangolo.com/python-types/",
            },
            {
                "slug": "concurrency-and-async-await",
                "title": "Concurrency and async / await",
                "url": "https://fastapi.tiangolo.com/async/",
            },
            {
                "slug": "environment-variables",
                "title": "Environment Variables",
                "url": "https://fastapi.tiangolo.com/environment-variables/",
            },
            {
                "slug": "virtual-environments",
                "title": "Virtual Environments",
                "url": "https://fastapi.tiangolo.com/virtual-environments/",
            },
        ],
    },
    {
        "slug": "user-guide",
        "title": "Tutorial Básico de FastAPI",
        "lessons": [
            {
                "slug": "tutorial-user-guide",
                "title": "Tutorial - User Guide",
                "url": "https://fastapi.tiangolo.com/tutorial/",
            },
            {
                "slug": "first-steps",
                "title": "First Steps",
                "url": "https://fastapi.tiangolo.com/tutorial/first-steps/",
            },
            {
                "slug": "path-parameters",
                "title": "Path Parameters",
                "url": "https://fastapi.tiangolo.com/tutorial/path-params/",
            },
            {
                "slug": "query-parameters",
                "title": "Query Parameters",
                "url": "https://fastapi.tiangolo.com/tutorial/query-params/",
            },
            {
                "slug": "request-body",
                "title": "Request Body",
                "url": "https://fastapi.tiangolo.com/tutorial/body/",
            },
            {
                "slug": "query-parameters-and-string-validations",
                "title": "Query Parameters and String Validations",
                "url": "https://fastapi.tiangolo.com/tutorial/query-params-str-validations/",
            },
            {
                "slug": "path-parameters-and-numeric-validations",
                "title": "Path Parameters and Numeric Validations",
                "url": "https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/",
            },
            {
                "slug": "query-parameter-models",
                "title": "Query Parameter Models",
                "url": "https://fastapi.tiangolo.com/tutorial/query-param-models/",
            },
            {
                "slug": "body-multiple-parameters",
                "title": "Body - Multiple Parameters",
                "url": "https://fastapi.tiangolo.com/tutorial/body-multiple-params/",
            },
            {
                "slug": "body-fields",
                "title": "Body - Fields",
                "url": "https://fastapi.tiangolo.com/tutorial/body-fields/",
            },
            {
                "slug": "body-nested-models",
                "title": "Body - Nested Models",
                "url": "https://fastapi.tiangolo.com/tutorial/body-nested-models/",
            },
            {
                "slug": "declare-request-example-data",
                "title": "Declare Request Example Data",
                "url": "https://fastapi.tiangolo.com/tutorial/schema-extra-example/",
            },
            {
                "slug": "extra-data-types",
                "title": "Extra Data Types",
                "url": "https://fastapi.tiangolo.com/tutorial/extra-data-types/",
            },
        ],
    },
    {
        "slug": "special-params",
        "title": "Parámetros especiales, modelos en capas y respuestas",
        "lessons": [
            {
                "slug": "cookie-parameters",
                "title": "Cookie Parameters",
                "url": "https://fastapi.tiangolo.com/tutorial/cookie-params/",
            },
            {
                "slug": "header-parameters",
                "title": "Header Parameters",
                "url": "https://fastapi.tiangolo.com/tutorial/header-params/",
            },
            {
                "slug": "cookie-parameter-models",
                "title": "Cookie Parameter Models",
                "url": "https://fastapi.tiangolo.com/tutorial/cookie-param-models/",
            },
            {
                "slug": "header-parameter-models",
                "title": "Header Parameter Models",
                "url": "https://fastapi.tiangolo.com/tutorial/header-param-models/",
            },
            {
                "slug": "response-model-return-type",
                "title": "Response Model - Return Type",
                "url": "https://fastapi.tiangolo.com/tutorial/response-model/",
            },
            {
                "slug": "extra-models",
                "title": "Extra Models",
                "url": "https://fastapi.tiangolo.com/tutorial/extra-models/",
            },
            {
                "slug": "response-status-code",
                "title": "Response Status Code",
                "url": "https://fastapi.tiangolo.com/tutorial/response-status-code/",
            },
        ],
    },
    {
        "slug": "forms-files-errors",
        "title": "Formularios, ficheros y manejo de errores",
        "lessons": [
            {
                "slug": "form-data",
                "title": "Form Data",
                "url": "https://fastapi.tiangolo.com/tutorial/request-forms/",
            },
            {
                "slug": "form-models",
                "title": "Form Models",
                "url": "https://fastapi.tiangolo.com/tutorial/request-form-models/",
            },
            {
                "slug": "request-files",
                "title": "Request Files",
                "url": "https://fastapi.tiangolo.com/tutorial/request-files/",
            },
            {
                "slug": "request-forms-and-files",
                "title": "Request Forms and Files",
                "url": "https://fastapi.tiangolo.com/tutorial/request-forms-and-files/",
            },
            {
                "slug": "handling-errors",
                "title": "Handling Errors",
                "url": "https://fastapi.tiangolo.com/tutorial/handling-errors/",
            },
            {
                "slug": "path-operation-configuration",
                "title": "Path Operation Configuration",
                "url": "https://fastapi.tiangolo.com/tutorial/path-operation-configuration/",
            },
            {
                "slug": "json-compatible-encoder",
                "title": "JSON Compatible Encoder",
                "url": "https://fastapi.tiangolo.com/tutorial/encoder/",
            },
            {
                "slug": "body-updates",
                "title": "Body - Updates",
                "url": "https://fastapi.tiangolo.com/tutorial/body-updates/",
            },
        ],
    },
    {
        "slug": "dependencies-security-middleware",
        "title": "Dependencias, seguridad básica y middleware",
        "lessons": [
            {
                "slug": "dependencies",
                "title": "Dependencies",
                "url": "https://fastapi.tiangolo.com/tutorial/dependencies/",
            },
            {
                "slug": "classes-as-dependencies",
                "title": "Classes as Dependencies",
                "url": "https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/",
            },
            {
                "slug": "sub-dependencies",
                "title": "Sub-dependencies",
                "url": "https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/",
            },
            {
                "slug": "dependencies-in-path-operation-decorators",
                "title": "Dependencies in path operation decorators",
                "url": "https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/",
            },
            {
                "slug": "global-dependencies",
                "title": "Global Dependencies",
                "url": "https://fastapi.tiangolo.com/tutorial/dependencies/global-dependencies/",
            },
            {
                "slug": "dependencies-with-yield",
                "title": "Dependencies with yield",
                "url": "https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/",
            },
            {
                "slug": "security",
                "title": "Security",
                "url": "https://fastapi.tiangolo.com/tutorial/security/",
            },
            {
                "slug": "security-first-steps",
                "title": "Security - First Steps",
                "url": "https://fastapi.tiangolo.com/tutorial/security/first-steps/",
            },
            {
                "slug": "get-current-user",
                "title": "Get Current User",
                "url": "https://fastapi.tiangolo.com/tutorial/security/get-current-user/",
            },
            {
                "slug": "simple-oauth2-with-password-and-bearer",
                "title": "Simple OAuth2 with Password and Bearer",
                "url": "https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/",
            },
            {
                "slug": "oauth2-with-password-and-bearer-jwt-tokens",
                "title": "OAuth2 with Password (and hashing), Bearer with JWT tokens",
                "url": "https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/",
            },
            {
                "slug": "middleware",
                "title": "Middleware",
                "url": "https://fastapi.tiangolo.com/tutorial/middleware/",
            },
            {
                "slug": "cors",
                "title": "CORS (Cross-Origin Resource Sharing)",
                "url": "https://fastapi.tiangolo.com/tutorial/cors/",
            },
        ],
    },
    {
        "slug": "sql-apps-background",
        "title": "BBDD SQL, estructura de apps grandes y tareas en segundo plano",
        "lessons": [
            {
                "slug": "sql-databases",
                "title": "SQL (Relational) Databases",
                "url": "https://fastapi.tiangolo.com/tutorial/sql-databases/",
            },
            {
                "slug": "bigger-applications-multiple-files",
                "title": "Bigger Applications - Multiple Files",
                "url": "https://fastapi.tiangolo.com/tutorial/bigger-applications/",
            },
            {
                "slug": "stream-json-lines",
                "title": "Stream JSON Lines",
                "url": "https://fastapi.tiangolo.com/tutorial/stream-json-lines/",
            },
            {
                "slug": "server-sent-events-sse",
                "title": "Server-Sent Events (SSE)",
                "url": "https://fastapi.tiangolo.com/tutorial/server-sent-events/",
            },
            {
                "slug": "background-tasks",
                "title": "Background Tasks",
                "url": "https://fastapi.tiangolo.com/tutorial/background-tasks/",
            },
        ],
    },
    {
        "slug": "docs-frontend-testing-debugging",
        "title": "Docs, frontend estático, testing y debugging",
        "lessons": [
            {
                "slug": "metadata-and-docs-urls",
                "title": "Metadata and Docs URLs",
                "url": "https://fastapi.tiangolo.com/tutorial/metadata/",
            },
            {
                "slug": "frontend",
                "title": "Frontend",
                "url": "https://fastapi.tiangolo.com/tutorial/frontend/",
            },
            {
                "slug": "static-files",
                "title": "Static Files",
                "url": "https://fastapi.tiangolo.com/tutorial/static-files/",
            },
            {
                "slug": "testing",
                "title": "Testing",
                "url": "https://fastapi.tiangolo.com/tutorial/testing/",
            },
            {
                "slug": "debugging",
                "title": "Debugging",
                "url": "https://fastapi.tiangolo.com/tutorial/debugging/",
            },
        ],
    },
    {
        "slug": "advanced-user-guide",
        "title": "Advanced User Guide: respuestas y dependencias avanzadas",
        "lessons": [
            {
                "slug": "advanced-user-guide",
                "title": "Advanced User Guide",
                "url": "https://fastapi.tiangolo.com/advanced/",
            },
            {
                "slug": "stream-data",
                "title": "Stream Data",
                "url": "https://fastapi.tiangolo.com/advanced/stream-data/",
            },
            {
                "slug": "path-operation-advanced-configuration",
                "title": "Path Operation Advanced Configuration",
                "url": "https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/",
            },
            {
                "slug": "additional-status-codes",
                "title": "Additional Status Codes",
                "url": "https://fastapi.tiangolo.com/advanced/additional-status-codes/",
            },
            {
                "slug": "return-a-response-directly",
                "title": "Return a Response Directly",
                "url": "https://fastapi.tiangolo.com/advanced/response-directly/",
            },
            {
                "slug": "custom-response-html-stream-file-others",
                "title": "Custom Response - HTML, Stream, File, others",
                "url": "https://fastapi.tiangolo.com/advanced/custom-response/",
            },
            {
                "slug": "additional-responses-in-openapi",
                "title": "Additional Responses in OpenAPI",
                "url": "https://fastapi.tiangolo.com/advanced/additional-responses/",
            },
            {
                "slug": "response-cookies",
                "title": "Response Cookies",
                "url": "https://fastapi.tiangolo.com/advanced/response-cookies/",
            },
            {
                "slug": "response-headers",
                "title": "Response Headers",
                "url": "https://fastapi.tiangolo.com/advanced/response-headers/",
            },
            {
                "slug": "response-change-status-code",
                "title": "Response - Change Status Code",
                "url": "https://fastapi.tiangolo.com/advanced/response-change-status-code/",
            },
            {
                "slug": "advanced-dependencies",
                "title": "Advanced Dependencies",
                "url": "https://fastapi.tiangolo.com/advanced/advanced-dependencies/",
            },
        ],
    },
    {
        "slug": "advanced-security",
        "title": "Advanced Security y middlewares",
        "lessons": [
            {
                "slug": "advanced-security",
                "title": "Advanced Security",
                "url": "https://fastapi.tiangolo.com/advanced/security/",
            },
            {
                "slug": "oauth2-scopes",
                "title": "OAuth2 scopes",
                "url": "https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/",
            },
            {
                "slug": "http-basic-auth",
                "title": "HTTP Basic Auth",
                "url": "https://fastapi.tiangolo.com/advanced/security/http-basic-auth/",
            },
            {
                "slug": "using-the-request-directly",
                "title": "Using the Request Directly",
                "url": "https://fastapi.tiangolo.com/advanced/using-request-directly/",
            },
            {
                "slug": "using-dataclasses",
                "title": "Using Dataclasses",
                "url": "https://fastapi.tiangolo.com/advanced/dataclasses/",
            },
            {
                "slug": "advanced-middleware",
                "title": "Advanced Middleware",
                "url": "https://fastapi.tiangolo.com/advanced/middleware/",
            },
        ],
    },
    {
        "slug": "subapps-proxy-templates-websockets",
        "title": "Subaplicaciones, proxy, plantillas, WebSockets y ciclo de vida",
        "lessons": [
            {
                "slug": "sub-applications-mounts",
                "title": "Sub Applications - Mounts",
                "url": "https://fastapi.tiangolo.com/advanced/sub-applications/",
            },
            {
                "slug": "behind-a-proxy",
                "title": "Behind a Proxy",
                "url": "https://fastapi.tiangolo.com/advanced/behind-a-proxy/",
            },
            {
                "slug": "templates",
                "title": "Templates",
                "url": "https://fastapi.tiangolo.com/advanced/templates/",
            },
            {
                "slug": "websockets",
                "title": "WebSockets",
                "url": "https://fastapi.tiangolo.com/advanced/websockets/",
            },
            {
                "slug": "lifespan-events",
                "title": "Lifespan Events",
                "url": "https://fastapi.tiangolo.com/advanced/events/",
            },
        ],
    },
    {
        "slug": "testing-settings-openapi",
        "title": "Testing avanzado, settings y OpenAPI extendido",
        "lessons": [
            {
                "slug": "testing-websockets",
                "title": "Testing WebSockets",
                "url": "https://fastapi.tiangolo.com/advanced/testing-websockets/",
            },
            {
                "slug": "testing-events-lifespan-startup-shutdown",
                "title": "Testing Events: lifespan and startup - shutdown",
                "url": "https://fastapi.tiangolo.com/advanced/testing-events/",
            },
            {
                "slug": "testing-dependencies-with-overrides",
                "title": "Testing Dependencies with Overrides",
                "url": "https://fastapi.tiangolo.com/advanced/testing-dependencies/",
            },
            {
                "slug": "async-tests",
                "title": "Async Tests",
                "url": "https://fastapi.tiangolo.com/advanced/async-tests/",
            },
            {
                "slug": "settings-and-environment-variables",
                "title": "Settings and Environment Variables",
                "url": "https://fastapi.tiangolo.com/advanced/settings/",
            },
            {
                "slug": "openapi-callbacks",
                "title": "OpenAPI Callbacks",
                "url": "https://fastapi.tiangolo.com/advanced/openapi-callbacks/",
            },
            {
                "slug": "openapi-webhooks",
                "title": "OpenAPI Webhooks",
                "url": "https://fastapi.tiangolo.com/advanced/openapi-webhooks/",
            },
        ],
    },
    {
        "slug": "integration-wsgi-generating-clients",
        "title": "Integración con WSGI, generación de clientes y tipos avanzados",
        "lessons": [
            {
                "slug": "including-wsgi",
                "title": "Including WSGI - Flask, Django, others",
                "url": "https://fastapi.tiangolo.com/advanced/wsgi/",
            },
            {
                "slug": "generating-sdks",
                "title": "Generating SDKs",
                "url": "https://fastapi.tiangolo.com/advanced/generate-clients/",
            },
            {
                "slug": "advanced-python-types",
                "title": "Advanced Python Types",
                "url": "https://fastapi.tiangolo.com/advanced/advanced-python-types/",
            },
            {
                "slug": "json-with-bytes-as-base64",
                "title": "JSON with Bytes as Base64",
                "url": "https://fastapi.tiangolo.com/advanced/json-base64-bytes/",
            },
            {
                "slug": "strict-content-type-checking",
                "title": "Strict Content-Type Checking",
                "url": "https://fastapi.tiangolo.com/advanced/strict-content-type/",
            },
        ],
    },
    {
        "slug": "cli-editor-deployment",
        "title": "CLI, editor y despliegue",
        "lessons": [
            {
                "slug": "fastapi-cli",
                "title": "FastAPI CLI",
                "url": "https://fastapi.tiangolo.com/fastapi-cli/",
            },
            {
                "slug": "editor-support",
                "title": "Editor Support",
                "url": "https://fastapi.tiangolo.com/editor-support/",
            },
            {
                "slug": "deployment",
                "title": "Deployment",
                "url": "https://fastapi.tiangolo.com/deployment/",
            },
            {
                "slug": "about-fastapi-versions",
                "title": "About FastAPI versions",
                "url": "https://fastapi.tiangolo.com/deployment/versions/",
            },
            {
                "slug": "fastapi-cloud",
                "title": "FastAPI Cloud",
                "url": "https://fastapi.tiangolo.com/deployment/fastapicloud/",
            },
            {
                "slug": "about-https",
                "title": "About HTTPS",
                "url": "https://fastapi.tiangolo.com/deployment/https/",
            },
            {
                "slug": "run-a-server-manually",
                "title": "Run a Server Manually",
                "url": "https://fastapi.tiangolo.com/deployment/manually/",
            },
            {
                "slug": "deployments-concepts",
                "title": "Deployments Concepts",
                "url": "https://fastapi.tiangolo.com/deployment/concepts/",
            },
            {
                "slug": "deploy-fastapi-on-cloud-providers",
                "title": "Deploy FastAPI on Cloud Providers",
                "url": "https://fastapi.tiangolo.com/deployment/cloud/",
            },
            {
                "slug": "server-workers-uvicorn-with-workers",
                "title": "Server Workers - Uvicorn with Workers",
                "url": "https://fastapi.tiangolo.com/deployment/server-workers/",
            },
            {
                "slug": "fastapi-in-containers-docker",
                "title": "FastAPI in Containers - Docker",
                "url": "https://fastapi.tiangolo.com/deployment/docker/",
            },
        ],
    },
    {
        "slug": "how-to-recipes",
        "title": "How To / Recipes",
        "lessons": [
            {
                "slug": "how-to-recipes",
                "title": "How To - Recipes",
                "url": "https://fastapi.tiangolo.com/how-to/",
            },
            {
                "slug": "general-how-to-recipes",
                "title": "General - How To - Recipes",
                "url": "https://fastapi.tiangolo.com/how-to/general/",
            },
            {
                "slug": "migrate-from-pydantic-v1-to-pydantic-v2",
                "title": "Migrate from Pydantic v1 to Pydantic v2",
                "url": "https://fastapi.tiangolo.com/how-to/migrate-from-pydantic-v1-to-pydantic-v2/",
            },
            {
                "slug": "graphql",
                "title": "GraphQL",
                "url": "https://fastapi.tiangolo.com/how-to/graphql/",
            },
            {
                "slug": "custom-request-and-apiroute-class",
                "title": "Custom Request and APIRoute class",
                "url": "https://fastapi.tiangolo.com/how-to/custom-request-and-route/",
            },
            {
                "slug": "conditional-openapi",
                "title": "Conditional OpenAPI",
                "url": "https://fastapi.tiangolo.com/how-to/conditional-openapi/",
            },
            {
                "slug": "extending-openapi",
                "title": "Extending OpenAPI",
                "url": "https://fastapi.tiangolo.com/how-to/extending-openapi/",
            },
            {
                "slug": "separate-openapi-schemas-for-input-and-output-or-not",
                "title": "Separate OpenAPI Schemas for Input and Output or Not",
                "url": "https://fastapi.tiangolo.com/how-to/separate-openapi-schemas/",
            },
            {
                "slug": "custom-docs-ui-static-assets-self-hosting",
                "title": "Custom Docs UI Static Assets (Self-Hosting)",
                "url": "https://fastapi.tiangolo.com/how-to/custom-docs-ui-assets/",
            },
            {
                "slug": "configure-swagger-ui",
                "title": "Configure Swagger UI",
                "url": "https://fastapi.tiangolo.com/how-to/configure-swagger-ui/",
            },
            {
                "slug": "testing-a-database",
                "title": "Testing a Database",
                "url": "https://fastapi.tiangolo.com/how-to/testing-database/",
            },
            {
                "slug": "use-old-403-authentication-error-status-codes",
                "title": "Use Old 403 Authentication Error Status Codes",
                "url": "https://fastapi.tiangolo.com/how-to/authentication-error-status-code/",
            },
        ],
    },
]

routers = []

global_router = APIRouter()


@global_router.get("/catalog", tags=["Catalog"])
def read_catalog():
    return {
        "title": "FastAPI tutorial catalog",
        "sections": [
            {
                "title": section["title"],
                "path": f"/{section['slug']}",
                "lessons": [
                    {
                        "title": lesson["title"],
                        "path": f"/{section['slug']}/{lesson['slug']}",
                        "reference_url": lesson["url"],
                    }
                    for lesson in section["lessons"]
                ],
            }
            for section in SECTION_DEFINITIONS
        ],
    }


routers.append(global_router)
routers.extend(lesson_routers_list)

def build_section_router(section: dict) -> APIRouter:
    router = APIRouter(prefix=f"/{section['slug']}", tags=[section["title"]])

    @router.get("/")
    def read_section():
        return {
            "section": section["title"],
            "section_path": f"/{section['slug']}",
            "lessons": [
                {
                    "title": lesson["title"],
                    "path": f"/{section['slug']}/{lesson['slug']}",
                    "reference_url": lesson["url"],
                }
                for lesson in section["lessons"]
            ],
        }

    return router


for section in SECTION_DEFINITIONS:
    routers.append(build_section_router(section))
