import discord
import datetime
from Script.Const_variables.import_const import Ids
from Script.import_functions import create_embed


async def member_remove(self, member):
    if member.guild.id == Ids["Support_server"]:
        nb_humans = 0
        for members in member.guild.members:
            if members.bot == 0:
                nb_humans += 1
        for channel in member.guild.channels:
            if channel.name.startswith("👤 Users : "):
                await channel.edit(name="👤 Users : " + str(nb_humans))
                break
        if "channel" not in locals():
            overwrite = {member.guild.default_role: discord.PermissionOverwrite(connect=False, view_channel=True)}
            await member.guild.create_voice_channel("👤 Users : " + str(nb_humans), overwrites=overwrite)
        welcome = self.get_channel(Ids["Welcome"])
        time_spent_on_the_server = (datetime.datetime.now().date() - member.joined_at.date()).days
        if time_spent_on_the_server > 1:
            embed = create_embed(f"Unfortunately, {member.name} left us", f"{member.name}#{member.discriminator} (`{member.id}`) left us. He/She joined the server the {member.joined_at.date().isoformat()} ({time_spent_on_the_server} days ago)", member.color, "", member.guild.me.avatar_url)
            embed.set_thumbnail(url=member.avatar_url)
            await welcome.send(embed=embed)
        else:
            async for message in welcome.history(limit=None):
                old_embed = message.embeds[0]
                if int(old_embed.description.split("`")[1]) == member.id:
                    new_embed = old_embed
                    new_embed.description = old_embed.description + "TesT"
                    await message.edit(embed=new_embed)
                    break
    return
