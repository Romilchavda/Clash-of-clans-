import discord
from Script.Const_variables.import_const import Ids
from Script.import_functions import create_embed_img


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
        embed = create_embed_img(f"Unfortunately, {member.name} left us", "", member.color, "", member.guild.me.avatar_url, member.avatar_url)
        await welcome.send(embed=embed)
    return
