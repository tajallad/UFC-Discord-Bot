# UFC-Discord-Bot
This bot will check daily at 1:00 AM PDT for a UFC event matching the current date. If a match is found, it will ping the specified role, alerting them of Main Event fighters, time, and date. 

# Commands
Bot does not need to be mentioned for commands to work. Simply type a command into a channel the bot has access to.

`!fetch` -  Populate the table with event data scraped from ufc.com/events

`!events` - Bot will message the channel the command was issued in with the populated table

`!refresh` - Empty the current event table and populate with new data

# Environment Variables
Bot host will need to provide a `.env` file. This file should contain the bot token, channel_id for which fight alerts are sent to, and role_id for which alerts are sent to.

Example:  
`TOKEN=slaeicjslaicnas.12da2taa`  
`CHANNEL_ID=102397510213754`  
`ROLE_ID=219837985719821`  
