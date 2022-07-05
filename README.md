# discord-bot
T.I.F.F. is a Discord bot for the Guardians of Esoterra guild.

```
▀█▀ ▀ █▀ █▀ 
░█░ █ █▀ █▀ 
░▀░ ▀ ▀░ ▀░
```


## Python Setup
- Set up a new `venv` using Python 3.7 for this project.
- Install the `requirements.txt` into the `venv` using the command `pip install -r requirements.txt` in the local Terminal.


## Discord Setup
- The package `python-dotenv` reads key-value pairs from an `.env` file and can set them as environment variables. 
- The `DISCORD_CLIENT_SECRET` environment variable is called in `discord.run()` to start the bot.
- Paste the Discord Client ID and Discord Client Secret from the Discord Developers [webpage](https://discord.com/developers/applications/976609136743686174/information) into the `.env` file. This `.env` file should be added to the root of the repository and should not be committed to the repository.