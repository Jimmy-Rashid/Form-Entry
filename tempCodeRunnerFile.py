lobby = amogus.concat(crewmate_list, ignore_index=True)
lobby.to_excel("output.xlsx", index=False)

lobby_update = amogus.concat([previous_lobby, lobby], ignore_index=True)
lobby_update.to_excel("master.xlsx", index=False)