# Reboot the Raspberry Pi

import os


async def reboot(ctx):
    await ctx.send("The Raspberry Pi will be rebooted")
    os.system("sudo reboot")
    return
