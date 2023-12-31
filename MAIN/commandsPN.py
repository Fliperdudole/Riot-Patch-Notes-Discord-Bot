# Import libraries
import discord
from discord.ext import commands

# Helper libraries
import ValorantPN
import LeaguePN
import saveVar



# This function sets the channel ID to whereever it was called from
async def channel_set(ctx, default_channel_id):
    if ctx.message.content.lower() == "!setchannel":# This response allows the user to set the channel they want the notifications in
        
        default_channel_id = ctx.message.channel.id
        await ctx.send('Notifcations will now be sent here.') 
        print(f"Notification Channel Updated to: {ctx.message.channel} (Server: {ctx.guild.name})\n")


        # save updated default channel
        saveVar.save_default_channel(default_channel_id)

    
    return None




# This command calls function 'channel_set()"
@commands.command()
async def setchannel(ctx):
        server_id = str(ctx.guild.id)
        channel_id = str(ctx.message.channel.id)
        saveVar.update_default_channel(server_id, channel_id, default_channels)
        await ctx.send("Default notification channel updated.")     

# Load the default channel ID when the commands starts
default_channels = saveVar.load_default_channels()     


# This command gives the user the notification role for the respective game
@commands.command()
async def valorant(ctx):
    if ctx.message.content.lower() == "!valorant":
        print(f"Command {ctx.message.content} has been recieved and sent by {ctx.message.author} (Server: {ctx.guild.name}) \n")
        giveRole = ValorantPN.role_name
        role = discord.utils.get(ctx.message.guild.roles, name=giveRole)
        if role: # if the user calls the command then give them the role
            try:
                await ctx.message.author.add_roles(role)
                # Currently set to DM's but if you want the message in general do "ctx.message.channel.send"
                await ctx.message.author.send(f'Role "{giveRole}" has been assigned to {ctx.message.author.mention}.')
                return
            # if the bot doesn't have permission then print
            except discord.Forbidden:
                await ctx.message.channel.send("I don't have permission to assign roles.")
                return
            
        else: #  if the user doesn't have the role then let them know 
            await ctx.message.channel.send(f'Role "{giveRole}" not found.')
            return
    # Processes the command through Discord's API
    await commands.process_commands(ctx.message)   


# This command removes the notification role for the respective game from the user
@commands.command()
async def rmvalorant(ctx):
    if ctx.message.content.lower() == "!rmvalorant":
        print(f"Command {ctx.message.content} has been recieved and sent by {ctx.message.author} (Server: {ctx.guild.name}) \n")
        removeRole = ValorantPN.role_name
        role = discord.utils.get(ctx.message.guild.roles, name=removeRole)
        if role: # if the user has the role then remove
            try:
                await ctx.message.author.remove_roles(role)
                # Currently set to DM's but if you want the message in general do "ctx.message.channel.send"
                await ctx.message.author.send(f'Role "{removeRole}" has been removed from {ctx.message.author.mention}.')
                return
            # if the bot doesn't have permission then print
            except discord.Forbidden:
                await ctx.message.channel.send("I don't have permission to remove roles.")
                return
            
        else:   #  if the user doesn't have the role then let them know 
            await ctx.message.channel.send(f'Role "{removeRole}" not found.')
            return
    # Processes the command through Discord's API
    await commands.process_commands(ctx.message)   



# This command gives the user the notification role for the respective game
@commands.command()
async def league(ctx):
    if ctx.message.content.lower() == "!league":
        print(f"Command {ctx.message.content} has been recieved and sent by {ctx.message.author} (Server: {ctx.guild.name}) \n")
        giveRole = LeaguePN.role_name
        role = discord.utils.get(ctx.message.guild.roles, name=giveRole)
        if role: # if the user calls the command then give them the role
            try:
                await ctx.message.author.add_roles(role)
                # Currently set to DM's but if you want the message in general do "ctx.message.channel.send"
                await ctx.message.author.send(f'Role "{giveRole}" has been assigned to {ctx.message.author.mention}.')
                return
            # if the bot doesn't have permission then print
            except discord.Forbidden:
                await ctx.message.channel.send("I don't have permission to assign roles.")
                return
            
        else: #  if the user doesn't have the role then let them know 
            await ctx.message.channel.send(f'Role "{giveRole}" not found.')
            return
    # Processes the command through Discord's API
    await commands.process_commands(ctx.message)   


# This command removes the notification role for the respective game from the user
@commands.command()
async def rmleague(ctx):
    if ctx.message.content.lower() == "!rmleague":
        print(f"Command {ctx.message.content} has been recieved and sent by {ctx.message.author} (Server: {ctx.guild.name}) \n")
        removeRole = LeaguePN.role_name
        role = discord.utils.get(ctx.message.guild.roles, name=removeRole)
        if role: # if the user has the role then remove
            try:
                await ctx.message.author.remove_roles(role)
                # Currently set to DM's but if you want the message in general do "ctx.message.channel.send"
                await ctx.message.author.send(f'Role "{removeRole}" has been removed from {ctx.message.author.mention}.')
                return
            # if the bot doesn't have permission then print
            except discord.Forbidden:
                await ctx.message.channel.send("I don't have permission to remove roles.")
                return
            
        else:   #  if the user doesn't have the role then let them know 
            await ctx.message.channel.send(f'Role "{removeRole}" not found.')
            return
    # Processes the command through Discord's API
    await commands.process_commands(ctx.message)   



# This is a help command as I was too lazy to mess with Discord's default help command
@commands.command()
async def helpPN(ctx):
    if ctx.message.content.lower() == "!helppn":
        print(f"Command {ctx.message.content} has been recieved and sent by {ctx.message.author} (Server: {ctx.guild.name}) \n")
        await ctx.message.channel.send("These are the current commands I can receive! \n" +
                                       "!setchannel - Set the notifications channel \n"+
                                       "!valorant - Add the Valorant-Patch-Notes role to receive notifications \n"+
                                       "!rmvalorant - Remove the Valorant-Patch-Notes role \n"+
                                       "!league - Add the League-Patch-Notes role to receive notifications \n"+
                                       "!rmleague - Remove the League-Patch-Notes role \n"+
                                       "!helpPN - Shows the commands  \n"
                                
                                       )
        

# This is a setup function to add the commands to the bot which is then loaded from the main file
async def setup(bot):
    bot.add_command(valorant)
    bot.add_command(rmvalorant)
    bot.add_command(league)
    bot.add_command(rmleague)

    bot.add_command(setchannel)

    bot.add_command(helpPN)