def getUserFromMention(mention):

    if (mention.startsWith('<@') and mention.endsWith('>')):
        mention = mention.slice[2:-1]

        if (mention.startsWith('!')):
            mention = mention.replace("!","")

        return client.users.cache.get(mention)
