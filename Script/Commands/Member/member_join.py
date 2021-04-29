import discord
from Script.Const_variables.import_const import Ids
from Script.import_functions import create_embed_img

from PIL import Image, ImageDraw, ImageFont, ImageOps
import io
WelcomeImage = Image.open("Pictures/Welcome.png")
Font = ImageFont.truetype("ttf/Supercell-magic-webfont.x-font-ttf", 100)


async def member_join(self, member):
    if member.guild.id == Ids["Support_server"]:
        nb_humans = 0
        for members in member.guild.members:
            if members.bot == 0:
                nb_humans += 1
        for channel in member.guild.channels:
            if channel.name.startswith("👤 "):
                await channel.edit(name="👤 Users : " + str(nb_humans))
                break
        if "channel" not in locals():
            overwrite = {member.guild.default_role: discord.PermissionOverwrite(connect=False, view_channel=True)}
            await member.guild.create_voice_channel("👤 Users : " + str(nb_humans), overwrites=overwrite)
        role = discord.utils.get(member.guild.roles, name="Rules not checked")
        await member.add_roles(role)

        welcome = self.get_channel(Ids["Welcome"])

        image = WelcomeImage
        buffer_avatar = io.BytesIO()
        await member.avatar_url.save(buffer_avatar)
        buffer_avatar.seek(0)

        avatar = Image.open(buffer_avatar)
        avatar = avatar.resize((512, 512))
        bigsize = (avatar.size[0] * 3, avatar.size[1] * 3)
        mask = Image.new("L", bigsize, 0)
        draw = ImageDraw.Draw(mask)

        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(avatar.size, Image.ANTIALIAS)
        avatar.putalpha(mask)

        output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)

        avatar_image = output
        avatar_size = 768
        image = image.resize((1920, 1080))
        image_width, image_height = image.size
        avatar_image = avatar_image.resize((avatar_size, avatar_size))

        background = WelcomeImage
        foreground = avatar_image
        x = (1024 - avatar_size) // 2
        y = (image_height - avatar_size) // 2
        background.paste(foreground, (x, y), foreground)
        image = background

        draw = ImageDraw.Draw(image)

        text_width, text_height = draw.textsize("Welcome " + member.name, font=Font)
        x = (image_width - text_width) // 2
        y = (image_height - text_height) // 2 - 400
        draw.text((x, y), "Welcome " + member.name, fill=(0, 0, 255), font=Font)
        text_width, text_height = draw.textsize("Clash INFO support server", font=Font)
        x = (image_width - text_width) // 2
        y = (image_height - text_height) // 2 + 400
        draw.text((x, y), "Clash INFO support server", fill=(0, 0, 255), font=Font)

        buffer_output = io.BytesIO()
        image.save(buffer_output, format="PNG")
        buffer_output.seek(0)
        file = discord.File(buffer_output, "welcome.png")
        url = "attachment://welcome.png"

        embed = create_embed_img(f"Welcome {member.name} !", f"ID : `{member.id}`", member.color, "", member.guild.me.avatar_url, url)
        await welcome.send(embed=embed, file=file)
    return
