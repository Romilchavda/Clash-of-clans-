import discord
<<<<<<< HEAD
import datetime
from Script.Const_variables.import_const import Ids
from Script.import_functions import create_embed
=======
from Script.Const_variables.import_const import Ids
from Script.import_functions import create_embed_img
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9


async def member_remove(self, member):
    if member.guild.id == Ids["Support"]:
        nb_humans = 0
        for members in member.guild.members:
            if members.bot == 0:
                nb_humans += 1
        x = 0
        for channel in member.guild.channels:
            if channel.name.startswith("👤 "):
                await channel.edit(name="👤 Users : " + str(nb_humans))
                x = 1
        if x == 0:
            overwrite = {member.guild.default_role: discord.PermissionOverwrite(connect=False, view_channel=True)}
            await member.guild.create_voice_channel("👤 Users : " + str(nb_humans), overwrites=overwrite)

        welcome = self.get_channel(Ids["Welcome"])
<<<<<<< HEAD
        embed = create_embed(f"Unfortunately, {member.name} left us", f"{member.name}#{member.discriminator} (`{member.id}`) left us. He/She joined the server the {member.joined_at.date().isoformat()} ({0-(member.joined_at.date()-datetime.datetime.now().date()).days} days ago)", member.color, "", member.guild.me.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
=======
        embed = create_embed_img(f"Unfortunately, {member.name} left us", "", member.color, "", member.guild.me.avatar_url, member.avatar_url)
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
        await welcome.send(embed=embed)
    return
