from redbot.core.bot import Red
from .duel import Duel

async def setup(bot: Red) -> None:
    await bot.add_cog(Duel())
