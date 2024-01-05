from importlib.metadata import PackageNotFoundError, version


def get_version() -> str:
    try:
        return version("json-editor")
    except PackageNotFoundError:
        # package is not installed
        return "DEV"
