team_char = input().split()
select_char = input().split()

list_team_char = set(team_char)
list_select_char = set(select_char)

use_char = list_select_char - list_team_char

print(len(use_char))