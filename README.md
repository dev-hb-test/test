# hafid
Hafid is a discord bot that can learn and communicate

## How to use

To use Hafid in discord app follow these steps :

- create a discord bot and retrieve bot token
- put token in .env file
- host php file in a php server
- import database to your MySQL server
- install python dependencies (discord, requests, bs4, ...)
- change data_server link in vocab.py file to your api link
- edit vocabulary.json
- edit normalization.json
- run hafid.py
- you're all set up, go to discord and test hafid

## how to add new action

- go to actions.json and add an action object (specify name, keywords that fires the action and max keywords that you message must contain)
- open actionner.py file and add action name and a function to self.functions dict variable
- create the function inside Actionner class
- do the process inside the function and return the response

<br/>
<br/>

<a href='https://devcrawlers.com' target='_blank'>
  <img src='https://devcrawlers.com/img/logo.png' alt='DevCrawlers Logo' width='200'/>
</a>
<br/>
&copy; 2020 DevCrawlers Open Source, All Rights Reserved
