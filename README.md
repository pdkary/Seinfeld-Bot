# Seinfeld-Bot
A Chatbot with the intent of learning and writing Seinfeld episodes.

## get_episodes.py
Using the file seinfeld-scripts.html, (pulled from http://www.seinfeldscripts.com), locate and find the names of each and every episode, along with the links to the respected script link. Outputs for a file of episode names.

## extract_scripts.py
Using Regex, and Beautifulsoup, download the html script, and convert it into simple text. This text is then filtered into individual users dialog, and converted into a "corpus" using each characters lines, and the preceeding line from another character.

## chatterbot_corpus.py
Using these created corpus files, train a chatterbot, and produce a small conversation.

## chatterbot_list.py
Rather than using corpus files, all dialog is simply put into a large list, and chatterbot is trained using this.
