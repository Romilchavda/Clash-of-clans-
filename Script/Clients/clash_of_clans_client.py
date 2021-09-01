# Initialize the Clash Of Clans client : Clash_of_clans

import coc

from Data.Const_variables.import_const import Login, Main_bot

if Main_bot:
    login = Login["clash of clans"]
else:
    login = Login["clash of clans beta"]
Clash_of_clans = coc.login(login["email"], login["password"], key_names="Clash INFO", key_count=10)
