from redbot.core import commands
import discord
import requests
import json

class ytSearch(commands.Cog):
    """Easy youtube searcher"""

    @commands.command()
    async def ytSearch(self, ctx):
        headers = {
            "Authroization": "Bearer AIzaSyCG2iX8LVoryxzA2HBb80EOVnWkGaoPye4",
            "Accept": "application/json",
            "Content-Type": "application/json"

        }

        def search(mySearch):
            params = {}
            mySearch = mySearch.replace(" ", "%20")
            response = requests.get("https://www.googleapis.com/youtube/v3/search?q={}&key=AIzaSyCG2iX8LVoryxzA2HBb80EOVnWkGaoPye4".format(mySearch), headers=headers, params=params)
            return response.text

        mySearch = input('Enter search item here: ')
        myResults = json.loads(search(mySearch))
        numResults = myResults['pageInfo']['resultsPerPage']

        for i in range(numResults):
            ctx.send('https://www.youtube.com/watch?v=' + myResults['items'][i-1]['id']['videoId'])