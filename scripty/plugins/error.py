import hikari
import lightbulb

from scripty import functions


error = lightbulb.Plugin("Error")


@error.listener(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    if isinstance(event.exception, lightbulb.CommandInvocationError):
        embed = hikari.Embed(
            title="Error",
            description="This interaction failed",
            color=functions.Color.red(),
        )
        await event.context.respond(embed)
        raise event.exception

    # Setup other error handling instances

    # exception = event.exception.__cause__ or event.exception

    # if isinstance(exception, lightbulb.NotOwner):
    #     await event.context.respond("You are not the owner of this bot.")
    # elif isinstance(exception, lightbulb.CommandIsOnCooldown):
    #     await event.context.respond(f"This command is on cooldown. Retry in `{exception.retry_after:.2f}` seconds.")
    # elif isinstance(exception, lightbulb.CheckFailure):
    #     await event.context.respond(f"The checks failed for this command.")
    # else:
    #     raise exception


def load(bot: lightbulb.BotApp):
    bot.add_plugin(error)


def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(error)
