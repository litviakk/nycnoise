from meta.views import Meta
from django.templatetags.static import static


def get_meta(
    url=None,
    title="nyc noise",
    description=(
        "NYC experimental live music calendar • noise, improv, jazz, new music,"
        " avant-electronics, weirdos • performance against corporate interests!"
    ),
    redirect=None,
    redirect_time=10,
):
    """
    Generate Meta tags for pages.

    Args:
        url (str, optional): The base URL for the page. Defaults to None.
        title (str, optional): The title of the page. Defaults to "nyc noise".
        description (str, optional): A brief description of the page content.
            Defaults to a description about NYC experimental live music.
        redirect (str): If provided, sets up a page redirect to the specified URL.
        redirect_time (int): Sets the delay (in seconds) before redirect occurs.
            Defaults to 10 seconds if not specified.
    """
    meta = Meta(
        title=title,
        url=f"{url or ''}/",
        description=description,
        image=static("core/images/NYC-Noise-facebook-preview-TOO-BIG.png"),
    )

    if redirect:
        meta.extra_custom_props = [
            ("http-equiv", "refresh", f"{redirect_time}; url={redirect}")
        ]

    return meta
