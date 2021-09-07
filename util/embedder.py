from typing import Optional, Union

import nextcord
from nextcord.embeds import EmptyEmbed, _EmptyEmbed

DEFAULT_COLOUR = nextcord.Colour.blurple()
MAX_EMBED_DESC_LENGTH = 4096
MAX_EMBED_TITLE_LENGTH = 256
MAX_EMBED_FOOTER_LENGTH = 2048


def __trim(text: str, limit: int) -> str:
    """limits text to a certain number of characters"""
    return text[: limit - 3].strip() + "..." if len(text) > limit else text


def embed_success(
    title: str,
    desc: Optional[str] = None,
    footer: Optional[str] = None,
    url: Union[str, _EmptyEmbed] = EmptyEmbed,
    image: Optional[str] = None,
    thumbnail: Optional[str] = None,
) -> nextcord.Embed:
    """Embed a success message and an optional description, footer, and URL"""
    return build_embed(
        title, desc, footer, url, nextcord.Colour.green(), image, thumbnail
    )


def embed_warning(
    title: str,
    desc: Optional[str] = None,
    footer: Optional[str] = None,
    url: Union[str, _EmptyEmbed] = EmptyEmbed,
    image: Optional[str] = None,
    thumbnail: Optional[str] = None,
) -> nextcord.Embed:
    """Embed a warning message and an optional description, footer, and URL"""
    return build_embed(
        title, desc, footer, url, nextcord.Colour.gold(), image, thumbnail
    )


def embed_error(
    title: str,
    desc: Optional[str] = None,
    footer: Optional[str] = None,
    url: Union[str, _EmptyEmbed] = EmptyEmbed,
    image: Optional[str] = None,
    thumbnail: Optional[str] = None,
) -> nextcord.Embed:
    """Embed an error message and an optional description, footer, and URL"""
    return build_embed(
        title, desc, footer, url, nextcord.Colour.red(), image, thumbnail
    )


def build_embed(
    title: str,
    desc: Optional[str] = None,
    footer: Optional[str] = None,
    url: Union[str, _EmptyEmbed] = EmptyEmbed,
    colour: nextcord.Colour = DEFAULT_COLOUR,
    image: Optional[str] = None,
    thumbnail: Optional[str] = None,
) -> nextcord.Embed:
    """Embed a message and an optional description, footer, and URL"""
    embed = nextcord.Embed(
        title=__trim(title, MAX_EMBED_TITLE_LENGTH), url=url, colour=colour
    )
    if desc:
        embed.description = __trim(desc, MAX_EMBED_DESC_LENGTH)
    if footer:
        embed.set_footer(text=__trim(footer, MAX_EMBED_FOOTER_LENGTH))
    if image:
        embed.set_image(url=image)
    if thumbnail:
        embed.set_thumbnail(url=thumbnail)
    return embed
