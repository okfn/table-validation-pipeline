from importlib import import_module
from ..file import File


def describe(source, *, source_type=None, **options):
    """Describe the data source

    API      | Usage
    -------- | --------
    Public   | `from frictionless import describe`

    Parameters:
        source (any): data source
        source_type (str): source type - `schema`, `resource` or `package`
        **options (dict): options for the underlaying describe function

    Returns:
        Package|Resource|Schema: metadata
    """
    if not source_type:
        file = File(source, basepath=options.get("basepath", ""))
        source_type = "package" if file.multipart else "resource"
    module = import_module("frictionless.describe")
    describe = getattr(module, "describe_%s" % source_type)
    return describe(source, **options)
