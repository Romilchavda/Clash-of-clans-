import coc
from Data.Const_variables.import_const import Login


key_name = "Clash INFO"
Clash_of_clans = coc.login(Login["clash of clans"]["email"], Login["clash of clans"]["password"], key_names=key_name, key_count=10)
