from distutils.core import setup

setup(
    name="fastapi_sessions",
    packages=["fastapi_sessions","fastapi_sessions.backends","fastapi_sessions.frontends","fastapi_sessions.backends.implementations","fastapi_sessions.frontends.implementations"],
    version="0.1",
    license="MIT",
    description="Ready-to-use session cookies with custom backends for FastAPI",
    long_description=open("readme.md").read(),
    author="Jordan Isaacs",
    url="https://github.com/soo4767/fastapi-sessions",
    install_requires=["fastapi", "itsdangerous", "pydantic"],
)
